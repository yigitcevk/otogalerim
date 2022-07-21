import time
import logging

from flask import Blueprint, request, jsonify

controller = Blueprint('api_controller', __name__, url_prefix='') # template_folders?
logger = logging.getLogger(__name__)


@controller.route('/brands', methods=['get'])
def brands():
    return jsonify([{
          "id":"0",
          "name":""
        },
        {
          "id":"1",
          "name":"audi"
        },
        {
          "id":"2",
          "name":"mercedes"
        },
        {
          "id":"3",
          "name":"bmw"
        }])

@controller.route('/models', methods=['get'])
def models():
    return jsonify([[],
            [
                {
                    "id":"0",
                    "name":"a3"
                },
                {
                    "id":"1",
                    "name":"a4"

                },
                {
                    "id":"2",
                    "name":"a5"
                }
            ],
            [
                {
                    "id":"0",
                    "name":"cla180"
                },
                {
                    "id":"1",
                    "name":"a180"

                },
                {
                    "id":"2",
                    "name":"g30"
                }
            ],

            [
                {
                    "id":"0",
                    "name":"i8"
                },
                {
                    "id":"1",
                    "name":"i3"

                },
                {
                    "id":"2",
                    "name":"320"
                }
            ],            
            
        ])