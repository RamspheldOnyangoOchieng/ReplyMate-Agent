from flask import Blueprint, request
import os

whatsapp_webhook_blueprint = Blueprint("whatsapp_webhook", __name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@whatsapp_webhook_blueprint.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Forbidden", 403

    if request.method == "POST":
        data = request.get_json()
        print("Received message:", data)
        return "EVENT_RECEIVED", 200

    return "Method not allowed", 405
