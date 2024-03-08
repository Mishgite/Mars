from flask import Flask, url_for, request, render_template, redirect, abort
import sqlalchemy
import json
import random
import sqlite3
from data import db_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from requests import session
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, NumberRange
from flask_wtf import FlaskForm
from flask_login import login_user, current_user, LoginManager, logout_user, login_required
from data.jobs import Job
from data.users import User


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init('db/database.db')
db_sess = db_session.create_session()


@login_manager.user_loader
def load_user(user_id: int):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def get_jobs_from_db(name):
    conn = sqlite3.connect(f'db/{name}')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    jobs = cursor.fetchall()
    conn.close()
    return jobs


db_session.global_init('db/database.db')
db_sess = db_session.create_session()


@app.route('/')
def works_log():
    jobs = db_sess.query(Job).all()
    return render_template('jobs.html', title='Журнал работ', jobs=jobs)


@app.route('/promotion')
def promotion():
    litss = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(litss)


image = ''


@app.route('/load_photo', methods=['POST', 'GET'])
def form_sample():
    global image
    if request.method == 'POST':
        f = request.files['file']
        with open('static/img/test_image_01.png', 'wb') as img_file:
            img_file.write(f.read())
        image = 'static/img/test_image_01.png'

    return r'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="static/css/styles.css">
                        <title>Отбор астронавтов</title>
                      </head>
                      <body>
                        <h1>Загрузка фотографии</h1>
                        <h3>для участия в миссии</h3>
                        <div>
                            <form class="select_form" method="post" enctype="multipart/form-data"> 
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label><br>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <br>
                                {image_or_not}
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''.format(image_or_not='<img src="static/img/test_image_01.png" width=400 alt="здесь должна была быть картинка, но не нашлась">' if image else '')


class Registr(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired(), NumberRange(1, 150)])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Работа', validators=[DataRequired()])
    address = StringField('Модуль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registr()
    if form.validate_on_submit():
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.email = form.email.data
        user.hashed_password = form.password.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        db_sess.add(user)
        db_sess.commit()

    return render_template('register.html', form=form)


@app.route('/answer')
def answer():
    user_data = {
        'surname': 'Smith',
        'name': 'John',
        'education': 'Магистр космической инженерии',
        'profession': 'Астронавт',
        'sex': 'Мужской',
        'motivation': 'Исследование неизвестного',
        'ready': 'Да'
    }
    return render_template('auto_answer.html', **user_data)


class AccessForm(FlaskForm):
    astronaut_id = StringField('Astronaut ID', validators=[DataRequired()])
    astronaut_password = PasswordField('Astronaut Password', validators=[DataRequired()])
    captain_id = StringField('Captain ID', validators=[DataRequired()])
    captain_token = PasswordField('Captain Token', validators=[DataRequired()])
    submit = SubmitField('Login')


urls = ['static/img/mars1.jpg',
        'static/img/mars2.jpg',
        'static/img/mars3.jpg']


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    if request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/mars{len(urls) - 3}.png', 'wb') as img_file:
            img_file.write(f.read())
        urls.append(f'static/img/mars{len(urls) - 3}.png')

    return render_template('galery.html', title='Галерея с добавлением', urls=urls)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль')
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form,
                               current_user=current_user)
    return render_template('login.html', title='Авторизация', form=form)


class Registr_Jobs(FlaskForm):
    team_leader_id = StringField('ID тим-лидера', validators=[DataRequired(), NumberRange(1, 1500)])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = StringField('Время работы', validators=[DataRequired(), NumberRange(1, 1500)])
    collaborators = StringField('ID других участников', validators=[DataRequired()])
    remember_me = BooleanField('Работа выполнена')
    submit = SubmitField('Добавить')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register_jobs', methods=['GET', 'POST'])
def register_jobs():
    form = Registr_Jobs()
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        job = Job()
        job.team_leader_id = form.team_leader_id.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.remember_me.data
        db_sess.add(job)
        db_sess.commit()

    return render_template('register_jobs.html', form=form)


class JobForm(FlaskForm):
    team_leader_id = IntegerField('ID лидера', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Время работы', validators=[DataRequired()])
    collaborators = StringField('ID других участников', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена?', default=False)
    submit = SubmitField("Готово")


@app.route('/job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id: int):
    form = JobForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        if current_user.id == 1:
            job = db_sess.query(Job).filter(Job.id == id).first()
        else:
            job = db_sess.query(Job).filter(Job.id == id,
                                                 Job.team_leader == current_user).first()
        if job:
            form.team_leader_id.data = job.team_leader_id
            form.job.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if current_user.id == 1:
            job = db_sess.query(Job).filter(Job.id == id).first()
        else:
            job = db_sess.query(Job).filter(Job.id == id,
                                            Job.team_leader == current_user).first()
        if job:
            job.team_leader_id = form.team_leader_id.data
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job.html', title='Изменить работу', form=form)


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def job_delete(id: int):
    db_sess = db_session.create_session()
    if current_user.id == 1:
        job = db_sess.query(Job).filter(Job.id == id).first()
    else:
        job = db_sess.query(Job).filter(Job.id == id,
                                        Job.team_leader == current_user).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


if __name__ == '__main__':
    from data import api_jobs, api_users
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'random_key'
    app.register_blueprint(api_jobs.blueprint)
    app.register_blueprint(api_users.blueprint)
    app.run(port=5000, host='127.0.0.1')
