import psycopg2
from psycopg2 import sql

# Define your database connection parameters
connection_params = {
    "dbname": "chinook",
    "user": "gitpod",
    "password": "JimmyJam",
    "host": "localhost",  # or your database server address
    "port": "5432"        # default PostgreSQL port
}

try:
    connection = psycopg2.connect(database="chinook", user="gitpod", password="JimmyJam")
    cursor = connection.cursor()

    # query 1 
    #cursor.execute('SELECT * FROM "Artist"')
    
    # query 2
    # cursor.execute('SELECT "Name" FROM "Artist"')

    # query 3 
    # cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

    # query 4
    # cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

    # query 5
    # cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

    # query 6
    #cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

    # query 7
    #cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])
    
    #results = cursor.fetchall()
    # results = cursor.fetchone()

    for result in results:
        print(result)

except psycopg2.Error as e:
    print("Error in database operation:", e)
    connection = None  # Ensure connection is defined even if connection attempt fails
finally:
    if connection:
        connection.close()