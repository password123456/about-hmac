_author__ = 'https://github.com/password123456/'
__date__ = '2024.03.29'
__version__ = '1.0.0'
__status__ = 'Production'

import requests
import hashlib
from datetime import datetime

# Set your secret key for HMAC hashing.
SECRET_KEY = 'your_secret_key'


# Function to send the request to the server.
def send_hmac_request():
    # Get the current UTC time as a UNIX timestamp.
    current_request_utc_unix_timestamp = int(datetime.utcnow().timestamp())

    # Define the request URI.
    request_uri = '/example/users?user=test&institutionID=999&signature=7e745d74b69b7f62e8e2'

    # Prepare the data for HMAC calculation.
    data_to_hash = request_uri + str(current_request_utc_unix_timestamp) + SECRET_KEY

    # Calculate the HMAC hash.
    x_request_hmac = hashlib.sha256(data_to_hash.encode()).hexdigest()

    # Set the request headers.
    headers = {
        'X-Authorization-Content-HMAC': x_request_hmac,  # Include the HMAC hash in the request header.
        'X-Authorization-Timestamp': str(current_request_utc_unix_timestamp)  # Include the current timestamp in the request header.
    }

    # Send a GET request to the server.
    response = requests.get(f'http://127.0.0.1:5000{request_uri}', headers=headers)

    # Print the HTTP status code of the response.
    print('HTTP', response.status_code)

    # Print the response headers.
    for key, value in response.headers.items():
        print(f'{key}: {value}')
    print('\n')

    # Print the response body.
    print(response.text)

    # Get the timestamp and HMAC from the response headers.
    x_response_timestamp = response.headers.get('X-Response-Content-TimeStamp')
    x_response_hmac = response.headers.get('X-Response-Content-HMAC')

    # Get the current UTC time.
    current_utc_unix_timestamp = int(datetime.utcnow().timestamp())

    # Format the timestamps for display.
    datetime_x_response_timestamp = datetime.fromtimestamp(int(x_response_timestamp)).strftime("%Y-%m-%dT%H:%M:%S")
    current_datetime = datetime.fromtimestamp(int(current_utc_unix_timestamp)).strftime("%Y-%m-%dT%H:%M:%S")

    # Prepare the data for HMAC calculation.
    response_hmac_data = f'{x_response_timestamp}|{response.text}'
    response_data_hash = hashlib.sha256(response_hmac_data.encode() + SECRET_KEY.encode()).hexdigest()

    # Calculate the time difference between the response timestamp and the current time.
    time_difference = abs(int(current_utc_unix_timestamp) - int(x_response_timestamp))

    # Verify the HMAC and print the results.
    if response_data_hash == x_response_hmac:
        print('Server response HMAC verification successful')
        print('--------------')
        print(f'Response timestamp: {datetime_x_response_timestamp}')
        print(f'Current time: {current_datetime}')
        print(f'Time difference: {time_difference}')
    else:
        print("HMAC verification failed")


if __name__ == '__main__':
    send_hmac_request()
