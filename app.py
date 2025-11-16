from flask import Flask
from dominate import document
from dominate.tags import *

app = Flask(__name__)

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
        ]
    }
    
    # Criando documento HTML com Python
    doc = document(title=f"{data['nome']} - Currículo")
    
    with doc.head:
        meta(charset="UTF-8")
        meta(name="viewport", content="width=device-width, initial-scale=1.0")
        link(rel="stylesheet", href="/static/style.css")
        script(src="/static/animations.js", defer=True)
    
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
    
    return str(doc)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)