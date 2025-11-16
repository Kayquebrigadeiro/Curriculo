from flask import Blueprint, jsonify, request
from models import db, Profile, Educacao, Curso, Competencia, Contato

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/profile', methods=['GET'])
def get_profile():
    profile = Profile.query.first()
    if not profile:
        return jsonify({'error': 'Profile not found'}), 404
    
    return jsonify({
        'nome': profile.nome,
        'cargo': profile.cargo,
        'email': profile.email,
        'telefone': profile.telefone,
        'endereco': profile.endereco,
        'nascimento': profile.nascimento,
        'github': profile.github,
        'resumo': profile.resumo
    })

@api.route('/educacao', methods=['GET'])
def get_educacao():
    educacao = Educacao.query.all()
    return jsonify([{
        'id': e.id,
        'curso': e.curso,
        'instituicao': e.instituicao,
        'periodo': e.periodo,
        'descricao': e.descricao
    } for e in educacao])

@api.route('/cursos', methods=['GET'])
def get_cursos():
    cursos = Curso.query.all()
    return jsonify([{
        'id': c.id,
        'nome': c.nome,
        'periodo': c.periodo,
        'descricao': c.descricao
    } for c in cursos])

@api.route('/competencias', methods=['GET'])
def get_competencias():
    competencias = Competencia.query.all()
    return jsonify([{
        'id': c.id,
        'nome': c.nome,
        'nivel': c.nivel
    } for c in competencias])

@api.route('/contato', methods=['POST'])
def enviar_contato():
    data = request.get_json()
    
    if not all(k in data for k in ['nome', 'email', 'assunto', 'mensagem']):
        return jsonify({'error': 'Dados incompletos'}), 400
    
    contato = Contato(
        nome=data['nome'],
        email=data['email'],
        assunto=data['assunto'],
        mensagem=data['mensagem']
    )
    
    db.session.add(contato)
    db.session.commit()
    
    return jsonify({'message': 'Mensagem enviada com sucesso!'}), 201

@api.route('/contatos', methods=['GET'])
def get_contatos():
    contatos = Contato.query.order_by(Contato.data_envio.desc()).all()
    return jsonify([{
        'id': c.id,
        'nome': c.nome,
        'email': c.email,
        'assunto': c.assunto,
        'mensagem': c.mensagem,
        'data_envio': c.data_envio.isoformat(),
        'lida': c.lida
    } for c in contatos])