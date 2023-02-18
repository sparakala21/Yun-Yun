# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:13:05 2023

@author: Sravan Parakala
"""

from flask import *
import json
import time


'''
http://ipaddress:5000/commons/add/?user={username}       add user username to commons

http://ipaddress:5000/commons/remove/?user={username}    remove user username from commons

http://ipaddress:5000/union/add/?user={username}         add user username to union

http://ipaddress:5000/union/remove/?user={username}      remove user username from union

http://ipaddress:5000/add/?user={username}               remove user username

http://ipaddress:5000/union                              union list

http://ipaddress:5000/commons                            union list

'''


def entry_time(user, l):
    print("{} entered at {}:{} on {}/{}/{}".format(user, l[3],l[4], l[1],l[2], l[0]))
    
def exit_time(user, l):
    print("{} left at {}:{} on {}/{}/{}".format(user, l[3],l[4], l[1],l[2], l[0]))
app = Flask(__name__)

<<<<<<< Updated upstream

union = []
commons = []
@app.route('/union', methods=['GET'])
def union_page():
    for user in union:
        print(user['name'])
    return union



@app.route('/union/add/', methods=['GET'])
def add_page_union():
    
    
    user_query = str(request.args.get('user'))
    if user_query == '':
        return json_dump
    for user in union:
        if user["name"] == user_query:
            print("Repeated user", user_query)
            return json.dumps(user)
    times = (time.time(),time.localtime())
    
    data_set = {'name': user_query,'time': times[0]}
    entry_time(user_query, times[1])
    union.append(data_set)
    json_dump = json.dumps(data_set)
    
    return json_dump
@app.route('/union/remove/', methods=['GET'])
def remove_page_union():
    user_query = str(request.args.get('user'))
    if user_query == '':
        return json.dumps()
    for user in union:
        if user["name"] == user_query:
            union.remove(user)
            return json.dumps(user)
    print("User {} not in list", user_query)
    return json.dumps(user_query)


@app.route('/commons', methods=['GET'])
def commons_page():
    for user in commons:
        print(user['name'])
    return commons


@app.route('/commons/add/', methods=['GET'])
def add_page_commons():
    
    
    user_query = str(request.args.get('user'))
    if user_query == '':
        return json_dump
    for user in commons:
        if user["name"] == user_query:
            print("Repeated user", user_query)
            return json.dumps(user)
    times = (time.time(),time.localtime())
    
    data_set = {'name': user_query,'time': times[0]}
    entry_time(user_query, times[1])
    commons.append(data_set)
    json_dump = json.dumps(data_set)
    
    return json_dump
@app.route('/commons/remove/', methods=['GET'])
def remove_page_commons():
    user_query = str(request.args.get('user'))
    if user_query == '':
        return json.dumps()
    for user in commons:
        if user["name"] == user_query:
            commons.remove(user)
            return json.dumps(user)
    print("User {} not in list", user_query)
    return json.dumps(user_query)



if __name__ == '__main__':
    app.run(host = "0.0.0.0")