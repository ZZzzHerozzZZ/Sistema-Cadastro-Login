🔐 Sistema de Cadastro e Login

Projeto pessoal desenvolvido para fins de aprendizado, implementando um sistema completo de cadastro e autenticação de usuários, com persistência de dados em banco MySQL.

🧱 Tecnologias utilizadas
Python
Flask
MySQL
✨ Funcionalidades
Cadastro de novos usuários
Autenticação (login) de usuários
Armazenamento e validação dos dados no banco de dados MySQL
Hash de senhas para armazenamento seguro

📁 Estrutura do projeto
backend/
├── config/              # Configurações da aplicação
├── database/
│   └── connection.py    # Conexão com o banco de dados MySQL
├── routes/
│   └── auth.py          # Rotas de autenticação (login/cadastro)
├── static/
│   └── css/
│       ├── cadastro.css
│       └── style.css
├── templates/
│   ├── cadastro.html
│   └── login.html
├── .env                 # Variáveis de ambiente (credenciais do banco, etc.)
├── .gitignore
├── app.py               # Ponto de entrada da aplicação Flask
└── README.md
