from peewee import *

__author__ = "Brandon Duke"

__version__ = ""
__email__ = "http://bduke.net"

"""
models:

Contains classes that are models for tables in the database
"""

""" the database connection string """
db = MySQLDatabase("dbf79d1040d58c4b2da431a88d017b1284", host="f79d1040-d58c-4b2d-a431-a88d017b1284.mysql.sequelizer.com", port=3306, user="elgyqslrczcdhpme", passwd="kdfd5rqRVKPdyWzmuym3jh4dZVvdEZphefNuZnw3mFkccxsqD2UZxJachbmi4mm5")


class MySQLModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = db


class event(MySQLModel):
    event_id = PrimaryKeyField()
    event_nm = CharField()
    event_cd = CharField()
    date_st = DateTimeField()
    date_end = DateTimeField()

    class Meta:
        db_table = "event"


class team(MySQLModel):
    team_no = PrimaryKeyField()
    team_nm = CharField()

    class Meta:
        db_table = "team"


class event_team_xref(MySQLModel):
    event = ForeignKeyField(event, to_field="event_id")
    team_no = ForeignKeyField(team, to_field="team_no", db_column="team_no")

    class Meta:
        db_table = "event_team_xref"


class pit(MySQLModel):
    pit_id = PrimaryKeyField()
    event = ForeignKeyField(event, to_field="event_id")
    team_no = ForeignKeyField(team, to_field="team_no", db_column="team_no")
    drivetrain = CharField()
    speed = CharField()
    climb = CharField()
    fabrication = CharField()
    rocket = CharField()
    auto = CharField()
    teleop = CharField()
    cargo_ship = CharField()
    hatch_mech = CharField()
    ball_mech = CharField()
    strategy = CharField()
    img_id = CharField()
    img_ver = CharField()

    class Meta:
        db_table = "pit"


class robot_match(MySQLModel):
    match_id = PrimaryKeyField()
    event = ForeignKeyField(event, to_field="event_id")
    team_no = ForeignKeyField(team, to_field="team_no", db_column="team_no")
    sandstorm = CharField()
    st_lvl = IntegerField()
    pre_cargo_hp = IntegerField()
    pre_cargo_c = IntegerField()
    pre_rocket_hp = IntegerField()
    pre_rocket_c = IntegerField()
    auto_cargo_hp = IntegerField()
    auto_cargo_c = IntegerField()
    auto_rocket_hp = IntegerField()
    auto_rocket_c = IntegerField()
    teleop_cargo_hp = IntegerField()
    teleop_cargo_c = IntegerField()
    teleop_rocket_hp = IntegerField()
    teleop_rocket_c = IntegerField()
    lv_climb = IntegerField()
    comments = CharField()

    class Meta:
        db_table = "robot_match"


class user(MySQLModel):
    user_id = PrimaryKeyField()
    username = CharField()
    password = CharField()
    email = CharField()
    confirmed_at = DateTimeField(null=True)
    active = BooleanField()
    first_name = CharField()
    last_name = CharField(null=True)

    class Meta:
        db_table = "user"


class role(MySQLModel):
    role_id = PrimaryKeyField()
    role_nm = CharField()

    class Meta:
        db_table = "role"


class user_roles(MySQLModel):
    user_role_id = PrimaryKeyField()
    user = ForeignKeyField(user, to_field="user_id")
    role = ForeignKeyField(role, to_field="role_id")

    class Meta:
        db_table = "user_roles"