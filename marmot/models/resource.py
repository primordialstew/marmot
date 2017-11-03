import json

from sqlalchemy import (
    Column,
    Integer,
    # Index,
    Text,
)
from sqlalchemy.orm import validates
# from sqlalchemy.dialects.postgresql import JSONB

from .meta import Base


class Resource(Base):
    __tablename__ = 'resource'
    id = Column(Integer, primary_key=True)
    # rev = Column(Integer)
    # schema = Column(Text)
    body = Column(Text)

    @validates('body')
    def validate_json(self, key, value):
        json.loads(value)
        return value


# Index('my_index', MyModel.name, unique=True, mysql_length=255)
