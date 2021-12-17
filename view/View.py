from apispec import APISpec
import apispec
from apispec_webframeworks.flask import FlaskPlugin
from yaml import add_implicit_resolver

import models.Model as model

def describe_bookcollection():
    spec = APISpec(
        title="Descriere pentru bookcollection ",
        version="1.0",
        openapi_version="3.0.3",
        plugins=[FlaskPlugin()],
        info=dict(
            description="Informatii pentru rute disponibile"
        ),
        paths="/books, /authors"
    )
    return spec.to_yaml()


def describe_books():
    spec = APISpec(
        title="Descriere pentru books",
        version="1.0",
        openapi_version="3.0.3",
        plugins=[FlaskPlugin()],
        info=dict(
            books=str(model.get_all_books())
        )
    )
    return spec.to_yaml()


def describe_authors():
    spec = APISpec(
        title="Descriere pentru authors",
        version="1.0",
        openapi_version="3.0.3",
        plugins=[FlaskPlugin()],
        info=dict(
            authors=str(model.get_all_authors())
        ),
        paths="/{id}"
    )
    return spec.to_yaml()