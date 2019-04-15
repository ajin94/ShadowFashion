from flask import Flask, session, request
from flask import redirect, render_template
from flask import url_for
from flask_wtf.csrf import CSRFProtect
from connections import Connection
from form_validations import valid_signup

sfapp = Flask(__name__)


@sfapp.route('/')
def index():
    template_arguments = {
        "user-name": session.get('user', None)
    }
    return render_template('client/index.html', template_data=template_arguments)


@sfapp.route('/signup')
def signup():
    return render_template('auth/signup.html')\



@sfapp.route('/validate_and_add_user', methods=['POST'])
def validate_and_add_user():
    import pdb; pdb.set_trace()
    form_data = dict()
    form_data['account_type'] = int(request.form.get('account_type', None))
    form_data['fname'] = request.form.get('fname', None)
    form_data['sname'] = request.form.get('sname', None)
    form_data['uname'] = request.form.get('uname', None)
    form_data['gender'] = request.form.get('gender', None)
    form_data['dob'] = request.form.get('dob', None)
    form_data['email'] = request.form.get('email', None)
    form_data['phone'] = request.form.get('phone', None)
    form_data['street_apt'] = request.form.get('street_apt', None)
    form_data['district'] = request.form.get('district', None)
    form_data['city'] = request.form.get('city', None)
    form_data['state'] = request.form.get('state', None)
    form_data['pin'] = request.form.get('pin', None)
    form_data['password'] = request.form.get('password', None)

    if not valid_signup(form_data):
        return redirect(url_for('signup'))

    try:
        cursor, con_obj = Connection()
        insert_query = """INSERT INTO user (account_type_id, fname, sname, gender, dob, user_name,
                          password, email, phone_number, house_apt, district, city, state, pin)
                          VALUES (%i,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    except Exception as e:
        print(e)
    else:
        con_obj.close()
        return redirect(url_for('index'))


if __name__ == '__main__':
    sfapp.secret_key = '6wfwef6ASDW676w6QDWD6748wd((FD'
    sfapp.config['SESSION_TYPE'] = 'filesystem'
    csrf = CSRFProtect()
    csrf.init_app(sfapp)
    sfapp.run(host='0.0.0.0')
