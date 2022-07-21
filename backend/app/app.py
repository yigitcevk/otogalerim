from flask import Flask, render_template
from flask_cors import CORS

from .controller import api_controller

app = Flask('otogaleri', static_folder='')
app.register_blueprint(api_controller.controller)

CORS(app)
