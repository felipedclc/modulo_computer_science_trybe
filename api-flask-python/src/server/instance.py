from flask import Flask
from flask_restplus import Api


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,  # onde ficaram os controllers
            version="1.0",
            title="Simple book api",
            description="Xablau description",
            doc="/docs",
        )

    def run(self):
        self.app.run(debug=True)  # funciona como o nodemon


server = Server()
