from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv

app = Flask(__name__)
socket = SocketIO(app)
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

if __name__ == '__main__':
    socket.run(app, debug=True)