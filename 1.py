from flask import Flask, url_for, render_template

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
    <h1>Присоединяйся!</h1>
</body>
</html>"""
@app.route('/image_mars/')
def mars():
    return render_template('1.html', filename=url_for('static', filename='img/mars.jpg'))


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')