from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socket = SocketIO(app)
csrf = CSRFProtect(app)
load_dotenv('.env')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    pass

@app.route('/chatroom/<chatroom>')
def chatroom():
    pass

@app.route('/invitation')
def invitation():
    return render_template('email_invitation.html', chat={'chatroom_id' : '78364243', 'username' : 'amy-90653452'})

if __name__ == '__main__':
    socket.run(app, debug=True)