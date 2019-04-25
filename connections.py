import MySQLdb


def get_connection():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="password", port=3306, db="shadowfashion")
    cursor = conn.cursor()
    return cursor, conn

