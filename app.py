from flask import Flask
from routes.Routes import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)


if __name__ == "__main__":
    app.run(host='localhost', port=4444, debug=True)