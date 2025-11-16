from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    nascimento = db.Column(db.String(50), nullable=False)
    github = db.Column(db.String(200), nullable=False)
    resumo = db.Column(db.Text, nullable=False)

class Educacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    curso = db.Column(db.String(200), nullable=False)
    instituicao = db.Column(db.String(200), nullable=False)
    periodo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    periodo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

class Competencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.Integer, nullable=False)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    assunto = db.Column(db.String(200), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)
    lida = db.Column(db.Boolean, default=False)