import psycopg2
from psycopg2.extras import RealDictCursor


try:
    db_info = {
            "host":"localhost",
            "database":"fastapi_test_db",
            "user":"fastapi_test_user",
            "password":"fastapi_test_password",
            "cursor_factory":RealDictCursor
            }
    conn = psycopg2.connect(**db_info)
 
except:
    print("I am unable to connect to the database") 

cur = conn.cursor()
try:
    cur.execute("CREATE TABLE posts (id serial PRIMARY KEY, content varchar, title varchar not null, published boolean default True);")
except:
    print("I can't drop our test database!")

conn.commit() # <--- makes sure the change is shown in the database
conn.close()
cur.close()
