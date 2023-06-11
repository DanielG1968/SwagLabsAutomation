import requests

# Set the base URL for the API endpoint
base_url = 'https://www.saucedemo.com'

# Set the login endpoint
login_endpoint = '/do_login'

# Set the login credentials
username = 'standard_user'
password = 'secret_sauce'

# Create a session to maintain cookies
session = requests.Session()

# Send a POST request to the login endpoint with the credentials
login_url = base_url + login_endpoint
login_data = {
    'username': username,
    'password': password
}
response = session.post(login_url, data=login_data)

# Verify the response status code
if response.status_code == 200:
    print("API test passed - Response status code: 200 OK")
else:
    print("API test failed - Response status code:", response.status_code)

# Verify the response data
expected_message = "Products"
if expected_message in response.text:
    print("API test passed - Expected message found in the response")
else:
    print("API test failed - Expected message not found in the response")

# Additional verification can be performed based on the API response
# such as checking specific data, headers, cookies, etc.

# Example: Checking if the session cookie was set
if 'session-identifier' in session.cookies:
    print("API test passed - Session cookie was set")
else:
    print("API test failed - Session cookie was not set")
