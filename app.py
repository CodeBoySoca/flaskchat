from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
import os
import datetime
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socket = SocketIO(app)
csrf = CSRFProtect(app)
load_dotenv('.env')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        chatroom = request.form.get('chatroom')
        image = request.form.get('photo')
        email = request.form.get('email')
        user = User(username=username, email=email, chatroom=Generator.generate_chatroom_id(chatroom), image=f'/static/images/{image}')
        user.save()

    return render_template('index.html')

@app.route('/chat')
def chat():
    pass

# @socket.on('connect')
# def connected(data):
#     print('connected with websocket')

# @socket.on('user_join')
# def get_data(data):
#     print(f"chatroom data: {data}")

# @app.route('/chatroom')
# def chatroom():
#     return render_template('chatroom.html')

@app.route('/invitation')
def invitation():
    return render_template('email_invitation.html', chat={'chatroom_id' : '78364243', 'username' : 'amy-90653452'})

if __name__ == '__main__':
    socket.run(app, debug=True)