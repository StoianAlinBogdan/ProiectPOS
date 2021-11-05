from typing import get_args
import models.Model as model
from flask import Response, request

def index():
    return "Hello World!"


def get_params(lrequest):
    dict = {}
    dict['title'] = lrequest.args.get("title")
    dict['publisher'] = lrequest.args.get("publisher")
    dict['year'] = lrequest.args.get("year")
    dict['genre'] = lrequest.args.get("genre")
    return dict

def books(ISBN):
    if(request.method == 'POST'):
        return str(add_new_book(ISBN))
    elif(request.method == 'PUT'):
        return str(replace_book(ISBN))
    elif(request.method == 'DELETE'):
        return str(delete_book(ISBN))
    else:
        books = model.get_book(ISBN)
        if len(books) > 0:
            return Response(str(books), status=200, mimetype='text/plain')
        return Response('', status=404)


def get_author(id):
    author = model.get_author(id)
    if len(author) > 0:
        return Response(str(author), status=200, mimetype='text/plain')
    return Response('', status=404)


def add_new_book(ISBN):
    params = get_params(request)
    code = model.add_new_book(ISBN, params["title"], params["publisher"], params['year'], params['genre'])
    return code


def replace_book(ISBN):
    params = get_params(request)
    code = model.replace_book(ISBN, params["title"], params["publisher"], params["year"], params['genre'])
    return code

def delete_book(ISBN):
    code = model.delete_book(ISBN)
    return code


def get_book_author(ISBN):
    books = model.get_book_author(ISBN)
    if len(books) > 0:
        return Response(str(books), status=200, mimetype='text/plain')
    else:
        return Response('', status=404)