from flask import url_for, redirect, render_template, flash, request
from flask_login import login_user, logout_user
from ..models import User
from ..decorators import redirect_logged_users
from .forms import LoginForm, RegisterForm
from . import auth


@auth.route("/login", methods=["GET", "POST"])
@redirect_logged_users
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u is not None and u.confirm_password(form.password.data):
            flash("Você está logado agora", "success")
            login_user(u, form.remember_me.data)
            _next = request.args.get("next")
            if _next is None or not _next.startswith("/"):
                _next = url_for("main.index")
            return redirect(_next)
        flash("Credenciais inválidas", "error")
    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
@redirect_logged_users
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User()
        u.email = form.email.data
        u.password = form.password.data
        u.save()
        flash("Registrado com sucesso", "success")
        return redirect(url_for(".login"))
    return render_template("register.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
