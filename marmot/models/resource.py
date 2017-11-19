from jsonschema import Draft4Validator
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Index,
    Text,
)
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
from sqlalchemy.dialects.postgresql import JSONB

from .meta import Base


class Schemas(Base):

    __tablename__ = 'schemas'

    name = Column(Text, primary_key=True)
    rev = Column(Integer, primary_key=True)
    start = Column(DateTime, nullable=False, server_default=func.now())
    end = Column(DateTime)
    body = Column(JSONB, server_default="{}")

    @validates('body')
    def valid_draft4_schema(self, key, schema):
        Draft4Validator.check_schema(schema)

Index(
    'ix_{0}_latest'.format(Schemas.__tablename__),
    Schemas.name,
    Schemas.end.is_(None),
    unique=True,
)


class Resource(Base):

    __abstract__ = True
    __table_args__ = {'schema': 'resources'}

    schema_name = Column(Text, nullable=False)
    schema_rev = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    rev = Column(Integer, primary_key=True)
    start = Column(DateTime, nullable=False, server_default=func.now())
    end = Column(DateTime)
    body = Column(JSONB, server_default="{}")


class Cities(Resource):
    __tablename__ = 'cities'


class Users(Resource):
    __tablename__ = 'users'


resources = (
    Cities,
    Users,
)
models = ((Schemas, ) + resources)
for cls in resources:
    Index(
        'ix_{0}_latest'.format(cls.__tablename__),
        cls.id,
        cls.end.is_(None),
        unique=True,
    )
    ForeignKeyConstraint([cls.schema_name, cls.schema_rev],
                         [Schemas.name, Schemas.rev])
