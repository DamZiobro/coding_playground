from chalice import Chalice
import logging

logging.basicConfig(level=logging.INFO)
app = Chalice(app_name='helloworld')

CITIES_TO_REGION = {
    'Leeds': 'West Yorkshire',
    'Sheffield': 'South Yorkshire',
}

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/cities/{city}')
def state_of_city(city):
    logging.info(f"asking about state of city {city}")
    return {'state': CITIES_TO_REGION[city]}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
#@app.route('/hello/{name}')
#def hello_name(name):
    ## '/hello/james' -> {"hello": "james"}
    #return {'hello': name}

# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
