from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def name():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
       <title>Марс</title>
   </head>
   <body>
       <h1>Миссия Колонизация Марса</h1>
   </body>
</html>'''


@app.route('/index/')
def apple():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
       <title>Марс</title>
   </head>
   <body>
       <h1>Миссия Колонизация Марса</h1>
       <h1>И на марсе будут яблони цвести!</h1>
   </body>
</html>'''


@app.route('/promotion/')
def promotion():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Реклама</title>
</head>
<body>
    <h1>Человечество вырастает из детства.</h1>
    <h1>Человечеству мала одна планета.</h1>
    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
    <h1>И начнем с Марса!</h1>
</body>
</html>"""


@app.route('/image_mars/')
def mars():
    return render_template('1.html', filename=url_for('static', filename='img/mars.jpg'))


@app.route('/promotion_image/')
def mars_promotion():
    return render_template('2.html', style=url_for('static', filename='css/style.css'),
                           filename=url_for('static', filename='img/mars.jpg'))


@app.route('/astronaut_selection/')
def application():
    return render_template('application.html', style=url_for('static', filename='css/style.css'))


@app.route('/choice/<planet_name>/')
def choice_planet(planet_name):
    return render_template('choice_planet.html', style=url_for('static', filename='css/style.css'),
                           planet_name=planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>/')
def result_test(nickname, level, rating):
    return render_template('rating.html', style=url_for('static', filename='css/style.css'),
                           nickname=nickname, level=level, rating=rating)


@app.route('/load_photo/', methods=['POST', 'GET'])
def load_image():
    if request.method == 'GET':
        return render_template('load_image.html', filename=url_for('static', filename='img/image.png'),
                               style=url_for('static', filename='css/style.css'))
    if request.method == 'POST':
        f = request.files['file']
        with open(url_for('static', filename='img/image.png')[1:], 'wb') as fr:
            fr.write(f.read())
        return render_template('load_image.html', filename=url_for('static', filename='img/image.png'),
                               style=url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    print('http://127.0.0.1:8005/load_photo/')
    app.run(port=8005, host='127.0.0.1')
