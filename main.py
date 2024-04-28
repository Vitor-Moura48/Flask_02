from flask import Flask
from configuracao import configurar_tudo

app = Flask(__name__)


configurar_tudo(app)


app.run(debug=True)