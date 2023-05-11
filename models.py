import redis
import datetime
import uuid
import smtplib
from datetime import datetime
from twilio.rest import Client
from mongoengine import *

connect('history')

class Chat(Document):
    pass

class User(Document):
    pass

class Messages():
    pass

