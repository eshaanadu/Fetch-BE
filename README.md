# Fetch Backend API

This repository contains a simple backend API developed as part of the Fetch Backend Internship coding challenge. The API helps manage points for a user from multiple payers and includes functionality for adding, spending, and viewing the current points balance.

## Features

- **Add Points**: Add points for a specific payer with a timestamp.
- **Spend Points**: Spend points, following the rule of spending the oldest points first.
- **View Points Balance**: Retrieve the current points balance, grouped by payer.

## Endpoints

### 1. Add Points
**Route**: `/add`  
**Method**: `POST`  
**Description**: Adds points for a given payer. The request should include the payer, points to be added, and the timestamp of the transaction.

#### Example Request:
```bash
curl -X POST http://localhost:5000/add -H 'Content-Type: application/json' -d '{"payer": "DANNON", "points": 5000, "timestamp": "2022-11-01T14:00:00Z"}'
```

### 2. Spend Points
**Route**: `/spend`  
**Method**: `POST`  
**Description**: Spends points, with the rule that the oldest points are spent first. If a user does not have enough points, the request will return an error.

#### Example Request:
```bash
curl -X POST http://localhost:5000/spend -H 'Content-Type: application/json' -d '{"points": 5000}'
```

### 3. Get Points Balance
**Route**: `/balance`  
**Method**: `GET`  
**Description**: Returns the current points balance, grouped by payer.

#### Example Request:
```bash
curl http://localhost:5000/balance
```

## Running the Application

### Requirements:
- **Python 3.6+**
- **Flask**: Install Flask by running `pip install Flask`.

### Steps to Run:

1. Clone the repository:
   ```bash
   git clone https://github.com/eshaanadu/Fetch-BE.git
   ```

2. Install dependencies (Flask):
   ```bash
   pip install Flask
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Continue to your computer terminal and run your desired `curl` commands (Example requests in Endpoints section). You must only change the parts inside the curly brackets.


## Technologies Used

- **Python**: The core programming language.
- **Flask**: Lightweight web framework for building the API.
