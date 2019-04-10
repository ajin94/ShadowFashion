from flask import Flask, session
from flask import render_template

sfapp = Flask(__name__)


@sfapp.route('/')
def index():
    template_arguments = {
        "user-name": session.get('user', None)
    }
    return render_template('client/index.html', template_data=template_arguments)


@sfapp.route('/signup')
def signup():
    return render_template('auth/signup.html')


if __name__ == '__main__':
    sfapp.secret_key = '6wfwef6ASDW676w6QDWD6748wd((FD'
    sfapp.config['SESSION_TYPE'] = 'filesystem'
    sfapp.run(host='0.0.0.0')
