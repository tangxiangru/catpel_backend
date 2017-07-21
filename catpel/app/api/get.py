from flask import jsonify ,request
from ..  import db
from ..models import User
from . import api
import json
import os

@api.route('/get/',methods=['POST'])
def get():
    if request.method == "POST":
        my_id = int(request.get_json().get('my_id'))

        if os.path.isdir("Message/"+str(my_id)):
            message_file=open("Message/"+str(my_id)+"/message")
            ALL_LINES = message_file.readlines()
            if ALL_LINES[2] == "haventsend":
                bind_id = int(ALL_LINES[1][8:])
                message = str(ALL_LINES[0][8:])
                os.remove("Message/"+str(my_id)+"/message")

                return jsonify({
                    "bind_id":bind_id,
                    "message":message
                })



        else:
            return jsonify({
                "status":404
            })

