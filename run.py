from flask import Flask
from app.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    print("App iniciando...")
    app.run(debug=True)