import unittest
import transaction
from jsonschema.exceptions import SchemaError

from pyramid import testing


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'postgresql://marmot_app:devPass789@localhost:5432/marmot'  # noqa
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        from mammoth.models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from mammoth.models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from mammoth.models.meta import Base

        testing.tearDown()
        # transaction.abort()
        Base.metadata.drop_all(self.engine)


class TestModels(BaseTest):

    def setUp(self):
        super().setUp()
        self.init_database()

    def test_schema_validation(self):
        from .models import Schemas
        body = '''[]'''
        expected = None
        try:
            instance = Schemas(name='test_invalid', rev='1', body=body)
        except Exception as exc:
            expected = exc
        assert type(expected) == SchemaError
        # with transaction.manager:
        #     self.session.add(instance)
        #     transaction.commit()
