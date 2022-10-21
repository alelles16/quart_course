# Send a message from one place to another,
# when components are not directly connected

# We can use Blinker, which is a signal library that lets
# you subscribe a function to an event

# Quart triggers signals at critical moments during
# the processing of a request.

from quart import Quart, request_finished  # g
# from quart.signals import signals_available

app = Quart(__name__)

# For instance, the got_request_exception signal is triggered
# when an exception occurs
# before the framework does something with it.
# That's how Sentry's (https://sentry.io)
# Python client hooks itself in to log exceptions.


def finished(sender, response, **extra):
    print("About to send a Response")
    print(response)


def other_finished(sender, response, **extra):
    print("About to send a Response - 2")
    print(response)


request_finished.connect(finished)
request_finished.connect(other_finished)


@app.route("/api")
async def my_microservices():
    json = {"hello": "world"}
    print(json)
    return json


if __name__ == "__main__":
    app.run()
