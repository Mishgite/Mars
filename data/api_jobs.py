import flask
from flask import jsonify, request
import datetime
from data import db_session
from data.jobs import Job


blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    "team_leader_id", "job", "work_size", "collaborators", "start_date", "end_date", "is_finished"))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def api_jobs(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).filter(Job.id == job_id)
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    "team_leader_id", "job", "work_size", "collaborators", "start_date", "end_date", "is_finished"))
                    for item in jobs]
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    db_sess = db_session.create_session()
    job = Job()
    job.team_leader_id = request.json['team_leader_id']
    job.job = request.json['job']
    job.work_size = request.json['work_size']
    job.start_date = datetime.datetime.strptime(request.json['start_date'])
    job.is_finished = request.json['is_finished']
    job.collaborators = request.json['collaborators']

    db_sess.add(job)
    db_sess.commit()

    return jsonify({'id': job.id})