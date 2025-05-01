from flask import Flask, request
from app.config import Config
from app.api.whatsapp.webhook import handle_webhook
from app.utils.logger import get_logger

app = Flask(__name__)
app.config.from_object(Config)
logger = get_logger()

@app.route('/whatsapp/webhook', methods=['GET', 'POST'])
def whatsapp_webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == Config.VERIFY_TOKEN:
            logger.info("Webhook verified successfully.")
            return challenge, 200
        else:
            logger.warning("Webhook verification failed.")
            return 'Verification failed', 403

    if request.method == 'POST':
        return handle_webhook(request)

if __name__ == '__main__':
    app.run(port=5000)
