###############################################################################
# Connection to Relational python -
###############################################################################

import MySQLdb
import pymssql
import psycopg2

# Microsoft sql
# import pymssql

conn = pymssql.connect(server='server', user='user', password='password', database='db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(MemberID) as count FROM Members WHERE id = 1")
row = cursor.fetchone()

conn.close()

print(row)

# Postgres
# import psycopg2

conn = psycopg2.connect(database='db', user='user', password='pw', host='host', port="5432")
cursor = conn.cursor()

cursor.execute('SELECT COUNT(MemberID) as count FROM Members WHERE id = 1')
row = cursor.fetchone()

conn.close()

print(row)

# mysql
# import MySQLdb

conn = MySQLdb.connect(host='host', user='user', passwd='passwd', db='db')
cursor = conn.cursor()

cursor.execute('SELECT COUNT(MemberID) as count FROM Members WHERE id = 1')
row = cursor.fetchone()

conn.close()

print(row)



