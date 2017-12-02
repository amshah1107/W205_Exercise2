import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def displayOneRecord(searchStr, cur):
   cur.execute("SELECT word, count from tweetwordcount where word = %s", (searchStr,))
   records = cur.fetchall()
   if len(records) == 0:
      print "The string {} does not exists in the tcount database".format(searchStr)
   else:
      for rec in records:
         print "Total number of occurances of {} :{} ".format(searchStr,rec[1])  
def displayAllrecords(cur):
   cur.execute("SELECT word, count from tweetwordcount")
   records = cur.fetchall()
   records = sorted(records)
   if len(records) == 0:
      print "No records in the database"
   else:
      for rec in records:
         print rec[0],":",rec[1] 

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

arguments = sys.argv[1:]
if len(arguments) == 0:
   displayAllrecords(cur)
elif len(arguments) == 1:
   searchStr = sys.argv[1]
   displayOneRecord(searchStr,cur)
else:
   print "Usage: python argv[0] - for all the words"
   print "       python argv[0] searchString - to search a single string"


