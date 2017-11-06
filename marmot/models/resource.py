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
    type = Column(Text, primary_key=True)
    id = Column(Integer, primary_key=True)
    # rev = Column(Integer)
    body = Column(Text, server_default="'{}'")

    @validates('body')
    def well_formed_json(self, key, value):
        json.loads(value)
        return value

# Index('my_index', MyModel.name, unique=True, mysql_length=255)
