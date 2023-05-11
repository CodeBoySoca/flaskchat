from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
socket = SocketIO(app)
csrf = CSRFProtect(app)
load_dotenv('.env')


@app.route('/')
def index():
    pass

@app.route('/chat')
def chat():
    pass

@app.route('/chatroom/<str:chatroom>')
def chatroom():
    pass

@app.route('/invitation')
def invitation():
    pass

if __name__ == '__main__':
    socket.run(app, debug=True)