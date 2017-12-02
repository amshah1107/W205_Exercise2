import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount order by count desc limit 20");  
records = cur.fetchall()
for rec in records:
    print rec[0],":",rec[1] 

