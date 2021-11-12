from flask import Blueprint

import controllers.Controller as controller

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(controller.index)
blueprint.route('/bookcollection/books/<string:ISBN>', methods=['GET', 'POST', 'PUT', 'DELETE'])(controller.books)
blueprint.route('/bookcollection/authors/<int:id>', methods=['GET'])(controller.get_author)
blueprint.route('/bookcollection/books/<string:ISBN>/authors', methods=['GET'])(controller.get_book_author)
blueprint.route('/bookcollection/books', methods=['GET'])(controller.handle_search)