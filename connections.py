import MySQLdb


def Connection():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", port=3306, db="shadowfashion")
    cursor = conn.cursor()

    return cursor, conn
