from flask import Blueprint, request, jsonify
from app.services.ai_reply_engine import generate_ai_reply
from app.api.whatsapp.send_message import send_message
from app.utils.logger import get_logger

whatsapp_webhook_blueprint = Blueprint("whatsapp_webhook", __name__)
logger = get_logger()

@whatsapp_webhook_blueprint.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.get_json()
    logger.info(f"Incoming webhook data: {data}")

    try:
        for entry in data.get('entry', []):
            for change in entry.get('changes', []):
                value = change['value']
                messages = value.get('messages')
                if messages:
                    msg = messages[0]
                    sender = msg['from']
                    text = msg['text']['body']

                    # Generate AI response
                    reply = generate_ai_reply(text)
                    
                    
                    send_message(to=sender, message=reply)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        logger.error(f"Error in webhook: {str(e)}")
        return jsonify({"error": "webhook processing failed"}), 500
