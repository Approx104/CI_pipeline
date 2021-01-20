import pymysql

# Establishing a connection to DB
try:
    conn = pymysql.connect(host='remotemysql.coms', port=3306, user='7n3ZZQTFqz', passwd='fyf4qhIdcV', db='7n3ZZQTFqz')
except pymysql.err.OperationalError:
    raise Exception("Can't connect to DB!")
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()
