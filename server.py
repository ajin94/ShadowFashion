import json
from flask import Flask, session, request, send_file
from flask import redirect, render_template
from flask import url_for
from flask_wtf.csrf import CsrfProtect
from connections import get_connection
import traceback

sfapp = Flask(__name__)
sfapp.secret_key = '6wfwef6ASDW676w6QDWD6748wd((FD'
sfapp.config['SESSION_TYPE'] = 'filesystem'
sfapp.config['WTF_CSRF_SECRET_KEY'] = 'asdaDa#$@%fewd#22342FWFQE'
csrf = CsrfProtect()
csrf.init_app(sfapp)


@sfapp.route('/')
def index():
    template_arguments = {
        "user-name": session.get('user_name', None),
        "points": session.get('points', None)
    }
    return render_template('client/index.html', template_data=template_arguments)


@sfapp.route('/collaboration')
def collaboration():
    template_arguments = {
        "user-name": session.get('user_name', None),
        "points": session.get('points', None)
    }
    return render_template('client/collaboration.html', template_data=template_arguments)


@sfapp.route('/store')
def store():
    template_arguments = {
        "user-name": session.get('user_name', None),
        "points": session.get('points', None)
    }
    return render_template('client/store.html', template_data=template_arguments)


@sfapp.route('/contest')
def contest():
    template_arguments = {
        "user-name": session.get('user_name', None),
        "points": session.get('points', None)
    }
    return render_template('client/contest.html', template_data=template_arguments)


@sfapp.route('/contact')
def contact():
    template_arguments = {
        "user-name": session.get('user_name', None),
        "points": session.get('points', None)
    }
    return render_template('client/contact.html', template_data=template_arguments)


@sfapp.route('/aboutus')
def aboutus():
    template_arguments = {
        "user-name": session.get('user_name', None),
        "points": session.get('points', None)
    }
    return render_template('client/about.html', template_data=template_arguments)


@sfapp.route('/signup')
def signup():
    account_types_dict = {}
    select_query = "SELECT * FROM account_types"
    try:
        cursor, conn = get_connection()
        cursour_result = cursor.execute(select_query)
        if cursour_result:
            rows = cursor.fetchall()
            account_types_dict = {id: name for (id, name) in rows}
    except Exception as e:
        pass
    return render_template('auth/signup.html', account_type_dict=account_types_dict)


@sfapp.route('/_send_message', methods=['POST'])
def send_message():
    form_data = dict()
    form_data['email'] = request.form.get('email', None)
    form_data['message'] = request.form.get('msg', None)
    try:
        cursor, conn = get_connection()
        insert_query = "INSERT INTO messages (email, message) VALUES (%s,%s)"
        args = (form_data['email'], form_data['message'],)
        cursor.execute(insert_query, args)
        conn.commit()
    except Exception as e:
        return json.dumps({"status": "ERROR"})
    else:
        return json.dumps({"status": "OK"})

    return json.dumps({'status': 'OK'})


@sfapp.route('/_signin', methods=['POST'])
def signin():
    user_name_or_email = request.form.get('uname_or_email', None)
    password = request.form.get('account_password', None)

    select_query = "SELECT id, user_name, reward_point FROM user WHERE user_name=%s AND password=%s"
    if user_name_or_email.endswith(".com"):
        select_query = "SELECT id, user_name, reward_point FROM user WHERE email=%s AND password=%s"
    args = (user_name_or_email, password)
    try:
        cursor, conn = get_connection()
        cursor.execute(select_query, args)
        rows = cursor.fetchall()
        if rows:
            ((id, user_name, reward_point),) = rows
            session['user_name'] = user_name
            session['id'] = id
            session['points'] = reward_point
            return json.dumps({'status': 'OK'})
        else:
            return json.dumps({'status': 'NU'})
    except Exception as e:
        print(e)
    return json.dumps({'status': 'OK'})


@sfapp.route('/logout')
def logout():
    session.pop('user_name', None)
    session.pop('id', None)
    session.pop('points', None)
    return redirect(url_for('index'))


@sfapp.route('/_get_participation_form')
def get_participation_form():
    try:
        return send_file('/home/mxp/projects/ShadowFashion/static/files/pageantapplicationform.pdf',
                         attachment_filename='participant_form.pdf', as_attachment=True)
    except Exception as e:
        return str(e)


@sfapp.route('/_user_signup', methods=['POST'])
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
        cursor, conn = get_connection()
        insert_query = "INSERT INTO user (account_type_id, fname, sname, user_name, gender, dob, email, phone_number, house_apt, district, city, state, pin, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(form_data)
        args = (form_data['account_type'], form_data['fname'], form_data['sname'],
                form_data['uname'], form_data['gender'], form_data['dob'],
                form_data['email'], form_data['phone'], form_data['street_apt'],
                form_data['district'], form_data['city'], form_data['state'],
                form_data['pin'], form_data['password'])
        cursor.execute(insert_query, args)
        conn.commit()
    except Exception as e:
        return json.dumps({"status": "ERROR"})
    else:
        session['user_name'] = form_data['uname']
        session['points'] = 100
        return json.dumps({"status": "OK"})


@sfapp.route('/_check_email_duplicate', methods=['GET'])
def check_email_duplicate():
    email_id = request.args.get('email', None)
    try:
        cursor, conn = get_connection()
        select_query = "SELECT user_name FROM user WHERE email='{}'".format(email_id)
        cursor.execute(select_query)
        rows = cursor.fetchall()
        if rows:
            return json.dumps({'status': 'EXISTING'})
    except Exception as e:
        print(traceback.format_exc())
        return json.dumps({'status': 'ERROR'})
    return json.dumps({'status': 'OK'})


@sfapp.route('/_check_phone_duplicate', methods=['GET'])
def check_phone_duplicate():
    phone = request.args.get('phone', None)
    try:
        cursor, conn = get_connection()
        select_query = "SELECT user_name FROM user WHERE phone_number='{}'".format(phone)
        cursor.execute(select_query)
        rows = cursor.fetchall()
        if rows:
            return json.dumps({'status': 'EXISTING'})
    except Exception as e:
        return json.dumps({'status': str(traceback.format_exc())})
    return json.dumps({'status': 'OK'})


@sfapp.route('/_check_uname_duplicate', methods=['GET'])
def check_uname_duplicate():
    user_name = request.args.get('user_name', None)
    try:
        cursor, conn = get_connection()
        select_query = "SELECT user_name FROM user WHERE user_name='{}'".format(user_name)
        cursor.execute(select_query)
        rows = cursor.fetchall()
        if rows:
            return json.dumps({'status': 'EXISTING'})
    except Exception as e:
        return json.dumps({'status': 'ERROR'})
    return json.dumps({'status': 'OK'})

# if __name__ == "__main__":
#     sfapp.run()
