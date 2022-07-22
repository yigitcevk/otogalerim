import time
import logging
import psycopg2

from flask import Blueprint, request, jsonify

controller = Blueprint('api_controller', __name__, url_prefix='') # template_folders?
logger = logging.getLogger(__name__)


@controller.route('/brands', methods=['get'])
def brands():

    conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute('''select * from brand;''')
    brands = cur.fetchall()
    result = []
    result.append({'id':'0','name':''})
    for brand in brands:
        result.append({'id':brand[0],'name':brand[1]})
    conn.commit()
    conn.close()

    return jsonify(result)
@controller.route('/models', methods=['get'])
def models():
    conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute('''select * from model;''')
    models = cur.fetchall()
    cur.execute('''select count(*) from brand;''')
    totalBrands = cur.fetchall()[0][0]
    result = []
    for _ in range(totalBrands + 1):
        result.append([])
    for model in models:
        result[int(model[2])].append({'id':model[0],'name':model[1]})
    conn.commit()
    conn.close()

    return jsonify(result)