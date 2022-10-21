# Quart provides a mechanism for storing global variables
# that are unique to a particular request context.

# That is used for request and session,
# but is also available to store any custom object.


# The quart.g variable contains all globals,
# and you can set whatever attributes you want on it. In Quart,
# the @app.before_request decorator can be used to
# point to a function that the app will call every time a request is made,
# just before it dispatches the request to a view.

from quart import Quart, g, request

app = Quart(__name__)


@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization["username"]
    else:
        g.user = "Anonymous"


@app.before_request
def greetings():
    g.say_hello = "Say hello!"


@app.route("/api")
def my_microservice():
    return {"Hello": g.user, "Info": g.say_hello}


if __name__ == "__main__":
    app.run()
