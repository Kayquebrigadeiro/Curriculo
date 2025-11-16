from flask import Blueprint, render_template_string, request, redirect, url_for, flash, jsonify
from models import db, Profile, Educacao, Curso, Competencia, Contato

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def dashboard():
    total_contatos = Contato.query.count()
    contatos_nao_lidos = Contato.query.filter_by(lida=False).count()
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin - Currículo</title>
        <style>
            body { font-family: Arial; margin: 20px; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; }
            .card { background: white; padding: 20px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
            .stat { background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 20px; border-radius: 8px; text-align: center; }
            .nav { background: #2c3e50; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
            .nav a { color: white; text-decoration: none; margin-right: 20px; padding: 8px 16px; border-radius: 4px; }
            .nav a:hover { background: rgba(255,255,255,0.1); }
            h1 { color: #2c3e50; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎛️ Painel Administrativo</h1>
            
            <div class="nav">
                <a href="/admin">Dashboard</a>
                <a href="/admin/profile">Perfil</a>
                <a href="/admin/contatos">Contatos</a>
                <a href="/">Ver Site</a>
            </div>
            
            <div class="stats">
                <div class="stat">
                    <h3>{{ total_contatos }}</h3>
                    <p>Total de Contatos</p>
                </div>
                <div class="stat">
                    <h3>{{ contatos_nao_lidos }}</h3>
                    <p>Não Lidos</p>
                </div>
            </div>
            
            <div class="card">
                <h3>📊 Resumo</h3>
                <p>Bem-vindo ao painel administrativo do seu currículo digital!</p>
                <p>Aqui você pode gerenciar suas informações, ver mensagens de contato e atualizar seu perfil.</p>
            </div>
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(template, 
                                total_contatos=total_contatos,
                                contatos_nao_lidos=contatos_nao_lidos)

@admin.route('/contatos')
def contatos():
    contatos = Contato.query.order_by(Contato.data_envio.desc()).all()
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contatos - Admin</title>
        <style>
            body { font-family: Arial; margin: 20px; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; }
            .card { background: white; padding: 20px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .nav { background: #2c3e50; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
            .nav a { color: white; text-decoration: none; margin-right: 20px; padding: 8px 16px; border-radius: 4px; }
            .nav a:hover { background: rgba(255,255,255,0.1); }
            .contato { border-left: 4px solid #3498db; margin: 10px 0; }
            .contato.nao-lida { border-left-color: #e74c3c; background: #fdf2f2; }
            .meta { color: #666; font-size: 0.9em; margin-bottom: 10px; }
            h1 { color: #2c3e50; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📧 Mensagens de Contato</h1>
            
            <div class="nav">
                <a href="/admin">Dashboard</a>
                <a href="/admin/profile">Perfil</a>
                <a href="/admin/contatos">Contatos</a>
                <a href="/">Ver Site</a>
            </div>
            
            {% for contato in contatos %}
            <div class="card contato {% if not contato.lida %}nao-lida{% endif %}">
                <div class="meta">
                    <strong>{{ contato.nome }}</strong> ({{ contato.email }}) - {{ contato.data_envio.strftime('%d/%m/%Y %H:%M') }}
                    {% if not contato.lida %}<span style="color: #e74c3c;">● Não lida</span>{% endif %}
                </div>
                <h4>{{ contato.assunto }}</h4>
                <p>{{ contato.mensagem }}</p>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(template, contatos=contatos)