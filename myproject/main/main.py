from datetime import time

import requests
from MySQLdb import escape_string as thwart
from flask import Blueprint, render_template, request, abort, \
    session, send_from_directory
from flask_login import login_required, current_user
from werkzeug.datastructures import ImmutableOrderedMultiDict

from myproject import db
from myproject.models import MenuList, payments, Orders

main = Blueprint('main', __name__, template_folder='temp')


@main.route('/')
@login_required
def index():
    tas = tasks.query.filter_by(user_id== current_user.id)

    return render_template("index.html", tas)


@main.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = UsersModel.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=True, duration=datetime.timedelta(weeks=52))

            nex = request.args.get('next')

            if nex is None or not nex[0] == '/':
                nex = url_for('main.index')
            return redirect(nex)
        else:
            flash(Markup('''<div class="alert alert-primary alert-dismissible fade show" role="alert">
   The password or the email is incorrect.
  </div>'''))
            return render_template("login.html", form=form, d=form.errors)
    print(form.errors)
    return render_template('login.html', form=form, d=form.errors)

@main.route('/add')
@login_required
def add():
    a_new = adding_new()
    if a_new.validate_on_submit():
        d = tasks(user_id= current_user.id, description= a_new.description.data, title=a_new.title.data)
        try:
            db.session.add(d)
            db.session.commit()
        except:
            db.session.rollback()

        return redirect('/')
    return render_template('add.html', a_new)


@main.route('/done')
@login_required
def done():
    re = request.get('id')
    ta = tasks.query.get(re)
    if ta.user_id != current_user.id:
        abort(404)
    ta.done = True
    return "done"


@main.route('/main_js')
def main_js():
    reque = request.args.get('id')
    return render_template("main.js", t = reque)
