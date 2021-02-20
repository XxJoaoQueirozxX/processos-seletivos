from flask import url_for, redirect, render_template, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from ..decorators import redirect_logged_users
from ..email import send_email
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
    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
@redirect_logged_users
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User()
        u.email = form.email.data
        u.password = form.password.data
        u.save()

        token = u.generate_confirmation_token()
        send_email(
            u.email,
            "Confirme sua email",
            "auth/mail/confirm_email",
            user=u,
            token=token
        )
        flash("Registrado com sucesso, um email de confirmação foi enviado para seu email", "success")
        return redirect(url_for(".login"))
    return render_template("auth/register.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash("Email confirmado com sucesso. Obrigado!")
    else:
        flash("Link de confirmação inválido ou expirado")
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != 'auth'\
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route("/confirm")
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(
        current_user.email,
        "Confirme seu email",
        "auth/mail/confirm_email",
        user=current_user,
        token=token
    )
    flash("Um novo email de confirmação de confirmação foi enviado para você.")
    return redirect(url_for('main.index'))


@auth.route("/unconfirmed")
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


