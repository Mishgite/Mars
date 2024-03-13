import flask
from flask import jsonify, request, make_response
import datetime
from data import db_session
from data.jobs import Job
from data.users import User
from data.users_resource import UsersResource, UsersListResource


blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/v2/users')
def get_users():
    user = UsersResource()
    return jsonify(
        {
            'users':
                [item.to_dict(only=(
                    "id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password", "modified_date", "city"))
                 for item in user.get()]
        }
    )


@blueprint.route('/api/v2/users/<int:user_id>')
def get_users1(user_id):
    user = UsersListResource()
    return jsonify(
        {
            'users':
                [item.to_dict(only=(
                    "id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password", "modified_date", "city"))
                 for item in user.get(user_id)]
        }
    )


@blueprint.route('/api/users')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=(
                    "id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password", "modified_date", "city"))
                 for item in jobs]
        }
    )


@blueprint.route('/api/users/<int:job_id>')
def api_jobs(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(User).filter(User.id == job_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    "id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password", "modified_date", "city"))
                    for item in jobs]
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def add_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ["id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password", "modified_date", "city"]):
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


@blueprint.route('/api/users/<int:job_id>', methods=['DELETE'])
def delete_job(job_id: int):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(job_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(user)
    db_sess.commit()

    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:job_id>', methods=['PUT'])
def edit_job(job_id: int):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(job_id)

    if not user:
        return make_response(jsonify({'error': 'Empty request'}), 404)
    elif not all(key in ["id", "surname", "name", "age", "position", "speciality", "address", "email", "hashed_password", "modified_date", "city"] for key in request.json):
        return make_response(jsonify({'error': 'Wrong request'}), 404)

    for key in request.json:
        if key == 'surname':
            user.surname = request.json['surname']
        elif key == 'name':
            user.name = request.json['name']
        elif key == 'age':
            user.age = request.json['age']
        elif key == 'position':
            user.position = request.json['position']
        elif key == 'speciality':
            user.speciality = request.json['speciality']
        elif key == 'address':
            user.address = request.json['address']
        elif key == 'email':
            user.email = request.json['email']
        elif key == 'hashed_password':
            user.hashed_password = request.json['hashed_password']
        elif key == 'modified_date':
            user.modified_date = datetime.datetime.strptime(request.json['modified_date'])
        elif key == 'city':
            user.city = request.json['city']

    db_sess.add(user)
    db_sess.commit()

    return jsonify({'success': 'OK'})
