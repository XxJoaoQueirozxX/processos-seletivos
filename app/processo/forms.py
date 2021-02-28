from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, DateField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Optional
from ..models import Processo, Etapa


class ProcessoForm(FlaskForm):
    cargo = StringField("Cargo", validators=[DataRequired(), Length(1, 60, message="O cargo deve ter entre 1 e 60 caracteres")])
    empresa = StringField("Cargo", validators=[DataRequired(), Length(1, 40, message="O nome da empresa deve ter entre 1 e 40 caracteres")])
    dt_inicio = DateField("Data inicio", format="%d/%m/%Y")
    dt_fim = DateField("Data fim", format="%d/%m/%Y", validators=[Optional()])
    descricao = TextAreaField("Descrição")
    is_finished = BooleanField("Encerrado")
    submit = SubmitField("Salvar")

    def load_model(self, processo: Processo):
        self.cargo.data = processo.cargo
        self.empresa.data = processo.empresa
        self.descricao.data = processo.descricao
        self.dt_inicio.data = processo.dt_inicio
        self.dt_fim.data = processo.dt_fim
        self.is_finished.data = processo.is_finished


class DeleteForm(FlaskForm):
    deletar = SubmitField("Deletar")


class EtapaForm(FlaskForm):
    titulo = StringField("Titulo", validators=[DataRequired(), Length(1, 60)])
    dt_inicio = DateField("Data inicio", format="%d/%m/%Y", validators=[DataRequired()])
    dt_fim = DateField("Data fim", format="%d/%m/%Y", validators=[Optional()])
    descricao = TextAreaField("Descricao", validators=[DataRequired()])
    is_finished = BooleanField("Encerrado")
    salvar = SubmitField("Salvar")

    def load_model(self, e: Etapa):
        self.titulo.data = e.titulo
        self.descricao.data = e.descricao
        self.dt_inicio.data = e.dt_inicio
        self.dt_fim.data = e.dt_fim
        self.is_finished.data = e.is_finished
