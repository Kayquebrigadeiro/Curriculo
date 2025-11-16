from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
from dominate import document
from dominate.tags import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seu-secret-key-aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///curriculo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    github = db.Column(db.String(200), nullable=False)
    resumo = db.Column(db.Text, nullable=False)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    assunto = db.Column(db.String(200), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

# API Routes
@app.route('/api/contato', methods=['POST'])
def enviar_contato():
    data = request.get_json()
    
    contato = Contato(
        nome=data['nome'],
        email=data['email'],
        assunto=data['assunto'],
        mensagem=data['mensagem']
    )
    
    db.session.add(contato)
    db.session.commit()
    
    return jsonify({'message': 'Mensagem enviada com sucesso!'}), 201

@app.route('/admin')
def admin():
    contatos = Contato.query.all()
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin - Contatos</title>
        <style>
            body { font-family: Arial; margin: 20px; background: #f5f5f5; }
            .container { max-width: 1000px; margin: 0 auto; }
            .card { background: white; padding: 20px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; }
            .contato { border-left: 4px solid #3498db; }
            .meta { color: #666; margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📧 Mensagens Recebidas</h1>
            <a href="/" style="color: #3498db;">← Voltar ao site</a>
            
            {% for contato in contatos %}
            <div class="card contato">
                <div class="meta"><strong>{{ contato.nome }}</strong> ({{ contato.email }})</div>
                <h4>{{ contato.assunto }}</h4>
                <p>{{ contato.mensagem }}</p>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(template, contatos=contatos)

@app.route('/')
def home():
    # Dados do currículo
    data = {
        'nome': 'Kayque Gregorio',
        'cargo': 'Estudante de Informática',
        'email': 'gregoriokayque352@gmail.com',
        'telefone': '+55 11 98058-4791',
        'endereco': 'Rua Mar de Ross, Parque Ribeiro de Lima, Barueri - SP',
        'nascimento': '25 de abril de 2008',
        'github': 'https://github.com/Kayquebrigadeiro/Curriculo.git',
        'resumo': 'Estudante de Informática com extrema vontade de aprender e trabalhar na área de tecnologia. Sociável, comprometido, responsável e comunicativo, com pensamento lógico e resiliência.',
        'educacao': [
            {
                'curso': 'Cursando Informática',
                'instituicao': 'FIEB TECH, Barueri',
                'periodo': 'fev 2024 – atual',
                'descricao': 'Desenvolvimento de aplicações web utilizando HTML, CSS e JavaScript. Framework React e T-SQL intermediário.'
            }
        ],
        'cursos': [
            {
                'nome': 'Programação e Desenvolvimento Web',
                'periodo': 'set 2024',
                'descricao': 'Desenvolvimento de páginas web utilizando HTML e CSS com foco em design e usabilidade.'
            },
            {
                'nome': 'Linguagem de Programação Python',
                'periodo': 'nov 2025',
                'descricao': 'Domínio dos conceitos básicos de Python, orientação a objetos e desenvolvimento de projetos práticos.'
            },
            {
                'nome': 'Soluções de IA no GitHub',
                'periodo': 'atual',
                'descricao': 'Estudo e aplicação de soluções baseadas em inteligência artificial disponíveis no GitHub.'
            },
            {
                'nome': 'AIF-C01: Praticante de IA Certificado pela AWS',
                'periodo': 'atual',
                'descricao': 'Desenvolvimento de soluções de IA utilizando AWS SageMaker para modelagem e treinamento.'
            }
        ],
        'competencias': [
            {'nome': 'Lógica de Programação', 'nivel': 4},
            {'nome': 'HTML', 'nivel': 4},
            {'nome': 'CSS', 'nivel': 3},
            {'nome': 'Desenvolvimento Web', 'nivel': 3},
            {'nome': 'Programação Python', 'nivel': 3},
            {'nome': 'Criação de Páginas Web', 'nivel': 3}
        ],
        'idiomas': [
            {'idioma': 'Português', 'nivel': 'Nativo'},
            {'idioma': 'Inglês', 'nivel': 'Iniciante'}
        ],
        'qualidades': [
            'Extrema vontade de aprender e trabalhar na área',
            'Sociável, comprometido, responsável e comunicativo',
            'Pensamento lógico e resiliência'
        ],
        'projetos': [
            {
                'nome': 'Currículo Digital Interativo',
                'tecnologias': ['Python', 'Flask', 'HTML/CSS', 'JavaScript'],
                'descricao': 'Site de currículo desenvolvido em Python com animações CSS, formulário de contato funcional e painel administrativo.',
                'github': 'https://github.com/Kayquebrigadeiro/Curriculo',
                'status': 'Concluído'
            },
            {
                'nome': 'Sistema de Gestão Web',
                'tecnologias': ['HTML', 'CSS', 'JavaScript', 'React'],
                'descricao': 'Aplicação web responsiva para gestão de dados com interface moderna e funcionalidades CRUD.',
                'github': '#',
                'status': 'Em desenvolvimento'
            },
            {
                'nome': 'Bot de Automação',
                'tecnologias': ['Python', 'APIs', 'Selenium'],
                'descricao': 'Automação de tarefas repetitivas com integração de APIs e web scraping para otimização de processos.',
                'github': '#',
                'status': 'Planejado'
            }
        ]
    }
    
    # Criando documento HTML com Python
    doc = document(title=f"{data['nome']} - Currículo")
    
    with doc.head:
        meta(charset="UTF-8")
        meta(name="viewport", content="width=device-width, initial-scale=1.0")
        link(rel="stylesheet", href="/static/style.css")
        script(src="/static/animations.js", defer=True)
        script(src="/static/contact.js", defer=True)
    
    with doc:
        with div(cls="container"):
            # Header
            with header():
                with div(cls="profile-section"):
                    with div(cls="profile-avatar"):
                        with div(cls="avatar-circle"):
                            span("KG", cls="initials")
                    
                    with div(cls="profile-info"):
                        h1(data['nome'])
                        h2(data['cargo'])
                        
                        with div(cls="contact-grid"):
                            with div(cls="contact-item"):
                                i("📧", cls="icon")
                                span(data['email'])
                            
                            with div(cls="contact-item"):
                                i("📱", cls="icon")
                                span(data['telefone'])
                            
                            with div(cls="contact-item"):
                                i("📍", cls="icon")
                                span(data['endereco'])
                            
                            with div(cls="contact-item"):
                                i("📅", cls="icon")
                                span(data['nascimento'])
                            
                            with div(cls="contact-item"):
                                i("💻", cls="icon")
                                a("GitHub Portfolio", href=data['github'], target="_blank", cls="github-link")
            
            # Resumo
            with section(cls="resumo"):
                h3("Resumo Profissional")
                p(data['resumo'])
            
            # Educação
            with section(cls="educacao"):
                h3("Formação Acadêmica")
                for edu in data['educacao']:
                    with div(cls="item"):
                        h4(edu['curso'])
                        p(f"{edu['instituicao']} | {edu['periodo']}", cls="instituicao")
                        p(edu['descricao'], cls="descricao")
            
            # Cursos
            with section(cls="cursos"):
                h3("Cursos e Certificações")
                for curso in data['cursos']:
                    with div(cls="item"):
                        h4(curso['nome'])
                        p(curso['periodo'], cls="periodo")
                        p(curso['descricao'], cls="descricao")
            
            # Competências
            with section(cls="competencias"):
                h3("Competências Técnicas")
                with div(cls="skills-grid"):
                    for comp in data['competencias']:
                        with div(cls="skill-item"):
                            span(comp['nome'], cls="skill-name")
                            with div(cls="skill-bar"):
                                div(cls="skill-level", style=f"width: {comp['nivel'] * 20}%")
            
            # Projetos
            with section(cls="projetos"):
                h3("💻 Projetos")
                with div(cls="projetos-grid"):
                    for projeto in data['projetos']:
                        with div(cls="projeto-card"):
                            with div(cls="projeto-header"):
                                h4(projeto['nome'])
                                span(projeto['status'], cls=f"status {projeto['status'].lower().replace(' ', '-')}")
                            
                            p(projeto['descricao'], cls="projeto-desc")
                            
                            with div(cls="tecnologias"):
                                for tech in projeto['tecnologias']:
                                    span(tech, cls="tech-tag")
                            
                            with div(cls="projeto-links"):
                                if projeto['github'] != '#':
                                    a("🔗 Ver no GitHub", href=projeto['github'], target="_blank", cls="projeto-link")
                                else:
                                    span("🔒 Em breve", cls="projeto-link disabled")
            
            # Idiomas
            with section(cls="idiomas"):
                h3("Idiomas")
                for idioma in data['idiomas']:
                    with div(cls="idioma-item"):
                        strong(f"{idioma['idioma']}:")
                        span(f" {idioma['nivel']}")
            
            # Qualidades
            with section(cls="qualidades"):
                h3("Qualidades Pessoais")
                with ul(cls="qualidades-list"):
                    for qualidade in data['qualidades']:
                        li(qualidade)
            
            # Formulário de contato
            with section(cls="contato-form"):
                h3("Entre em Contato")
                with form(id="contact-form"):
                    with div(cls="form-group"):
                        input_(type="text", id="nome", placeholder="Seu nome", required=True)
                    with div(cls="form-group"):
                        input_(type="email", id="email", placeholder="Seu email", required=True)
                    with div(cls="form-group"):
                        input_(type="text", id="assunto", placeholder="Assunto", required=True)
                    with div(cls="form-group"):
                        textarea(id="mensagem", placeholder="Sua mensagem", rows="5", required=True)
                    button("Enviar Mensagem", type="submit", cls="btn-submit")
                
                div(id="form-message", cls="form-message")
    
    return str(doc)

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='127.0.0.1', port=5000)