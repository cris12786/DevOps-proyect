from flask import Blueprint, Response
from app.db import get_connection
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

main = Blueprint("main", __name__)

REQUEST_COUNT = Counter('request_count', 'Total requests')

@main.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@main.route("/")
def home():
    REQUEST_COUNT.inc()
    return "App funcionando 🚀"

@main.route("/db")
def db_test():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"DB conectada: {db_version}"
