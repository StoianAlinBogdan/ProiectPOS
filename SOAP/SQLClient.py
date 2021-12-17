from soaplib.client import make_service_client
from SQL import SoapService

client = make_service_client("http://localhost:8080/authors", SoapService())
client.get_authors()