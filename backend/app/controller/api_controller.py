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

@controller.route('/galleryCars/<string:galleryId>', methods=['get'])
def galleryCars(galleryId):

    conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    sql_select_query = """select c.car_id,brand_name,model_name,uretim_yili,renk,durumu,km,yakit,vites,motor_hacmi,motor_gucu,on_sale from own as o, car as c, brand as b, model as m where c.model_id = m.model_id and c.brand_id = b.brand_id and o.car_id = c.car_id and o.gallery_id = %s"""
    cur.execute(sql_select_query, (galleryId,))
    car_ids = cur.fetchall()

    return jsonify(car_ids)