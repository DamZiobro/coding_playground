#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid
import traceback

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER", 'smtp.gmail.com')
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

recipient = os.getenv("RECIPIENT_MAIL")


@app.route("/")
def index():
    """Root endpoint."""
    request_id = uuid.uuid4()

    msg = Message(
        'Hello from the other side! request_id: {request_id}',
        sender=app.config['MAIL_USERNAME'],
        recipients=[recipient]
    )
    msg.body = "Hey Damian, sending you this email from my Flask app."

    try:
        mail.send(msg)
    except Exception as exc:
        message = "ERROR: Failed to send request change email for request_id: "\
            f"{request_id}. Reason: {exc}"
        print(message)
        traceback.print_exc()
        return {
            "error": ["failed_to_send_email"],
            "reason": message
        }, 503
    return "Message sent!"


if __name__ == '__main__':
    app.run(debug=True, port=8888)
