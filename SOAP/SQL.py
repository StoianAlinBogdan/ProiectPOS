import web
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types
import mysql.connector


urls = ("/authors", "HelloService",
        "/authors.wsdl", "HelloService",
)
render = web.template.Template("$def with (var)\n$:var")


class SoapService(SimpleWSGISoapApp):
    @soapmethod(soap_types.Null,_returns=soap_types.String)
    def get_authors(self):
        conn = mysql.connector.connect(
        host='localhost',
        port='3360',
        user='db_manager',
        database='mydb',
        password='Admin1234')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM BOOKS")
        books = []
        for book in cursor:
            books.append(book)
        return str(books)


class AuthorsService(SoapService):
        def start_response(self, status, headers):
            web.ctx.status = status
            for header, value in headers:
                web.header(header, value)
            

        def POST(self):
            response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
            return render("\n".join(str(response)))