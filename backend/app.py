from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Cloud Computing Project",
        "status": "Backend Running Successfully",
        "technology": "Docker Compose"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "database"),
            database=os.getenv("DB_NAME", "cloud_db"),
            user=os.getenv("DB_USER", "cloud_user"),
            password=os.getenv("DB_PASSWORD"),
            connect_timeout=5
        )
        conn.close()
        return jsonify({"database": "Connected Successfully"})
    except Exception as e:
        return jsonify({"database": "Connection Failed", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
