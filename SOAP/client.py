from soaplib.client import make_service_client
from app import HelloService

client = make_service_client("http://localhost:8080/hello.wsdl", HelloService())
client.hello("test")