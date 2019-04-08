from flask import Flask
from flask import render_template

sfapp = Flask(__name__)


@sfapp.route('/')
def index():
    return render_template('client/index.html')


@sfapp.route('/projects')
def projects():
    return render_template('client/projects.html')


@sfapp.route('/testimonials')
def testimonials():
    return render_template('client/testimonials.html')


@sfapp.route('/about')
def about():
    return render_template('client/aboutus.html')

if __name__ == '__main__':
    sfapp.run(host='0.0.0.0')
