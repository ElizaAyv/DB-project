import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Database configuration
DB_NAME = "scientific_conferences"
DB_USER = "postgres" 
DB_PASSWORD = "89793238" 
DB_HOST = "localhost"  
DB_PORT = 5432 

try:
    connection = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()

    cursor.execute(f"CREATE DATABASE {DB_NAME} OWNER {DB_USER};")
    print(f"Database '{DB_NAME}' created successfully!")

    cursor.close()
    connection.close()

except Exception as e:
    print("An error occurred:", e)
