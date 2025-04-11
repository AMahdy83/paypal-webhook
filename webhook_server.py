from flask import Flask, request

app = Flask(__name__)

@app.route("/paypal/webhook", methods=["POST"])
def paypal_webhook():
    data = request.json
    print("📩 Webhook received:", data)
    return {"status": "received"}, 200
