from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

# index routing
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teacher_login')
def teacher_login():
    return render_template('teacher_login.html')


if __name__ == '__main__':
    manager.run()
