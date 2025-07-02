from flask import Flask, request
from pythonosc.udp_client import SimpleUDPClient
from flask_cors import CORS
import os

# OSC client setup (Reaper listens on port 8000)
osc_ip = os.getenv("OSC_TARGET_IP", "127.0.0.1")
osc_port = int(os.getenv("OSC_TARGET_PORT", "8000"))
client = SimpleUDPClient(osc_ip, osc_port)

app = Flask(__name__)
CORS(app)

@app.route("/send_osc")
def send_osc():
    address = request.args.get("address")
    value = request.args.get("value", default=None)

    if address is None:
        return "Missing OSC address", 400

    if value is not None:
        try:
            value = float(value)
            client.send_message(address, value)
        except ValueError:
            client.send_message(address, value)
    else:
        client.send_message(address, [])

    print(f"Sent: {address} {value}")
    return "OSC message sent", 200

@app.route("/play")
def play():
    client.send_message("/play", [])
    return "Play triggered", 200

@app.route("/stop")
def stop():
    client.send_message("/stop", [])
    return "Stop triggered", 200

@app.route("/seek")
def seek():
    time_str = request.args.get("time")
    if time_str is None:
        return "Missing time parameter", 400
    try:
        time = float(time_str)
        client.send_message("/time", time)
        return f"Seek to {time} seconds", 200
    except ValueError:
        return "Invalid time format", 400

@app.route("/")
def index():
    return "Flask OSC Server is running."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
