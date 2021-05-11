"""
create db
"""

from apocryphes.rider import step

__depends__ = {""}

steps = [
    step("""
        create table users (
            id serial primary key,
            email varchar(256) not null,
            password varchar(128) not null,
            created timestamp default now() not null,
            updated timestamp default now() not null,
            tombstoned timestamp null
        );
    """),
]
