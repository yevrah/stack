import datetime
import dateutil.parser

from apocryphes.pool import PooledPostgreSQLDatabase
from estoult import Field, FieldError, fn, Query

from config import config

db = PooledPostgreSQLDatabase(
    host=config["DB_HOST"],
    database=config["DB_NAME"],
    user=config["DB_USER"],
    password=config["DB_PASSWORD"],
)


def cast_date(date):
    if isinstance(date, datetime.date):
        return date

    if isinstance(date, str):
        try:
            return dateutil.parser.isoparse(date)
        except ValueError:
            pass

        for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%Y-%m-%d %H:%M:%S"):
            try:
                return datetime.datetime.strptime(date, fmt)
            except ValueError:
                pass

        raise ValueError("No valid date format found for " + str(date))

    return None


class BaseSchema(db.Schema):
    id = Field(int, primary_key=True)
    created = Field(datetime.datetime, caster=cast_date)
    updated = Field(datetime.datetime, caster=cast_date)
    tombstoned = Field(datetime.datetime, caster=cast_date, default=None)

    @classmethod
    def update(cls, old, new):
        new["updated"] = datetime.datetime.now()
        return super().update(old, new)

    @classmethod
    def insert(cls, data):
        data["updated"] = datetime.datetime.now()
        data["created"] = datetime.datetime.now()
        return super().insert(data)

    @classmethod
    def update_eh(cls, *args, **kwargs):
        try:
            return super().update(*args, **kwargs), None
        except FieldError as e:
            return None, e.args[0]

    @classmethod
    def insert_eh(cls, *args, **kwargs):
        try:
            return super().insert(*args, **kwargs), None
        except FieldError as e:
            return None, e.args[0]

    @classmethod
    def get_by_id(cls, id):
        return (
            Query(cls)
            .select()
            .where(cls.id == id, fn.is_null(cls.tombstoned))
            .execute()
        )
