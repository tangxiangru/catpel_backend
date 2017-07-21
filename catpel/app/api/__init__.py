from flask import Blueprint

api = Blueprint('api',__name__)

from . import signup,signin,uploadtime,getinfo,forgive,send_info,get
