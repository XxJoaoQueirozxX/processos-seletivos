from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Optional
from ..models import Processo, Etapa


class ProcessoForm(FlaskForm):
    cargo = StringField("Cargo", validators=[DataRequired(), Length(1, 60, message="O cargo deve ter entre 1 e 60 caracteres")])
    dt_inicio = DateField("Data inicio", format="%d/%m/%Y")
    dt_fim = DateField("Data fim", format="%d/%m/%Y", validators=[Optional()])
    descricao = TextAreaField("Descrição")
    submit = SubmitField("Salvar")

    def load_model(self, processo: Processo):
        self.cargo.data = processo.cargo
        self.descricao.data = processo.descricao
        self.dt_inicio.data = processo.dt_inicio
        self.dt_fim.data = processo.dt_fim


# class DeleteForm(FlaskForm):
#     deletar = SubmitField("Deletar")
