from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
transactions = []
points_balance = {}

@app.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']
    
    # Add transaction
    transactions.append(data)
    
    # Update balance
    if payer not in points_balance:
        points_balance[payer] = 0
    points_balance[payer] += points
    
    return '', 200  # Return success status

@app.route('/spend', methods=['POST'])
def spend_points():
    points_to_spend = request.get_json()['points']
    
    if sum(points_balance.values()) < points_to_spend:
        return 'Not enough points', 400
    
    # Sort transactions by timestamp (oldest first)
    sorted_transactions = sorted(transactions, key=lambda x: x['timestamp'])
    spent_points = []
    
    for transaction in sorted_transactions:
        payer = transaction['payer']
        points = min(points_to_spend, transaction['points'])
        
        if points_to_spend <= 0:
            break
        
        if points > 0:
            spent_points.append({'payer': payer, 'points': -points})
            points_balance[payer] -= points
            points_to_spend -= points
    
    return jsonify(spent_points), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(points_balance), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


