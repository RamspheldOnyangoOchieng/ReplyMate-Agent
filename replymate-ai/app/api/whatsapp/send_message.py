from flask import Blueprint, request, jsonify
import requests
import os

send_message_blueprint = Blueprint('send_message', __name__)

@send_message_blueprint.route('/', methods=['POST'])
def send_message():
    data = request.json
    to = data.get("to")
    message = data.get("message")

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": message},
        "type": "text"
    }

    headers = {
        "Authorization": f"Bearer {os.getenv('WHATSAPP_TOKEN')}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        os.getenv("WHATSAPP_API_URL"),
        json=payload,
        headers=headers
    )

    return jsonify(response.json()), response.status_code
# This code defines a Flask blueprint for sending messages via WhatsApp using the WhatsApp Business API.