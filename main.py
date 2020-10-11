from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import ast

from datetime import date
from pprint import pprint

app = Flask(__name__)
api = Api(app)

WRITE_MESSAGE = "writeMessage"
GET_ALL_MESSAGES = "getAllMessages"
GET_UNREAD_MESSAGES = "getUnreadMessages"
READ_MESSAGE = "readMessage"
DELETE_MESSAGE = "deleteMessage"
FILE = "./data.txt"
USERS = []
# user_dict = {'user_id': str, 'message': dict}
# message_dict = {'msg_id': int, 'sender_id': int}

message = reqparse.RequestParser()
message.add_argument("messages", action='split', help="List of messages")
message.add_argument("function", type=str, help="Function name to run", required=True)
message.add_argument("message_id", help="Message id number")
message.add_argument("user_id", type=int, help="User id number")

function = reqparse.RequestParser()
function.add_argument('function', type=str, required=True, help="function to run")
function.add_argument('user_id', type=int, required=True, help="User id")


class MessageHandler(Resource):

    def get(self):
        args = message.parse_args()
        func = args['function']
        if func == WRITE_MESSAGE:
            if type(args['messages']) is str:
                self.writeMessage(json.loads(args['messages']))
            elif type(args['messages']) is list:
                for msg in args['messages']:
                    self.writeMessage(json.loads(msg))
            else:
                return "Message type is invalid, please put string or list type"
            return "Messages append successfully"
        elif func == DELETE_MESSAGE:
            return self.deleteMessage(args['user_id'], args['message_id'])
        elif func == READ_MESSAGE:
            return self.readMessage(args['user_id'], args['message_id'])
        else:
            return {'error': 'function not found'}

    def writeMessage(self, message_data):
        try:
            with open(FILE, "a+") as file:
                msg = {'msg_id': message_data['message_id'], 'sender_id': message_data['sender_id'],
                       'readed': False, 'subject': message_data['subject'], 'context': message_data['context'],
                       'date': date.today().__str__()}
                user = {'user_id': message_data['receiver_id'], 'message': msg}
                try:
                    file.write(user.__str__())
                    file.write('\n')
                except Exception as e:
                    print(e)
                # USERS.append(user)
                print("append message succeeded")
            file.close()

        except Exception as e:
            print(e)
            return {'error': e}

    def deleteMessage(self, user_id, message_id):
        users = getFileData()
        try:
            for item in users:
                if item['user_id'] == user_id:
                    print("user found")
                    if item['message']['msg_id'] == int(message_id):
                        print("message found")
                        users.remove(item)
                        updateFile(users)
                        print("message deleted successfully")
                        return "Message deleted successfully"
        except Exception as e:
            print(e)
            return {'error': e}

    def readMessage(self, user_id, message_id):
        users = getFileData()
        print(users)
        try:
            for item in users:
                if item['user_id'] == user_id:
                    print("user found")
                    if item['message']['msg_id'] == int(message_id):
                        print("message found")
                        item['message']['readed'] = True
                        updateFile(users)
                        return item['message']
        except Exception as e:
            print(e)
            return {'error': e}


class UserMessageHandler(Resource):

    def get(self):
        print("inside UserMessageHandler")
        data = function.parse_args()
        if data['function'] == GET_ALL_MESSAGES:
            return self.getAllMessages(data['user_id'])
        else:
            return self.getUnreadMessages(data['user_id'])

    def getAllMessages(self, user_id):
        users = getFileData()
        lst = [item for item in users if item['user_id'] == user_id]
        print("finished to get all messeages")
        return lst

    def getUnreadMessages(self, user_id):
        users = getFileData()
        lst = [item for item in users if item['user_id'] == user_id and item['message']['readed'] is False]
        print("finished to get unread messages")
        return lst


def getFileData():
    with open(FILE, "r") as file:
        data = file.readlines()
        users = [ast.literal_eval(item) for item in data]
    return users


def updateFile(users):
    try:
        output = [(str(item) + '\n') for item in users]
        with open(FILE, "w") as file:
            file.writelines(output)
        file.close()
    except Exception as e:
        print(e)
        return {'error': e}


api.add_resource(MessageHandler, "/massage/")
api.add_resource(UserMessageHandler, "/user/")

if __name__ == "__main__":
    app.run(debug=True)
