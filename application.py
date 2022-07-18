from flask import Flask

application = Flask(__name__)


@application.route("/")
def say_hello():
    return "<h1>Hello World!</h1>\n"


if __name__ == "__main__":
    application.debug = True
    application.run()
