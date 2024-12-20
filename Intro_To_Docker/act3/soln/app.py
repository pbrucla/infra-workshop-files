# Database connection parameters
DB_HOST = 'db'  # Change this to your DB host
DB_NAME = 'workshop'  # Replace with your DB name
DB_USER = 'workshop'  # Replace with your DB user
DB_PASSWORD = 'ACMCyber'  # Replace with your DB password
DB_PORT = 5432 # Replace with DB port

# Do not edit anything below

from flask import Flask
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Route for querying the database
@app.route('/')
def db_query():
    try:
        # Establish the connection to the database
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM secrets;")
        
        # Fetch all results
        rows = cursor.fetchall()

        # Convert the rows into a string to return
        result = ""
        for row in rows:
            result += str(row) + "\n"
        
        # Close the connection
        cursor.close()
        conn.close()

        return result
    except Exception as e:
        return f"Error querying the database: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
