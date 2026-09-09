from flask import Blueprint, request, jsonify,render_template
from werkzeug.security import generate_password_hash, check_password_hash

from database.connection import conectar

auth = Blueprint('auth',  __name__ )

@auth.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    email = request.form['email']
    senha = request.form['senha']

    conexao = conectar()
    cursor = conexao.cursor()

    # -------------------------
    # Consulta os dados do usuário
    # -------------------------

    sql = """
            SELECT id,nome,email,senha
            From usuarios
            WHERE email = %s 
    """

    valores = (email,)

    cursor.execute(sql,valores)

    usuario = cursor.fetchone()

    # -------------------------
    # Fecha o cursor e a conexão com o banco
    # -------------------------

    cursor.close()
    conexao.close()

    # -------------------------
    # Verifica as credenciais do usuário
    # -------------------------

    if usuario and check_password_hash(usuario[3],senha):
        return jsonify({
            'mensagem': 'Login realizado',
            'usuario': usuario[1]
        })

    return jsonify({
        'mensagem': 'Email ou senha incorretos'
    })

    


@auth.route('/cadastro', methods=['POST'])
def cadastro():

    # -------------------------
    # Obtém os dados enviados pelo formulário
    # -------------------------

    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    data_nascimento = request.form['data_nascimento']

    senha_hash = generate_password_hash(senha)

    conexao = conectar()
    cursor = conexao.cursor()

    # -------------------------
    # Insere os dados do usuário no MySQL
    # -------------------------

    sql ="""
        INSERT INTO usuarios
        (nome, email, senha, data_nascimento)
        VALUES (%s,%s,%s,%s)
    """

    valores = (nome,email,senha_hash,data_nascimento)

    
    cursor.execute(sql,valores)

    # -------------------------
    # Executa a consulta para localizar o usuário pelo email
    # -------------------------
    
    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({
        'mensagem': 'cadastro realizado'
    })

    
   