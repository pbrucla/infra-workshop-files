# Database connection parameters
import os

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = int(os.environ.get("DB_PORT", 5432))

from flask import Flask, request, jsonify
import psycopg2
import socket
from psycopg2 import sql

app = Flask(__name__)


# Route for querying the database
@app.route("/")
def db_query():
    try:
        # Establish the connection to the database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM secrets;")

        # Fetch all results
        rows = cursor.fetchall()

        # Convert the rows into a string to return
        result = f"running on hostname {socket.gethostname()}:\n"
        for row in rows:
            result += str(row) + "\n"

        # Close the connection
        cursor.close()
        conn.close()

        return result
    except Exception as e:
        return f"Error querying the database: {str(e)}"


# Route for adding data to the database via query parameters
@app.route("/add", methods=["GET"])
def add_data():
    try:
        # Get data from query parameters
        secret = request.args.get("secret")
        if not secret:
            return jsonify({"error": "The 'secret' query parameter is required"}), 400

        # Establish the connection to the database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        cursor = conn.cursor()

        # Insert the data into the database
        insert_query = sql.SQL("INSERT INTO secrets (secret) VALUES (%s);")
        cursor.execute(insert_query, (secret,))

        # Commit the transaction
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        return jsonify({"message": "Data added successfully"}), 201

    except Exception as e:
        return jsonify({"error": f"Error adding data to the database: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
