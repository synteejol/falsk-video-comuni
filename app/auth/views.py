from .models import AuthUser 
from flask import Flask, render_template, request, redirect, render_template_string, session, url_for, flash, Blueprint
from flask_login import current_user, UserMixin,  LoginManager, login_user, logout_user, login_required, fresh_login_required, confirm_login
from werkzeug.urls import url_parse


auth_blueprint = Blueprint('auth_blueprint', __name__,
    template_folder='templates')
    #static_folder='static', static_url_path='assets')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('view_home_page'))
    #form = LoginForm()
    if request.method == 'POST':
        user = AuthUser.query.filter_by(username=request.form['userName']).first()
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('view_home_page')
        return redirect(next_page)
    return render_template('login.html', title='Sign In')

