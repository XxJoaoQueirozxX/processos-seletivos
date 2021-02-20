from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    processo = db.relationship("Processo", backref="user", cascade="all,delete-orphan", lazy='dynamic')

    def __repr__(self):
        return f"<user {self.email}>"

    def save(self):
        db.session.add(self)
        db.session.commit(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError("O campo 'password' não pode ser acessado diretamente")

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def confirm_password(self, pwd: str):
        return check_password_hash(self.password_hash, pwd)


class Processo(db.Model):
    __tablename__ = "processos"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"))
    cargo = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    dt_inicio = db.Column(db.Date, nullable=False)
    dt_fim = db.Column(db.Date)
    etapas = db.relationship("Etapa", backref="processo", cascade="all,delete-orphan", lazy='dynamic')

    def __repr__(self):
        return f"<Processo {self.cargo}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Etapa(db.Model):
    __tablename__ = "etapas"
    id = db.Column(db.Integer, primary_key=True)
    processo_id = db.Column(db.ForeignKey("processos.id"))
    titulo = db.Column(db.String(60))
    descricao = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    dt_inicio = db.Column(db.Date, nullable=False)
    dt_fim = db.Column(db.Date)

    def __repr__(self):
        return f"<Etapa {self.titulo}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
