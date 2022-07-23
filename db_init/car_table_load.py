from random import randint
import psycopg2
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
# motor_gucuL = [50-600]
# kmL=[10000-1000000]

for brand in brands:
    print(brand)

for model in models:
    print(model)

cur.execute('''create table if not EXISTS CAR(
    car_id varchar(30) NOT NULL,
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
    primary key(car_id),
    foreign key(model_id) references MODEL(model_id),
    foreign key(brand_id) references BRAND(brand_id)
);''')

car_id = 0

for _ in range(1000):
    index = randint(1,len(brands) - 1)
    brand_id = brands[index]['id']
    brand_name = brands[index]['name']
    index2 = randint(0,len(models[index]) - 1)
    model_id = models[index][index2]['id']
    model_name = models[index][index2]['name']

    km = randint(0,3000000)
    durum = durumL[randint(0,len(durumL) - 1)]
    if (durum == 'Sıfır'):
        km = 0
    yakit = yakitL[randint(0,len(yakitL) - 1)]
    vites = vitesL[randint(0,len(vitesL) - 1)]
    renk = renkL[randint(0,len(renkL) - 1)]
    motor_hacmi = motor_hacmiL[randint(0,len(motor_hacmiL) - 1)]
    motor_gucu = randint(50,600)
    car_id = car_id + 1
    uretim_yili = randint(1980,2022)

    cur.execute('''insert into car values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',(car_id,model_id,brand_id,renk,km,durum,yakit,vites,motor_hacmi,uretim_yili,motor_gucu))
    print(brand_name,model_name,motor_hacmi,motor_gucu,durum,km,yakit,vites)

conn.commit()
conn.close()