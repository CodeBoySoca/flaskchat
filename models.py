import redis
import datetime
import uuid
import smtplib
import string
import secrets
from datetime import datetime
from twilio.rest import Client
from mongoengine import *


connect('flaskchat')

class Chat(Document):
    pass

class User(Document):
    username = StringField(required=True)
    email = EmailField(required=True)
    chatroom = StringField(required=True)
    image = StringField()
    role = StringField()

class Messages():
    pass

class Generator:
    def generate_chatroom_id(chatroom_id):
        return f"{chatroom_id}-{''.join([secrets.choice(string.digits) for _ in range(8)]) }"


    