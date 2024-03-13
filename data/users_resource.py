import flask
from flask import jsonify, request, make_response, abort
import datetime
from data import db_session
from flask_restful import Resource
from data.users import User


db_session.global_init('../db/database.db')
db_sess = db_session.create_session()


def abort_if_user_not_found(news_id):
    session = db_session.create_session()
    news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        users = db_sess.query(User).filter(User.id == user_id)
        return jsonify(
            {
                'users':
                    [item.to_dict(only=(
                        "id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password",
                        "modified_date", "city"))
                        for item in users]
            }
        )

    def post(self):
        if not request.json:
            return make_response(jsonify({'error': 'Empty request'}), 400)
        elif not all(key in request.json for key in
                     ["id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password",
                      "modified_date", "city"]):
            return make_response(jsonify({'error': 'Bad request'}), 400)
        db_sess = db_session.create_session()
        user = User()
        user.surname = request.json['surname']
        user.name = request.json['name']
        user.age = request.json['age']
        user.position = request.json['position']
        user.speciality = request.json['speciality']
        user.address = request.json['address']
        user.email = request.json['email']
        user.hashed_password = request.json['hashed_password']
        user.modified_date = datetime.datetime.strptime(request.json['modified_date'])
        user.city = request.json['city']

        db_sess.add(user)
        db_sess.commit()

        return jsonify({'id': user.id})

    def delete(self, news_id):
        abort_if_user_not_found(news_id)
        session = db_session.create_session()
        news = session.query(User).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        users = db_sess.query(User).all()
        return users