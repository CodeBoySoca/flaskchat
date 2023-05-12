from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
import os
import datetime
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
socket = SocketIO(app)
csrf = CSRFProtect(app)
load_dotenv('.env')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        chatroom = request.form.get('chatroom')
        image = request.files['photo']
        email = request.form.get('email')
        chatroom_id=chatroom=Generator.generate_chatroom_id(chatroom).lower()
        path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(path)
        user = User(username=username, email=email, chatroom=chatroom_id, image=image.filename)
        user.save()
        return redirect(url_for('chatroom', chatroom_id=chatroom_id))
    return render_template('index.html')



# @socket.on('disconnect')
# def disconnect(data):
#     ''' Save chat history '''


@app.route('/chatroom/<chatroom_id>')
def chatroom(chatroom_id):
    data = User.objects(chatroom=chatroom_id)
    return render_template('chatroom.html', data=data)

@app.route('/chat')
def chat():
    pass

# @socket.on('connect')
# def connected(data):
#     print('connected with websocket')

# @socket.on('user_join')
# def get_data(data):
#     print(f"chatroom data: {data}")


@app.route('/invitation')
def invitation():
    return render_template('email_invitation.html', chat={'chatroom_id' : '78364243', 'username' : 'amy-90653452'})

if __name__ == '__main__':
    socket.run(app, debug=True)