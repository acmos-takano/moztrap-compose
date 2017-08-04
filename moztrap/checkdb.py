# moztrap用初期DB構築判定
import os, sys, MySQLdb

# 接続設定はコンテナ起動時の外部変数を想定
DB_NAME = "moztrap"
DB_HOST = os.getenv("MYSQL_PORT_3306_TCP_ADDR","")
DB_USER = os.getenv("MYSQL_DB_USER","root")
DB_PASS = os.getenv("MYSQL_ENV_MYSQL_ROOT_PASSWORD","000000")

conn_string = ("dbname='" + DB_NAME + "' user='" + DB_USER + "' host='" + DB_HOST + "' password='" + DB_PASS + "'")
print("Connecting to database:\n" + conn_string)

con = MySQLdb.connect( user=DB_USER, passwd=DB_PASS, host=DB_HOST, db=DB_NAME)
cur= con.cursor()

# サーチ先がこれでいいかは確認
cur.execute("select * from information_schema.tables where table_name=%s", ('django_admin_log',))
exists = bool(cur.rowcount)

if exists is False:
    print("Database does not appear to be setup.")
    sys.exit(2)
