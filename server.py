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
        insert_query = "INSERT INTO user (account_type_id, fname, sname, user_name, gender, dob, email, phone_number, house_apt, district, city, state, pin, password) VALUES (%i,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        args = (form_data['account_type'], form_data['fname'], form_data['sname'],
                form_data['uname'], form_data['gender'], form_data['dob'],
                form_data['email'], form_data['phone'], form_data['street_apt'],
                form_data['district'], form_data['city'], form_data['state'],
                form_data['pin'], form_data['password'],)
        cursor.execute(insert_query, args)
        con_obj.commit()
    except Exception as e:
        print(e)
    else:
        cursor.close()
        con_obj.close()
        return redirect(url_for('index'))


if __name__ == '__main__':
    sfapp.secret_key = '6wfwef6ASDW676w6QDWD6748wd((FD'
    sfapp.config['SESSION_TYPE'] = 'filesystem'
    csrf = CSRFProtect()
    csrf.init_app(sfapp)
    sfapp.run(host='0.0.0.0')
