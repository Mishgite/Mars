from flask import Flask, url_for, request

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


@app.route('/choice/<planet_name>')
def choice(planet_name):
    if planet_name == 'Mercury':
        return f'''<!doctype html>
                            <html lang="en">
                                <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Варианты выбора</title>
                                </head>
                                <body>
                                <h1>Моё предложение: Меркурий</h1>
                                <div class="alert alert-danger" role="alert">
                                  Планета близка к Солнцу, что означает возможность использовать солнечную;
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Благодаря невероятно высоким температурам на дневной стороне, Меркурий может стать идеальным местом для разработки новых методов цифровой обработки материалов.
                                </div>
                                <div class="alert alert-dark" role="alert">
                                  На ней есть небольшое магнитное поле;
                                </div>
                                <div class="alert alert-warning" role="alert">
                                  Колонизация Меркурия открывает дверь к будущему изучения планетарной эволюции и формированию нашей собственной солнечной системы.
                                </div>
                                </body>
                            </html>'''
    if planet_name == 'Venus':
        return f'''<!doctype html>
                            <html lang="en">
                                <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Варианты выбора</title>
                                </head>
                                <body>
                                <h1>Моё предложение: Венера</h1>
                                <div class="alert alert-danger" role="alert">
                                  Заселение Венеры может предложить уникальную возможность изучения планеты с атмосферой, близкой по составу к Земле. 
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Исследование климата и технологий для выживания на Венере может привести к разработке новых подходов к экологической устойчивости.
                                </div>
                                <div class="alert alert-dark" role="alert">
                                  Венера представляет интерес для научных открытий и технологического развития благодаря своим уникальным геологическим и метеорологическим характеристикам.
                                </div>
                                <div class="alert alert-warning" role="alert">
                                  Колонизация Венеры открывает новые перспективы для расширения границ человеческого присутствия в космосе и познания тайн нашей солнечной системы.
                                </div>
                                </body>
                            </html>'''
    if planet_name == 'Mars':
        return f'''<!doctype html>
                    <html lang="en">
                        <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Варианты выбора</title>
                        </head>
                        <body>
                        <h1>Моё предложение: Марс</h1>
                        <div class="alert alert-danger" role="alert">
                          На ней много необходимых ресурсов;
                        </div>
                        <div class="alert alert-success" role="alert">
                          На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-dark" role="alert">
                          На ней есть небольшое магнитное поле;
                        </div>
                        <div class="alert alert-warning" role="alert">
                          Наконец, она просто красива!
                        </div>
                        </body>
                    </html>'''
    if planet_name == 'Jupiter':
        return f'''<!doctype html>
                            <html lang="en">
                                <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Варианты выбора</title>
                                </head>
                                <body>
                                <h1>Моё предложение: Юпитер</h1>
                                <div class="alert alert-danger" role="alert">
                                  Заселение Юпитера представляет вызовный проект из-за его экстремальных условий, но может принести важные научные открытия.
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Исследование газового гиганта открывает путь к пониманию формирования планет и атмосфер в нашей галактике.
                                </div>
                                <div class="alert alert-dark" role="alert">
                                  Юпитер является возможным исследовательским центром для разработки технологий выживания в условиях высокого давления и радиации.
                                </div>
                                <div class="alert alert-warning" role="alert">
                                  Колонизация Юпитера может стать толчком для развития космических исследований и будущих межпланетных миссий.
                                </div>
                                </body>
                            </html>'''
    if planet_name == 'Saturn':
        return f'''<!doctype html>
                            <html lang="en">
                                <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Варианты выбора</title>
                                </head>
                                <body>
                                <h1>Моё предложение: Сатурн</h1>
                                <div class="alert alert-danger" role="alert">
                                  Заселение Сатурна предоставит уникальную возможность исследования кольца и спутников газового гиганта, что поможет расширить наше понимание формирования планет. 
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Наличие ресурсов и потенциал использования энергии от Солнца делает Сатурн привлекательным объектом для колонизации и исследований.
                                </div>
                                <div class="alert alert-dark" role="alert">
                                  Развитие новых технологий для пребывания в экстремальных условиях планеты может позитивно сказаться на развитии космической инженерии.
                                </div>
                                <div class="alert alert-warning" role="alert">
                                  Колонизация Сатурна может открыть новые горизонты для научных открытий и поиска ответов на важные вопросы о происхождении солнечной системы.
                                </div>
                                </body>
                            </html>'''
    if planet_name == 'Uranus':
        return f'''<!doctype html>
                            <html lang="en">
                                <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Варианты выбора</title>
                                </head>
                                <body>
                                <h1>Моё предложение: Уран</h1>
                                <div class="alert alert-danger" role="alert">
                                  Заселение Урана представляет инновационный вызов с уникальными атмосферными и геологическими особенностями, что может привести к совершению важных научных открытий. 
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Исследование данной планеты способствует расширению нашего понимания газовых гигантов и процессов, протекающих в их атмосферах.
                                </div>
                                <div class="alert alert-dark" role="alert">
                                  Возможности для разработки технологий адаптации к суровым условиям Урана могут способствовать развитию космической индустрии.
                                </div>
                                <div class="alert alert-warning" role="alert">
                                 Присутствие ресурсов и уникальных особенностей Урана представляет перспективы для научных исследований и будущего расширения нашего присутствия в космосе.
                                </div>
                                </body>
                            </html>'''
    if planet_name == 'Neptune':
        return f'''<!doctype html>
                            <html lang="en">
                                <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Варианты выбора</title>
                                </head>
                                <body>
                                <h1>Моё предложение: Нептун</h1>
                                <div class="alert alert-danger" role="alert">
                                  Заселение Нептуна предоставит возможность изучения дальнего газового гиганта и его уникальных характеристик, что способствует расширению научных знаний о внешних планетах.
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Нептун является объектом интереса для исследования формирования Холодного гиганта и его атмосферы.
                                </div>
                                <div class="alert alert-dark" role="alert">
                                  Развитие инновационных технологий для приспособления к холодным и ветреным условиям Нептуна может сыграть ключевую роль в развитии космической инженерии.
                                </div>
                                <div class="alert alert-warning" role="alert">
                                 Колонизация Нептуна может открыть новые перспективы в научных исследованиях космоса и помочь понять процессы, лежащие в основе формирования внешних планет.
                                </div>
                                </body>
                            </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                            <html lang="en">
                                <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Результаты</title>
                                </head>
                                <body>
                                <h1>Результаты отбора</h1>
                                <div class="alert alert-danger" role="alert">
                                  Претендента на участие в миссии {nickname}:
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Поздровляем! Ваш рейтинг после {level} эпапа отбора
                                </div>
                                <div class="alert alert-dark" role="alert">
                                  составляет {rating}!
                                </div>
                                <div class="alert alert-warning" role="alert">
                                 Желаем удачи!
                                </div>
                                </body>
                            </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!DOCTYPE html>
                        <html>  
                        <head>
                            <!--Add pre compiled library files -->
                            <!--Automatics css and js adder-->
                            <!--auto compiled css & Js-->
                            <script type="text/javascript"
                                    src="//code.jquery.com/jquery-1.9.1.js">
                        </script>
                            <link rel="stylesheet"
                                type="text/css"
                                href="/css/result-light.css">
                            <script type="text/javascript"
                                    src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js">
                        </script>
                            <link rel="stylesheet"
                                type="text/css"
                                href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
                            <link rel="stylesheet"
                                type="text/css"
                                href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
                        </head>
                        <body>
                            <!-- create a bootstrap card in a container-->
                            <div class="container">
                                <!--Bootstrap card with slider class-->
                                <div id="carousel-demo"
                                    class="carousel slide"
                                    data-ride="carousel">
                                    <div class="carousel-inner">
                                        <div class="item">
                                            <img src=
                        "{url_for('static', filename='img/mars1.jpg')}">
                                        </div>
                                        <div class="item">
                                            <img src=
                        "{url_for('static', filename='img/mars2.jpg')}">
                                        </div>
                                        <div class="item active">
                                            <img src=
                        "{url_for('static', filename='img/mars3.jpg')}">
                                        </div>
                                        <div class="item">
                                            <img src=
                        "{url_for('static', filename='img/mars4.jpg')}">
                                        </div>
                                    </div>
                                    <!--slider control for card-->
                                    <a class="left carousel-control"
                                    href="#carousel-demo"
                                    data-slide="prev">
                                        <span class="glyphicon glyphicon-chevron-left">
                                    </span>
                                    </a>
                                    <a class="right carousel-control"
                                    href="#carousel-demo"
                                    data-slide="next">
                                        <span class="glyphicon glyphicon-chevron-right">
                                    </span>
                                    </a>
                                </div>
                            </div>
                        </body>
                        </html>


    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
