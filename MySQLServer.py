import mysql.connector
from decouple import config


def create_database():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host = config('DB_HOST'),
            port = config('DB_PORT', cast = int, default = 3306),
            user = config('DB_USER'),
            password = config('DB_PASSWORD')
        )

        if connection.is_connected():
            cursor = connection.cursor()
            sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(sql)
            cursor.execute("USE alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()


if __name__ == "__main__":
    create_database()
