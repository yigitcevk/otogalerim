import psycopg2
from random import randint
import requests

conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

brands = requests.get('http://127.0.0.1:5000/brands').json()
models = requests.get('http://127.0.0.1:5000/models').json()

renkL = ['Siyah', 'Gri', 'Kırmızı', 'Mavi', 'Lacivert', 'Beyaz', 'Yeşil', 'Sarı']
durumL = ['2.el', 'Sıfır']
yakitL = ['Benzin', 'Dizel', 'LPG', 'Elektrik', 'Benzin & LPG']
vitesL = ['Manuel', 'Yarı Otomatik', 'Otomatik']
motor_hacmiL = [1.3, 1.4, 1.5, 1.6]

cur.execute('''create table if not EXISTS SOLD(
    sold_id varchar(30) NOT NULL,
    car_id varchar(30) NOT NULL,
    gallery_id varchar(30) NOT NULL,
    model_id varchar(30) NOT NULL,
    brand_id varchar(30) NOT NULL,
    renk varchar(30),
    km integer,
    durumu varchar(30),
    yakit varchar(30),
    vites varchar(30),
    motor_hacmi real,
    uretim_yili integer,
    motor_gucu integer,
    price integer,
    satis_tarihi date,
    puan decimal,
    primary key(sold_id)
);''')

cur.execute('''select gallery_id from Gallery''')
gallery_ids = cur.fetchall()
cur.execute('''select car_id from Car''')
car_ids = cur.fetchall()
original_car_ids = car_ids

sold_id = 0

for i in range(100):
    
    #Assigning random values for each sold cars.
    index = randint(1,len(brands) - 1)
    brand_id = brands[index]['id']
    brand_name = brands[index]['name']
    index2 = randint(0,len(models[index]) - 1)
    model_id = models[index][index2]['id']
    model_name = models[index][index2]['name']
    km = randint(10000,300000)
    durum = durumL[randint(0,len(durumL) - 1)]
    if (durum == 'Sıfır'):
        km = 0
    yakit = yakitL[randint(0,len(yakitL) - 1)]
    vites = vitesL[randint(0,len(vitesL) - 1)]
    renk = renkL[randint(0,len(renkL) - 1)]
    motor_hacmi = motor_hacmiL[randint(0,len(motor_hacmiL) - 1)]
    motor_gucu = randint(50,600)
    uretim_yili = randint(1980,2022)
    gallery_id = gallery_ids[randint(0,len(gallery_ids) - 1)]
    month = randint(1,12)
    day = randint(1,28)
    price = randint(100000,300000)
    puan = randint(1,5)    
    sold_id = sold_id + 1
    car_id = randint(0,pow(10,9))
    
    #Preventing to use same car_id for more than one car.
    element_exist = car_id in car_ids
    while element_exist:
        car_id = randint(0,pow(10,9))
        element_exist = car_id in car_ids
    car_ids.append(car_id)
    
    
    cur.execute('''INSERT INTO SOLD VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',
                (sold_id,car_id,gallery_id,model_id, brand_id, renk, km, durum, yakit, vites, motor_hacmi, uretim_yili, motor_gucu, price,f"2021-{month}-{day}",puan))
    
    #Updating rating and total_sales values of related Gallery.
    cur.execute('''select gallery_rating from Gallery where gallery_id = %s''',(gallery_id))
    temp_gallery_rating = cur.fetchall()[0][0]
    cur.execute('''select total_sales from Gallery where gallery_id = %s''',(gallery_id))
    temp_total_sales = cur.fetchall()[0][0]
    new_gallery_rating = (temp_gallery_rating*temp_total_sales + puan)/(temp_total_sales+1)
    
    cur.execute('''UPDATE GALLERY SET  gallery_rating = %s WHERE gallery_id = %s;''',
                (new_gallery_rating,gallery_id))
    cur.execute('''UPDATE GALLERY SET  total_sales =  total_sales + 1 WHERE gallery_id = %s;''',
                (gallery_id))
    
conn.commit()
conn.close()
