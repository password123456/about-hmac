_author__ = 'https://github.com/password123456/'
__date__ = '2024.03.29'
__version__ = '1.0.0'
__status__ = 'Production'

from flask import Flask, request, jsonify, make_response
import hashlib
from datetime import datetime
import json

app = Flask(__name__)

# Set your secret key for HMAC hashing.
SECRET_KEY = 'your_secret_key'


# Endpoint to handle example requests.
@app.route('/example/users', methods=['GET'])
def handle_request():
    # Get X-Request-HMAC and X-Request-TimeStamp from the client request headers.
    request_hmac = request.headers.get('X-Authorization-Content-HMAC')
    request_timestamp = request.headers.get('X-Authorization-Timestamp')

    # Get the request URI and query string.
    request_uri = request.path
    query_string = request.query_string.decode()

    # Create the full URI.
    full_uri = request_uri + '?' + query_string

    # Prepare the data for HMAC calculation.
    data_to_hash = full_uri + str(int(datetime.utcnow().timestamp())) + SECRET_KEY

    # Calculate the HMAC hash.
    hmac = hashlib.sha256(data_to_hash.encode()).hexdigest()

    # Check time difference (within 5 minutes).
    time_difference = abs(int(str(int(datetime.utcnow().timestamp()))) - int(request_timestamp))
    time_threshold = 300  # 5 minutes in seconds

    if request_hmac == hmac and time_difference <= time_threshold:
        # If the client request is valid, return response data.
        # If response is response_data
        response_data = {"result": "ok", "users": "test", "sub": 2840345654}
        response_data_json = json.dumps(response_data)
        response = make_response(response_data_json, 200)

        # Get the current timestamp.
        response_data_timestamp = str(int(datetime.utcnow().timestamp()))

        # Prepare data for HMAC calculation (response timestamp + response data).
        hmac_data = f'{response_data_timestamp}|{response_data_json}'

        # Calculate HMAC.
        response_hmac = hashlib.sha256(hmac_data.encode() + SECRET_KEY.encode()).hexdigest()

        print(hmac_data)
        print(response_hmac)

        # Add X-Response-HMAC header.
        response.headers['X-Response-Content-HMAC'] = response_hmac
        # Add X-Response-TimeStamp header.
        response.headers['X-Response-Content-TimeStamp'] = response_data_timestamp

        return response
    else:
        # If the client request is invalid, return an error response.
        return jsonify({"error": "Invalid request or timestamp"}), 400


if __name__ == '__main__':
    app.run(debug=True)
