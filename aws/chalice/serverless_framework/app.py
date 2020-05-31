import logging

from chalice import Chalice

from chalicelib.lambda_function_1 import lambda_function_1_blueprint
from chalicelib.lambda_function_2 import lambda_function_2_blueprint
from chalicelib.lambda_function_3 import lambda_function_3_blueprint

logging.basicConfig(level=logging.INFO)
app = Chalice(app_name='serverless_framework')
app.log.setLevel(logging.INFO)

app.experimental_feature_flags.update([
    'BLUEPRINTS'
])

app.register_blueprint(lambda_function_1_blueprint)
app.register_blueprint(lambda_function_2_blueprint)
app.register_blueprint(lambda_function_3_blueprint)

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
