from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_required
from ..models import Processo
from .forms import ProcessoForm
from . import processo


@processo.route("/processos")
@login_required
def all():
    processos = current_user.processos.all()
    return render_template("processo/processos.html", processos=processos)


@processo.route("/processos/add", methods=["GET", "POSt"])
@login_required
def add():
    form = ProcessoForm()
    if form.validate_on_submit():
        p = Processo()
        p.cargo = form.cargo.data
        p.descricao = form.descricao.data
        p.dt_inicio = form.dt_inicio.data
        p.dt_fim = form.dt_fim.data
        p.user = current_user
        p.save()
        flash("Processo cadastrado com sucesso", "success")
        return redirect(url_for('.all'))
    return render_template("processo/add_processo.html", form=form)


@processo.route("/processo/<int:id>")
@login_required
def get_processo(id):
    p = current_user.processos.filter_by(id=id).first_or_404()
    return render_template("processo/processo.html", processo=p)


@processo.route("/processo/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):
    p = current_user.processos.filter_by(id=id).first_or_404()
    form = ProcessoForm()
    if form.validate_on_submit():
        p.cargo = form.cargo.data
        p.descricao = form.descricao.data
        p.dt_inicio = form.dt_inicio.data
        p.dt_fim = form.dt_fim.data
        p.save()
        flash("Processo atualizado com sucesso", "success")
        return redirect(url_for(".get_processo", id=id))
    form.load_model(p)
    return render_template("processo/edit_processo.html", form=form)
