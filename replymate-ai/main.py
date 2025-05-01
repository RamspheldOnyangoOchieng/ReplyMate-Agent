from flask import Flask
from app.api.whatsapp.webhook import whatsapp_webhook_blueprint
from app.api.whatsapp.send_message import send_message_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(whatsapp_webhook_blueprint, url_prefix="/whatsapp")
app.register_blueprint(send_message_blueprint, url_prefix="/send")

@app.route('/')
def index():
    return "ReplyMate AI is running 🚀", 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)
