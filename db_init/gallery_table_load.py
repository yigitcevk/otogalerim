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

    #connection established
    
    cur = conn.cursor()
    
    conn.commit()
    
except Exception as error:
    print(error)
    
finally:   
    if cur is not None: 
        cur.close()
    if conn is not None: 
        conn.close()
    #connection closed