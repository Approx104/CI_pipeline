import pymysql

# Establishing a connection to DB
try:
    conn = pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='Aa123456', db='sys')
except pymysql.err.OperationalError:
    try:
        conn = pymysql.connect(host='host.docker.internal', port=3306, user='root', passwd='Aa123456', db='sys')
    except pymysql.err.OperationalError:
        raise Exception("Can't connect to DB!")
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()
