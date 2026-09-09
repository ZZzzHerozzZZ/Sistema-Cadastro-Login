from flask import Flask,render_template
from routes.auth import auth

app = Flask(__name__) 

app.register_blueprint(auth)

@app.route('/')
def pagina_cadastro():
    return render_template('cadastro.html')

if __name__ == "__main__":
    app.run()