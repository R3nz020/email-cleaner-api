from flask import Flask
from app.routes import routes
import os

app = Flask(__name__)

print("Antes de registrar el blueprint")
app.register_blueprint(routes)
print("Después de registrar el blueprint")

# ✅ Endpoint directo para prueba
@app.route("/direct-test", methods=["GET"])
def direct_test():
    return {"mensaje": "✅ Endpoint directo funcionando"}

if __name__ == '__main__':
    print('App iniciando...')
    app.run(host='0.0.0.0', port=5000, debug=True)