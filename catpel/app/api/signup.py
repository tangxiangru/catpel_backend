from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

@api.route('/signup/', methods=['POST'])
def signup():
    if request.method == 'POST':

        un = request.get_json().get('username')
        passwd = request.get_json().get('password')
        b_name = request.get_json().get('bind_name')
        
        if b_name =="":
            b_name = None
        else:
            userbind = User.query.filter_by(username=b_name).first()
            if not userbind:
                return jsonify({}),400
            b_id = userbind.id



        user = User.query.filter_by(username=un).first()

        if user:
            return jsonify({}), 400
        if b_name == None:
            new_user = User(
                        username=un,
                        password=passwd,
                        bind_id=None,
                        time=0
                       )
        else:
            new_user = User(
                        username=un,
                        password=passwd,
                        bind_id=b_id,
                        time=0
                       )
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'created': new_user.id}), 200
