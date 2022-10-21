from quart import Quart, url_for
from werkzeug.routing import BaseConverter, ValidationError
import asyncio

_USERS = {"1": "Alice", "2": "Bob"}
_IDS = {val: user_id for user_id, val in _USERS.items()}


class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()

    def to_url(self, value):
        return _IDS[value]


app = Quart(__name__)
app.url_map.converters["registered"] = RegisteredUser


@app.route("/api/person/<registered:name>")
def person(name):
    return {"Hello": name}


async def run_url_for():
    async with app.test_request_context("/", method="GET"):
        print(url_for('person', name='Bob'))


if __name__ == "__main__":
    app.run()
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(run_url_for()))
