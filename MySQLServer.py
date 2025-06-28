import mysql.connector
from decouple import config

def create_database():
    try:
        #  connect to MySQL server
        connection = mysql.connector.connect(
            host= config('HOST'),
            user = config('USER'),
            password = config('PASSWORD')
        )

        if connection.is_connected():
            cursor = connection.cursor()
            sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(sql)
            cursor.execute("USE alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
