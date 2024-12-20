from flask import Flask
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Database connection parameters
DB_HOST = 'localhost'  # Change this to your DB host
DB_NAME = 'your_db_name'  # Replace with your DB name
DB_USER = 'your_db_user'  # Replace with your DB user
DB_PASSWORD = 'your_db_password'  # Replace with your DB password

# Route for "hello, world"
@app.route('/')
def hello():
    return 'Hello, World!'

# Route for querying the database
@app.route('/db')
def db_query():
    try:
        # Establish the connection to the database
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
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
    app.run(debug=True)
