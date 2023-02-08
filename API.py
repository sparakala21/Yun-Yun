# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:13:05 2023

@author: Sravan Parakala
"""

from flask import *
import json
import time

app = Flask(__name__)

user1 = {
  "name": 'name1',
  "isHere": True,
  "hereAt": 0.0

}
user2 = {
  "name": 'name2',
  "isHere": True,
  "hereAt": 0.0
}
user3 = {
  "name": 'name3',
  "isHere": True,
  "hereAt": 0.0
}
users = [user1,user2,user3]
@app.route('/', methods=['GET'])
def home_page():
    
    return users

@app.route('/user/', methods=['GET'])
def request_page():
    
    
    user_query = str(request.args.get('user'))
    
    for user in users:
        if user["name"] == user_query:
            print(user_query, "has left")
            user["isHere"] =False
            json_dump = json.dumps(user)
            users.remove(user)
            return json_dump
    
    data_set = {'name': user_query, 'isHere': True,  'Timestamp': time.time()}
    users.append(data_set)
    json_dump = json.dumps(data_set)
    
    return json_dump
    
if __name__ == '__main__':
    app.run(port = 7777)