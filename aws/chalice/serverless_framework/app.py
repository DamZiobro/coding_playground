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
