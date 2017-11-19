# from pyramid.response import Response
from pyramid.view import view_defaults
from pyramid.view import view_config

# from sqlalchemy.exc import DBAPIError

import transaction

from ..models import Schemas


def includeme(config):
    certificate_path = config.registry.settings.get('certificate_path')
    if not certificate_path:
        """ Disable Insecure Request Warning spam if we're not using certs
        """
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RESTResource(object):

    view_name = None

    def __init__(self, request):
        self.request = request


@view_defaults(route_name='schemas', renderer='json')
class SchemasResource(RESTResource):

    view_name = 'schemas'

    @view_config(request_method='POST', route_name='schemas')
    def create(self):
        document = dict(self.request.json)
        name = document['title']
        with transaction.manager:
            record = Schemas(
                name=name,
                body=document,
            )
            self.request.dbsession.add(record)

        return self.request.response


# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(MyModel)
#         one = query.filter(MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'Marmot'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_marmot_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
