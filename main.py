from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    litss = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(litss)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                          Вот она какая, красная планета.
                        </div>
                      </body>
                    </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/MARS.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                            <div class="alert alert-danger" role="alert">
                              Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-success" role="alert">
                              Человечеству мала одна планета. 
                            </div>
                            <div class="alert alert-dark" role="alert">
                              Мы сделаем обитаемыми безжизненные пока планеты. 
                            </div>
                            <div class="alert alert-warning" role="alert">
                              И начнём с Марса.
                            </div>
                            <div class="alert alert-secondary" role="alert">
                              Присоединяйся.
                            </div>
                          </body>
                        </html>'''


@app.route('/astronaut_selection')
def astronaut_selection():
    return f'''<!DOCTYPE html>
                    <html>
                    <head>
                        <title>Анкета для астронавтов</title>
                    </head>
                    <body>
                        <h1>Анкета для участия в миссии на Марс</h1>
                        <form method="POST">
                            <label>Фамилия:</label>
                            <input type="text" name="surname"><br><br>
                    
                            <label>Имя:</label>
                            <input type="text" name="first_name"><br><br>
                    
                            <label>Email:</label>
                            <input type="email" name="email"><br><br>
                    
                            <label>Образование:</label>
                            <input type="text" name="education"><br><br>
                    
                            <label>Выбор профессии:</label>
                            <select name="profession">
                                <option value="engineer_researcher">Инженер-исследователь</option>
                                <option value="engineer_researcher">пилот</option>
                                <option value="engineer_researcher">строитель</option>
                                <option value="engineer_researcher">инженер жизнеобеспечения</option>
                                <option value="engineer_researcher">штурман</option>

                                </select><br><br>
                    
                            <label>Пол:</label>
                            <input type="radio" name="gender" value="male">Мужской
                            <input type="radio" name="gender" value="female">Женский<br><br>
                    
                            <label>Мотивация:</label><br>
                            <textarea name="motivation" rows="4" cols="50"></textarea><br><br>
                    
                            <label>Готовы ли остаться на Марсе?</label>
                            <input type="checkbox" name="stay_on_mars" value="Yes">Да<br><br>
                    
                            <input type="submit" value="Отправить">
                        </form>
                    </body>
                    </html>
                    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')