from flask_restful import reqparse, abort, Resource
from flask import jsonify

from data.db_session import create_session
from data.jobs import Job


parser = reqparse.RequestParser()
parser.add_argument('team_leader_id', type=int, required=True)
parser.add_argument('job', type=str, required=True)
parser.add_argument('work_size', type=int, required=True)
parser.add_argument('collaborators', type=str, required=True)
parser.add_argument('category', type=str, required=True)
parser.add_argument('is_finished', type=bool, required=True)


def abort_if_user_doesnt_exist(user_id):
    db_sess = create_session()
    user = db_sess.query(Job).filter(Job.id == user_id)

    if not user:
        abort(404, messgae=f"Jobs {user_id} doesn't exist")

    return user, db_sess


class JobsResource(Resource):
    def get(self, user_id):
        user, _ = abort_if_user_doesnt_exist(user_id)
        return jsonify(
            {
                'jobs':
                    [item.to_dict(only=(
                        "id", "team_leader_id", "team_leader", "job", "work_size", "collaborators", "start_date",
                        "end_date", "category", "is_finished"))
                        for item in user]
            }
        )

    def delete(self, user_id):
        user, db_sess = abort_if_user_doesnt_exist(user_id)
        db_sess.delete(user)
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        db_sess = create_session()
        users = db_sess.query(Job).all()
        return jsonify(
            {
                'jobs':
                    [item.to_dict(only=(
                        "id", "team_leader_id", "team_leader", "job", "work_size", "collaborators", "start_date",
                        "end_date", "category", "is_finished"))
                        for item in users]
            }
        )

    def post(self):
        args = parser.parse_args()
        db_sess = create_session()
        job = Job()
        job.team_leader_id = args['team_leader_id']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.category = args['category']
        job.is_finished = args['is_finished']
        db_sess.add(job)
        db_sess.commit()

        return jsonify({'user_id': job.id})
