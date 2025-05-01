from flask import request, jsonify
import os

def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        expected_token = os.getenv("INTERNAL_API_TOKEN")

        if not token or token != f"Bearer {expected_token}":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return wrapper
