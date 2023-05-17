from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
import os
import datetime
from models import *
from twilio.rest import Client


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
app.config['SESSION_PERMANENT'] =os.getenv('SESSION_PERMANENT')
app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE')
socket = SocketIO(app)
Session(app)
CORS(app, support_credentials=True)
load_dotenv('.env')


@app.route('/', methods=['GET', 'POST'])
@cross_origin(support_credentials=True)
def index():
    session['username'] = request.form.get('username')
    chatroom = request.form.get('chatroom')

    #email = request.form.get('email')
    if request.method == 'POST':
        if chat := User.objects.filter(chat=[{'chatroom_id' : chatroom}]): 
            return redirect(url_for('chatroom', chatroom_id=chat['chatroom']))  
        chatroom_id=chatroom=Generator.generate_chatroom_id(chatroom).lower()
        image = request.files['photo']
        path= os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(path)
        role = 'creator'
        #user = User(username=session['username'], chat={chatroom_id : chatroom_id}, image=image.filename)
        user = User(**{
                    'username' : session['username'],  
                    'chat' : [{'chatroom_id' : chatroom_id}],
                    'image' : image.filename,
                    'role' : role
                })
        user.save()
        return redirect(url_for('chatroom', chatroom_id=chatroom_id))
    return render_template('index.html')

@app.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('index'))

# @socket.on('disconnect')
# def disconnect(data):
#     ''' Save chat history '''


@app.route('/chatroom/<chatroom_id>')
@cross_origin(support_credentials=True)
def chatroom(chatroom_id):
    data = User.objects(chatroom=chatroom_id)
    try: 
       return render_template('chatroom.html')
    except AttributeError: 
        return render_template('chatroom.html', data=data, username=session['username'])


@app.route('/chat')
def chat():
    pass


@app.route('/invite/<chatname>', methods=['GET', 'POST'])
@cross_origin(support_credentials=True)
def chat_invite(chatname):
    mobile = request.get_json('mobile_number')
    if chat := User.objects.get(chatroom=chatname):
        sms_from=os.getenv('TWILIO_FROM')
        twilio_client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        url = os.getenv('SITE_URL')
        SendSMS.send_chatname(
            chatname,
            twilio_client,
            sms_from,
            url,
            chat.username,
            f"+{mobile['mobile_number']}"
         )
        return "", 200
    else:
        return render_template('chatroom.html')

    

# @socket.on('connect')
# def connected(data):
#     print('connected with websocket')

@socket.on('user_join')
def get_data(data):
    print(f"chatroom data: {data}")


@app.route('/invitation')
def invitation():
    return render_template('email_invitation.html', chat={'chatroom_id' : '78364243', 'username' : 'amy-90653452'})

if __name__ == '__main__':
    socket.run(app, debug=True)