from flask import Flask
from flask_restplus import Api, Resource

from server.instance import server

app, api = server.app, server.api

mock_books = [
    {"id": 0, "title": "A volta dos que não foram"},
    {"id": 1, "title": "The lord of rings"},
    {"id": 1, "title": "Clean Code"},
]


@api.route("/books")
class BookList(Resource):
    def get(self):
        return mock_books
