from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)   # initialize flask app
app.config['SECRET'] = "secretkey"

# instantiate socketio passing in app
socketio = SocketIO(app, cors_allowed_origins="*")

# listen for 'message' event
@socketio.on('message')
def handle_message(msg):
    print("Received message: " + msg)

    if msg != "User connected!":
        send(msg, broadcast=True)

@app.route('/')         # render index html page at root '/'
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()