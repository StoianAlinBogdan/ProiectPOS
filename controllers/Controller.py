from typing import get_args
import models.Model as model
from flask import Response, request
import view.View as view

'''
    tot codul asta: https://pbs.twimg.com/media/DpPJAOoUcAAxZa4.jpg
'''

def index():
    return "Hello World!"


def get_params(lrequest):
    dict = {}
    dict['title'] = lrequest.args.get("title")
    dict['publisher'] = lrequest.args.get("publisher")
    dict['year'] = lrequest.args.get("year")
    dict['genre'] = lrequest.args.get("genre")
    dict['page'] = lrequest.args.get("page")
    dict['items_per_page'] = lrequest.args.get("items_per_page")
    return dict

def books(ISBN):
    if(request.method == 'OPTIONS'):
        return handle_options_books()
    elif(request.method == 'POST'):
        return str(add_new_book(ISBN))
    elif(request.method == 'PUT'):
        return str(replace_book(ISBN))
    elif(request.method == 'DELETE'):
        return str(delete_book(ISBN))
    else:
        books = get_book(ISBN)
        if len(books) > 0:
            return Response(str(books), status=200, mimetype='text/plain')
        return Response('', status=404)


def get_book(ISBN):
    params = get_params(request)
    return model.get_book(ISBN)
    


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


def handle_search():
    if(request.method == "OPTIONS"):
        return handle_options_books()
    print("Search with pages or query")
    params = get_params(request)
    if(params['page']):
        if(params['items_per_page']):
            return Response(str(model.search_with_pages(params['page'], params['items_per_page'])), status=200, mimetype='text/plain')
        else:
            return Response(str(model.search_with_pages(params['page'])), status=200, mimetype='text/plain')
    elif(params):
        return Response(str(model.search_with_pages(queries={'title': params['title'], 'genre': params['genre'], 'year': params['year']})), status=200, mimetype='text/plain')
    else:
        return Response('???', status=404)


def handle_options_bookcollection():
    yaml = view.describe_bookcollection()
    return Response(str(yaml), status=200)


def handle_options_books():
    yaml = view.describe_books()
    return Response(str(yaml), status=200)


def handle_options_authors():
    yaml = view.describe_authors()
    return Response(str(yaml), status=200)