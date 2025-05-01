import requests
import os

webhook_url = f"{os.getenv('APP_URL')}/whatsapp/webhook"
access_token = os.getenv("WHATSAPP_TOKEN")

payload = {
    "object": "whatsapp_business_account",
    "callback_url": webhook_url,
    "verify_token": os.getenv("VERIFY_TOKEN")
}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

res = requests.post("https://graph.facebook.com/v17.0/me/subscriptions", json=payload, headers=headers)
print("Webhook Setup Response:", res.status_code, res.json())
