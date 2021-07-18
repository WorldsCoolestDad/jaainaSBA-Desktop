import mysql.connector


def connect_to_db():
    return mysql.connector.connect(
        host="192.168.1.251",
        user="root",
        passwd="Rams2022!",
        database="jaainasba"
    )
