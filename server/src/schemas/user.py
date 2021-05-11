from estoult import Query, Field, op

from .base import BaseSchema


class User(BaseSchema):
    __tablename__ = "users"

    email = Field(str)
    password = Field(str)

    @classmethod
    def get_by_email(cls, email):
        return (
            Query(cls)
            .get_or_none()
            .where(cls.email == email, op.not_null(cls.tombstoned))
            .execute()
        )
