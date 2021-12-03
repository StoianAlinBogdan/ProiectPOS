from typing import get_args
import models.Model as model
import models.Model2 as model2
from flask import Response, request
import view.View as view
from datetime import date

def handle_order(ISBN):
    books = model.get_all_books()
    for book in books:
        if(book[0] == str(ISBN)):
        # adauga document in mongo (in model2)
            dict = {
                'date': str(date.today()),
                'ISBN': book[0],
                'title': book[1]
            }
        model2.add_order(dict)
        return Response('Felicitari', status=200)
    return Response('', status=404)
