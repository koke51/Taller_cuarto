from flask import Flask, render_template

app = Flask(__name__)

#vamos a importar lo necesario para los referenciales
from app.rutas.ciudad.ciudad_routes import ciudadmod
#se registran los modulos de referenciales
app.register_blueprint(app.rutas.ciudad.ciudad_routes, url_prefix="/ciudad")