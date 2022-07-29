import psycopg2
conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")
cur = conn.cursor()