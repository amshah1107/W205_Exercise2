import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def displayAllrecords(cur,k,l):
   if (k > l) :
      print "The first digit should be less than the second"
      return
   cur.execute("SELECT word, count from tweetwordcount where count >= %s and count <= %s ORDER BY count DESC",(k,l))
   records = cur.fetchall()
   if len(records) == 0:
      print "No records in the database"
   else:
      for rec in records:
         print rec[0],":",rec[1] 

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

arguments = sys.argv[1:]
if len(arguments) == 2:
   k = sys.argv[1]
   l = sys.argv[2]
   displayAllrecords(cur,k,l)
else:
   print "Usage: python argv[0] k,l- displays all records with freq >= k and <= l" 


