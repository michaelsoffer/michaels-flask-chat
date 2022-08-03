from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)   # initialize flask app
# app.config['SECRET'] = "secretkey"

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message') # socketio event handler on 'message', function will print message essentially
def handle_message(msg):
    print("Received message: " + msg)

    if msg != "User connected!":
        send(msg, broadcast=True)


@app.route('/')         # render index html page at root '/'
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()