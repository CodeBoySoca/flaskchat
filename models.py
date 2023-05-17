import redis
import datetime
import uuid
import string
import secrets
import os
from dotenv import load_dotenv
import datetime
from twilio.rest import Client
from mongoengine import *
from email.message import EmailMessage

load_dotenv('.env')
connect('flaskchat')

class Messages(EmbeddedDocument):
    sender = StringField(required=True)
    message = StringField()
    message_date = DateTimeField(default=datetime.datetime.utcnow)

class Chat(EmbeddedDocument):
    chatroom_id = StringField(required=True)
    creation_date = DateTimeField(default=datetime.datetime.utcnow)
    message = ListField(EmbeddedDocumentField(Messages))

class User(Document):
    username = StringField(required=True, unique=True)
    chat = ListField(EmbeddedDocumentField(Chat))
    creation_date = DateTimeField(default=datetime.datetime.utcnow)
    image = StringField()
    role = StringField()


class Generator:
    def generate_chatroom_id(chatroom_id):
        return f"{chatroom_id}-{''.join([secrets.choice(string.digits) for _ in range(8)]) }"

class SendSMS:
    def send_chatname(chatname, client, sms_from, url, username,  mobile):
        client.messages.create(
            body=f'Hello from FlaskChat 👋. You\'re invited to join {username} in there chatroom. Go to {url} and enter {chatname} as the name of the chat.',
            from_=sms_from,
            to=mobile
        ) 

    