from random import randint
import psycopg2

#change values user to user
dbname = 'otogaleri'
username = 'postgres'
hostname = 'localhost'
pwd = 'Yigit1323?'
port_id = '5432'
conn = None
cur = None

try:
    conn = psycopg2.connect(database = dbname, 
                            user = username, 
                            password = pwd, 
                            host = hostname, 
                            port = port_id)

    cur = conn.cursor()


    cur.execute('''create table if not EXISTS FOR_SALE(
        for_sale_id varchar(30) NOT NULL,
        car_id varchar(30) NOT NULL,
        gallery_id varchar(30) NOT NULL,
        price integer NOT NULL,
        for_sale_date date NOT NULL,
        primary key(for_sale_id)
    );''')


    cur.execute('''create table if not EXISTS OWN(
        car_id varchar(30) NOT NULL,
        gallery_id varchar(30) NOT NULL,
        on_sale boolean not null,
        foreign key(car_id) references CAR(car_id)
    );''')    


    cur.execute('''select car_id, gallery_id from CAR''')
    cars = cur.fetchall()
    
    for car in cars:
        onsale = False
        if (randint(1,10) <= 8):
            price = randint(100000,300000)
            id = randint(1000000,9999999)
            month = randint(1,12)
            day = randint(1,28)
            onsale = True
            cur.execute('''INSERT INTO FOR_SALE VALUES (%s, %s, %s,%s,%s);''',(id,car[0],car[1],price,f"2021-{month}-{day}"))
            pass
        cur.execute('''INSERT INTO OWN VALUES (%s, %s,%s);''',(car[0],car[1],onsale))        
    conn.commit()
    
except Exception as error:
    print(error)
    
finally:   
    if cur is not None: 
        cur.close()
    if conn is not None: 
        conn.close()
    #connection closed