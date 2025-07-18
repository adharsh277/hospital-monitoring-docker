from flask import Flask, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# 🔢 Define Prometheus metrics
request_counter = Counter('request_count', 'Total number of HTTP requests')
patient_admissions = Counter('patient_admissions_total', 'Total patient admissions')
icu_alerts = Counter('icu_alerts_total', 'Total ICU alerts triggered')
db_queries = Counter('db_queries_total', 'Total number of database queries')

# 🏠 Home route
@app.route("/")
def home():
    request_counter.inc()
    return "🏥 Hospital Monitoring Flask App is running!"

# 🚨 ICU alert route (example)
@app.route("/icu-alert", methods=["POST"])
def icu_alert():
    icu_alerts.inc()
    return "🚨 ICU Alert triggered!", 200

# 🛏️ Admit patient route (example)
@app.route("/admit", methods=["POST"])
def admit_patient():
    patient_admissions.inc()
    return "✅ Patient admitted", 200

# 🔍 Simulate DB query route (example)
@app.route("/query-db", methods=["GET"])
def query_db():
    db_queries.inc()
    return "📄 DB queried", 200

# 📈 Metrics endpoint for Prometheus scraping
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# 🚀 Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
