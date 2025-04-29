import json
import os
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

def lambda_handler(event, context):
    try:
        # Just a basic connection test
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1;')
        result = cur.fetchone()
        
        cur.close()
        conn.close()
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Database connected successfully!", "db_response": result}),
            "headers": {"Content-Type": "application/json"}
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }