import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def get_password():
    return 'dummy'


connection = {
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database'],
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password']
}


def get_connection():
    try:
        conn = mysql.connector.connect(**connection)
        if conn.is_connected():
            print("Connection established successfully")
            return conn

    except Error as e:
        print(e)


def getQuery(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    row_addbook = cursor.fetchone()
    print(row_addbook)
    return row_addbook






