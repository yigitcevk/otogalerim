from random import randint
import psycopg2
import trnamegen as trn

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

    #connection established
    
    cur = conn.cursor()
    
    gallery_names = []
    names = []
    for i in range(30):
        names.append(trn.firstName())
        gallery_names.append(names[i] + "Galeri")
    
    cur.execute('''CREATE TABLE IF NOT EXISTS gallery(
    gallery_id varchar(30) NOT NULL,
    gallery_name varchar(30) NOT NULL,
    city_name varchar(30),
    email varchar(30) NOT NULL,
    district_name varchar(30),
    gallery_rating real,
    telephone_number varchar(30),
    total_sales integer,
    primary key(gallery_id)
    );''')
    
    city_index = 0
    district_index = 0
    district_arr1 = ["Çankaya", "Keçiören", "Polatlı"]
    district_arr2 = ["Kadıköy", "Beşiktaş", "Etiler"]
    district_arr3 = ["Karşıyaka", "Güzelyalı", "Bostanlı"]
    for i in range(30):
        gallery_id = gallery_names[i]
        gallery_name = gallery_names[i]
        
        city_name = ""
        district_name = ""
        if(city_index == 3):
            city_index = 0
        if(city_index == 0):
            city_name = 'Ankara'
            district_name = district_arr1[randint(0,2)]
        if(city_index == 1):
            city_name = 'İstanbul'
            district_name = district_arr2[randint(0,2)]
        if(city_index == 2):
            city_name = 'İzmir'
            district_name = district_arr3[randint(0,2)]

        email = gallery_name + "@gmail.com"
        gallery_rating = 0
        telephone_number = "+90" + str(randint(500, 599)) + str(randint(0000000, 9999999))
        total_sales = 0       
        
        cur.execute('''INSERT INTO gallery VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''',
                    (gallery_id, gallery_name, city_name, email, district_name, gallery_rating, telephone_number, total_sales))
        print(gallery_id, gallery_name, city_name, email, district_name, gallery_rating, telephone_number, total_sales)
        city_index += 1
        
    conn.commit()
    
except Exception as error:
    print(error)
    
finally:   
    if cur is not None: 
        cur.close()
    if conn is not None: 
        conn.close()
    #connection closed