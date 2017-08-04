import os, sys, MySQLdb

DB_NAME = "moztrap"
#DB_HOST = os.getenv("MYSQL_PORT_3306_TCP_ADDR",mysql)
DB_HOST = os.getenv("MYSQL_HOST","")
DB_USER = os.getenv("MYSQL_DB_USER","root")
DB_PASS = os.getenv("MYSQL_ENV_MYSQL_PASS","000000")

conn_string = ("dbname='" + DB_NAME + "' user='" + DB_USER + "' host='" + DB_HOST + "' password='" + DB_PASS + "'")
print("Connecting to database:\n" + conn_string)

try:
  con = MySQLdb.connect( user=DB_USER, passwd=DB_PASS, host=DB_HOST, db=DB_NAME)
  cur= con.cursor()
  cur.execute("select * from information_schema.tables where table_name=%s", ('django_admin_log',))
  exists = bool(cur.rowcount)
  if exists is False:
      print("Table does not appear to be setup.")
      sys.exit(2)
except Exception as e:
    print("Database does not appear to be setup.")
    sys.exit(2)
finally:
    cur.close()
    con.close()
