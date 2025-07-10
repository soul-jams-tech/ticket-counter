from flask import Flask, request, jsonify
from shared_state import update_count, get_count

app = Flask(__name__)
DISTRICT_SECRET = "souljams123"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('x-district-secret') != DISTRICT_SECRET:
        return jsonify({'error': 'unauthorized'}), 403

    payload = request.json.get("sale_notification", {})
    new_tickets = int(payload.get("ticket_count", 1))
    update_count(new_tickets)
    return jsonify({'status': 'ok'}), 200

@app.route('/count', methods=['GET'])
def count():
    return jsonify({'count': get_count()})
