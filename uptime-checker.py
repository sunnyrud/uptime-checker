from flask import Flask, render_template_string
import requests
import time
import threading

app = Flask(__name__)

url = "https://www.google.com"
last_status = {"status": "Unknown", "code": 0, "timestamp": ""}

# Background checker thread
def check_site():
    while True:
        try:
            response = requests.get(url)
            last_status["status"] = "UP"
            last_status["code"] = response.status_code
        except requests.exceptions.RequestException:
            last_status["status"] = "DOWN"
            last_status["code"] = 0
        last_status["timestamp"] = time.ctime()
        time.sleep(30)

# Web route
@app.route("/")
def dashboard():
    return render_template_string("""
    <h1>🌐 Uptime Monitor</h1>
    <p><strong>URL:</strong> {{ url }}</p>
    <p><strong>Status:</strong> {{ status["status"] }}</p>
    <p><strong>HTTP Code:</strong> {{ status["code"] }}</p>
    <p><strong>Last Checked:</strong> {{ status["timestamp"] }}</p>
    """, url=url, status=last_status)

# Start thread and app
if __name__ == "__main__":
    threading.Thread(target=check_site, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
