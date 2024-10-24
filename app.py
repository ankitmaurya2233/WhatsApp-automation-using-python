from flask import Flask, request, jsonify
from utils.send_message import send_message, send_image
from utils.schedule_jobs import schedule_message
from utils.auto_reply import auto_reply

app = Flask(__name__)

# Route to send a message immediately
@app.route('/send-message', methods=['POST'])
def send_message_route():
    data = request.json
    phone_no = data['phone_no']
    message = data['message']
    send_message(phone_no, message)
    return jsonify({"status": "Message sent successfully"})


# Route to schedule a message
@app.route('/schedule-message', methods=['POST'])
def schedule_message_route():
    data = request.json
    phone_no = data['phone_no']
    message = data['message']
    time_hour = data['time_hour']
    time_minute = data['time_minute']
    schedule_message(phone_no, message, time_hour, time_minute)
    return jsonify({"status": "Message scheduled successfully"})


# Auto-reply feature route (runs in background)
@app.route('/start-auto-reply', methods=['POST'])
def start_auto_reply_route():
    auto_reply()
    return jsonify({"status": "Auto-reply started"})

if __name__ == "__main__":
    app.run(debug=True)
