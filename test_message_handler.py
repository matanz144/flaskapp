import requests
from pprint import pprint
import json

URL = " http://flaskapiapp1.herokuapp.com/"

# Const names of functions
WRITE_MESSAGE = "writeMessage"
GET_ALL_MESSAGES = "getAllMessages"
GET_UNREAD_MESSAGES = "getUnreadMessages"
READ_MESSAGE = "readMessage"
DELETE_MESSAGE = "deleteMessage"

"""
Examples of messages,
The message have to be in string type to be able pass it to the server.
You can pass one message or list of them.
"""

# One messages example
msg = json.dumps(
    {'sender_id': 13, 'receiver_id': 12, 'message_id': 15, 'subject': 'test message6', 'context': 'some text6'})

# List of messages example
msgs = [
    {'sender_id': 1, 'receiver_id': 2, 'message_id': 10, 'subject': 'test message1', 'context': 'some text1'},
    {'sender_id': 2, 'receiver_id': 3, 'message_id': 20, 'subject': 'test message2', 'context': 'some text2'},
    {'sender_id': 3, 'receiver_id': 2, 'message_id': 30, 'subject': 'test message3', 'context': 'some text3'},
    {'sender_id': 4, 'receiver_id': 1, 'message_id': 40, 'subject': 'test message4', 'context': 'some text4'},
    {'sender_id': 5, 'receiver_id': 1, 'message_id': 50, 'subject': 'test message5', 'context': 'some text5'},
    {'sender_id': 6, 'receiver_id': 4, 'message_id': 60, 'subject': 'test message6', 'context': 'some text6'}
]

# converting the messages to string type
json_lst = [json.dumps(msg) for msg in msgs]

# ----------------------------------------- #
"""
Here we have the api functions: read, write, delete, get all and get unread.
The functions divided to tow types, functions for specific user and handling messages functions.
We use the api with the command request.get with tow parameters:
        first: 
                For specific user functions (GET_ALL_MESSAGES, GET_UNREAD_MESSAGES) we add "/user/" to URL.
                For handling messages functions (WRITE_MESSAGE, READ_MESSAGE, DELETE_MESSAGE) we add "/message/" to URL.
        second:
                Dictionary with the data we want to pass
"""

# --- Write messages --- #
"""
message_data: 
        messages: contains the messages we send, type: string or list of strings
        function: The function you want to run (e.g: WRITE_MESSAGE)        
"""
# Example:
# message_data = {'messages': json_lst, 'function': WRITE_MESSAGE}
# response = requests.get(URL + "/massage/", message_data).json()
# print(response)


# --- Delete message --- #
"""
message_data:
        function: The function you want to run (e.g: DELETE_MESSAGE)
        user_id: The user id who holds the message you want to delete
        message_id: The message id you want to delete
"""
# Example:
# message_data = {'function': DELETE_MESSAGE, 'user_id': 2, 'message_id': 30}
# response = requests.get(URL + "/massage/", message_data).json()
# print(response)


# --- Read message --- #
"""
message_data:
        function: The function you want to run (e.g: READ_MESSAGE)
        user_id: The user id who holds the message you want to read
        message_id: The message id you want to read
"""
# Example:
# message_data = {'function': READ_MESSAGE, 'user_id': 1, 'message_id': 50}
# response = requests.get(URL + "/massage/", message_data).json()
# print("--- Read Message ---")
# print(response)

# -------------------------------------------------------- #

# --- Get all messages --- #
"""
user_data:
        function: The function you want to run (e.g: GET_ALL_MESSAGES)
        user_id: The user id who holds the messages
"""
# Example:
# user_data = {"function": GET_ALL_MESSAGES, 'user_id': 2}
# response = requests.get(URL + "/user/", user_data).json()
# print("--- All Messages from user: {} ---".format(user_data['user_id']))
# pprint(response)


# --- Get unread messages --- #
"""
user_data:
        function: The function you want to run (e.g: GET_UNREAD_MESSAGES)
        user_id: The user id who holds the messages
"""
# Example:
# user_data = {"function": GET_UNREAD_MESSAGES, 'user_id': 1}
# response = requests.get(URL + "/user/", user_data).json()
# print("--- Unread Message ---")
# pprint(response)
