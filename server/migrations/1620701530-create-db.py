"""
create db
"""

from apocryphes.rider import step

__depends__ = {""}

# PW == password123
pw = (
    "pbkdf2:sha256:150000$4QU8ECxW$2b65956dda981f9ff"
    "eeb8aa3002e18b2569fae81cdc7d73f6dd38214fc6364af"
)

steps = [
    step(
        """
        create table users (
            id serial primary key,
            email varchar(128) not null,
            type varchar(56) not null,
            password varchar(128) not null,
            created timestamp default now() not null,
            updated timestamp default now() not null,
            tombstoned timestamp null
        );
    """
    ),

    #
    # Test data - TODO: remove
    #

    step(f"""
        insert into users (email, password) values ('astolfo@email.com', '{pw}');
        insert into users (email, password) values ('matthieu@email.com', '{pw}');
    """),
]
