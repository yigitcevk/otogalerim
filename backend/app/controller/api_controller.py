from random import randint
import time
import logging
import psycopg2
from datetime import date

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

@controller.route('/galleryForSale/<string:galleryId>', methods=['get'])
def galleryForSale(galleryId):
    print(galleryId)
    conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    sql_select_query = """select c.car_id,brand_name,model_name,uretim_yili,renk,durumu,km,yakit,vites,motor_hacmi,motor_gucu,price from for_sale as o, car as c, brand as b, model as m where c.model_id = m.model_id and c.brand_id = b.brand_id and o.car_id = c.car_id and o.gallery_id = %s"""
    cur.execute(sql_select_query, (galleryId,))
    car_ids = cur.fetchall()
    return jsonify(car_ids)

@controller.route('/galleryNoSaleCars/<string:galleryId>', methods=['get'])
def galleryNoSaleCars(galleryId):
    conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    sql_select_query = """select c.car_id,brand_name,model_name,uretim_yili,renk,durumu,km,yakit,vites,motor_hacmi,motor_gucu from own as o, car as c, brand as b, model as m where o.on_sale = false and c.model_id = m.model_id and c.brand_id = b.brand_id and o.car_id = c.car_id and o.gallery_id = %s"""
    cur.execute(sql_select_query, (galleryId,))
    car_ids = cur.fetchall()
    return jsonify(car_ids)    

@controller.route('/removeCarFromSale', methods=['post'])
def removeCarFromSale():
    if request.json is not None:
        carId = request.json['car_id']
    else:
        return 'car_id must be defined', 400

    print(carId)

    conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()

    try:
        sql_select_query = """DELETE FROM for_sale WHERE car_id = %s;"""
        cur.execute(sql_select_query, (carId,))


        sql_select_query = """UPDATE own set on_sale = false WHERE car_id = %s;"""
        cur.execute(sql_select_query, (carId,))
    except:
        return jsonify({"message":"bir hata olustu"})
    conn.commit()

    return jsonify({"message":"basariyla silindi"})

@controller.route('/placeCar', methods=['post'])
def placeCar():
    print(request.json)
    if request.json is not None:
        galleryId = request.json['gallery_id']
        carId = request.json['car_id']
        price = request.json['price']
    else:
        return 'gallery_id, car_id and price must be defined', 400

    print(carId)

    conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()

    try:
        sql_select_query = """UPDATE own set on_sale = true WHERE car_id = %s;"""
        cur.execute(sql_select_query, (carId,))

        for_sale_id = randint(1,999999)
        for_sale_date = str(date.today())
        print(for_sale_date)

        sql_select_query = """INSERT INTO for_sale values (%s,%s,%s,%s,%s);"""
        cur.execute(sql_select_query, (for_sale_id,carId,galleryId,price,for_sale_date,))


    except:
        return jsonify({"message":"bir hata olustu"})
    conn.commit()

    return jsonify({"message":"basariyla silindi"})
      