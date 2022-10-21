from quart import Quart, request, jsonify


# When the service starts,Quart creates the QuartMap object,
# and we can see here what it knows about endpoints and the associated views.
app = Quart(__name__)


@app.route("/api", provide_automatic_options=False, methods=['GET'])
async def my_microservices():
    print(dir(request))
    response = jsonify({"hello": "world"})
    print(response)
    # Get data to retrieve any data that was sent with the request.
    print(await response.get_data())
    return response


@app.route('/person/<int:person_id>')
def person(person_id):
    return {'Hello': person_id}


@app.route("/<any('option1', 'option2'):segment>")
def hello(segment):
    return "Hello {}!".format(segment)


if __name__ == "__main__":
    # app.url_map instance of Quart Map
    # Validate name of endpoints - routing
    print(app.url_map)
    app.run()
