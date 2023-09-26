from django.test import TestCase
from rest_framework.test import RequestsClient
client = RequestsClient()

# TestCase for Account Registration Successfully
response = client.post('http://127.0.0.1:8000/polls/createuser', {
    "name":"john smith",
    "email":"josmth253@gmail.com",
    "password": "smith754"})
print("Test Case 1",response)
assert response.status_code == 200

# TestCase for Invalid Email
response = client.post('http://127.0.0.1:8000/polls/createuser', {
    "name":"john",
    "email":"john23gmailcom",
    "password": "smith754"})
print("Test Case 2",response)
assert response.status_code == 200

# TestCase for Already Existing User
response = client.post('http://127.0.0.1:8000/polls/createuser', {
    "name":"john",
    "email":"john23@gmail.com",
    "password": "smith754"})
print("Test Case 3",response)
assert response.status_code == 200

# TestCase for Leaving any Blank Input
response = client.post('http://127.0.0.1:8000/polls/createuser', {
    "email":"john23@gmail.com",
    "password": "smith754"})
print("Test Case 4",response)
assert response.status_code == 200

# TestCase for Login with invalid credentials
response = client.post('http://127.0.0.1:8000/polls/signinuser', {
    "email":"joshr377@gmail.com",
    "password": "smith754"})
print("Test Case 5",response)
assert response.status_code == 200

# TestCase for Login with Valid credentials
response = client.post('http://127.0.0.1:8000/polls/signinuser', {
    "email":"john23@gmail.com",
    "password": "smith754"})
print("Test Case 6",response)
assert response.status_code == 200

# TestCase for Get all Users
response = client.get('http://127.0.0.1:8000/polls/getuser')
print("Test Case 7",response.status_code)
assert response.status_code == 200

# TestCase for Get user for specific ID
response = client.get('http://127.0.0.1:8000/polls/getuser/2')
print("Test Case 8",response.status_code)
assert response.status_code == 200

