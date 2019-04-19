import json
from flask import Flask, session, request
from flask import redirect, render_template
from flask import url_for
from flask_wtf.csrf import CSRFProtect
from connections import connection
from form_validations import valid_signup

sfapp = Flask(__name__)

@sfapp.route('/')
def index():
    template_arguments = {
        "user-name": session.get('user_name', None)
    }
    return render_template('client/index.html', template_data=template_arguments)


@sfapp.route('/signup')
def signup():
    return render_template('auth/signup.html')


@sfapp.route('/_signin', methods=['POST'])
def signin():
    user_name_or_email = request.form.get('uname_or_email', None)
    password = request.form.get('account_password', None)

    select_query = "SELECT id, user_name FROM user WHERE user_name=%s AND password=%s"
    if user_name_or_email.endswith(".com"):
        select_query = "SELECT id, user_name FROM user WHERE email=%s AND password=%s"
    args = (user_name_or_email, password)
    try:
        cursor, conn = connection()
        cursor.execute(select_query, args)
        rows = cursor.fetchall()
        if rows:
            ((id, user_name),) = rows
            session['user_name'] = user_name
            session['id'] = id
            return json.dumps({'status': 'OK'})
        else:
            return json.dumps({'status': 'NU'})
    except Exception as e:
        print(e)
    return


@sfapp.route('/logout')
def logout():
    session.pop('user_name', None)
    session.pop('id', None)
    return redirect(url_for('index'))


@sfapp.route('/user_signup', methods=['POST'])
def user_signup():
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

    try:
        cursor, conn = connection()
        insert_query = "INSERT INTO user (account_type_id, fname, sname, user_name, gender, dob, email, phone_number, house_apt, district, city, state, pin, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(form_data)
        args = (form_data['account_type'], form_data['fname'], form_data['sname'],
                form_data['uname'], form_data['gender'], form_data['dob'],
                form_data['email'], form_data['phone'], form_data['street_apt'],
                form_data['district'], form_data['city'], form_data['state'],
                form_data['pin'], form_data['password'],)
        cursor.execute(insert_query, args)
        conn.commit()
    except Exception as e:
        return json.dumps({"exception":str(e.traceback())})
        print(e)
    else:
        session['user-name'] = form_data['uname']
        cursor.close()
        conn.close()
        return redirect(url_for('index'))


@sfapp.route('/check_email_duplicate', methods=['GET'])
def check_email_duplicate():
    email_id = request.args.get('email', None)
    try:
        cursor, conn = connection()
        select_query = "SELECT user_name FROM user WHERE email=%s"
        args = (email_id,)
        cursor.execute(select_query, args)
        rows = cursor.fetchall()
        if rows:
            return json.dumps({'status': 'EXISTING'})
    except Exception as e:
        print(e)
    return json.dumps({'status': 'OK'})


if __name__ == '__main__':
    sfapp.secret_key = '6wfwef6ASDW676w6QDWD6748wd((FD'
    sfapp.config['SESSION_TYPE'] = 'filesystem'
    csrf = CSRFProtect()
    csrf.init_app(sfapp)
    sfapp.run(host='0.0.0.0')
