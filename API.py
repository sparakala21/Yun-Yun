# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:13:05 2023

@author: Sravan Parakala
"""

from flask import *
import json
import time


'''
http://ipaddress:5000/add/?user={username}    add user username
http://ipaddress:5000/add/?user={username}    remove user username
http://ipaddress:5000                         main list




'''


def entry_time(user, l):
    print("{} entered at {}:{} on {}/{}/{}".format(user, l[3],l[4], l[1],l[2], l[0]))
    
def exit_time(user, l):
    print("{} left at {}:{} on {}/{}/{}".format(user, l[3],l[4], l[1],l[2], l[0]))
app = Flask(__name__)


users = []
@app.route('/', methods=['GET'])
def home_page():
    for user in users:
        print(user['name'])
    return users

@app.route('/add/', methods=['GET'])
def add_page():
    
    
    user_query = str(request.args.get('user'))
    if user_query == '':
        return json_dump
    for user in users:
        if user["name"] == user_query:
            print("Repeated user", user_query)
            return json.dumps(user)
    times = (time.time(),time.localtime())
    
    data_set = {'name': user_query,'time': times[0]}
    entry_time(user_query, times[1])
    users.append(data_set)
    json_dump = json.dumps(data_set)
    
    return json_dump
@app.route('/remove/', methods=['GET'])
def remove_page():
    user_query = str(request.args.get('user'))
    if user_query == '':
        return json.dumps()
    for user in users:
        if user["name"] == user_query:
            users.remove(user)
            return json.dumps(user)
    print("User {} not in list", user_query)
    return json.dumps(user_query)
if __name__ == '__main__':
    app.run(host = "0.0.0.0")