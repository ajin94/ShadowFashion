import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="sh@d0w", port=3306, db="shadowfashion")
    cursor = conn.cursor()
    return cursor, conn
