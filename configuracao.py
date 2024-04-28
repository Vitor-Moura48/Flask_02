from routes.cliente import cliente_route
from routes.home import home_route
from database.database import db
from database.models.cliente import Cliente

def configurar_tudo(app):
    configurar_rotas(app)
    configurar_banco()

def configurar_rotas(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')

def configurar_banco():
    db.connect()
    db.create_tables([Cliente])