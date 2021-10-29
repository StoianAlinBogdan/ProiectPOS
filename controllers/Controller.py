import models.Model as model
from flask import Response, request

def index():
    return "Hello World!"


def books(ISBN):
    if(request.method == 'POST'):
        return str(add_new_book(ISBN))
    else:
        books = model.get_book(ISBN)
        if len(books) > 0:
            return Response(str(books), status=200, mimetype='text/plain')
        return Response('', status=404)


def get_author(id):
    author = model.get_author(id)
    return str(author)


def add_new_book(ISBN):
    title = request.args.get("title")
    publisher = request.args.get("publisher")
    year = request.args.get("year")
    genre = request.args.get("genre")
    code = model.add_new_book(ISBN, title, publisher, year, genre)
    return code