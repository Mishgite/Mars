import flask
from flask import jsonify, request, make_response
import datetime
from data import db_session
from flask_restful import Resource
from data.jobs import Job
from data.users import User


db_session.global_init('../db/database.db')
db_sess = db_session.create_session()


class UsersResource(Resource):
    def get(self):
        users = db_sess.query(User).all()
        return users


class UsersListResource(Resource):
    def get(self, user_id):
        users = db_sess.query(User).filter(User.id == user_id)
        return users