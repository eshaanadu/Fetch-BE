from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for transactions and points balance
transactions = []
points_balance = {}

# Endpoint to add points for a payer
@app.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']
    
    # Add transaction to the transactions list
    transactions.append(data)
    
    # Update the points balance for the payer
    if payer not in points_balance:
        points_balance[payer] = 0
    points_balance[payer] += points
    
    return '', 200  # Return success status

# Endpoint to spend points
@app.route('/spend', methods=['POST'])
def spend_points():
    points_to_spend = request.get_json()['points']
    
    # Check if there are enough total points to spend
    if sum(points_balance.values()) < points_to_spend:
        return 'Not enough points', 400
    
    # Sort transactions by timestamp (oldest first)
    sorted_transactions = sorted(transactions, key=lambda x: x['timestamp'])
    spent_points = []
    
    # Deduct points from transactions in chronological order
    for transaction in sorted_transactions:
        payer = transaction['payer']
        points = min(points_to_spend, transaction['points'])  # Calculate points to deduct
        
        # Break the loop if no points are left to spend
        if points_to_spend <= 0:
            break
        
        # Deduct points if applicable
        if points > 0:
            spent_points.append({'payer': payer, 'points': -points})
            points_balance[payer] -= points
            points_to_spend -= points
    
    return jsonify(spent_points), 200  # Return the list of spent points

# Endpoint to retrieve the current balance for all payers
@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(points_balance), 200  # Return the points balance as JSON

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
