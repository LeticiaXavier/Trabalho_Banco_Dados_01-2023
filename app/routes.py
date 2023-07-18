from app import app
from flask import render_template, g, request
from flaskext.mysql import MySQL

# Configuração do banco de dados
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Abc753951*fuiska'
app.config['MYSQL_DATABASE_DB'] = 'banco_geral'

mysql = MySQL()
mysql.init_app(app)


def get_db():
    if 'db' not in g:
        g.db = mysql.connect()
    return g.db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


def inserir_dados(nome, matricula, curso, email, senha):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO banco_geral (nome, matricula, curso, email, senha) VALUES (%s, %s, %s, %s, %s)", (nome, matricula, curso, email, senha))
    conn.commit()
    cursor.close()


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['Nome']
        matricula = request.form['Matricula']
        curso = request.form['Curso']
        email = request.form['Email']
        senha = request.form['Senha']
    
        inserir_dados(nome, matricula, curso, email, senha)
    
        # Outras ações após a inserção (redirecionar, exibir mensagem, etc.)
    
    variavel = "Valor dinâmico"
    return render_template('/cadastro.html', variavel=variavel)


@app.route('/login')
def login():
    variavel = "Valor dinâmico"
    return render_template('/login.html', variavel=variavel)


@app.route('/home')
def home():
    variavel = "Valor dinâmico"
    return render_template('/home.html', variavel=variavel)


if __name__ == '__main__':
    app.run(debug=True)
