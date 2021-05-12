from estoult import Query, Field, op

from .base import BaseSchema


class User(BaseSchema):
    __tablename__ = "users"

    email = Field(str)
    password = Field(str)

    @classmethod
    def get_by_email(cls, email):
        user = (
            Query(cls)
            .get_or_none()
            .where(cls.email == email, op.is_null(cls.tombstoned))
            .execute()
        )

        if user:
            user["type"] = "user"

        return user
