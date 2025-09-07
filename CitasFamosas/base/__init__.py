# base/__init__.py

from flask import Flask, render_template
from datetime import datetime

# Importar controladores como Blueprints
from base.controllers import usuarios, citas

# Definir un filtro de Jinja2 para formatear fechas
def format_date(value, format='%Y-%m-%d'):
    if isinstance(value, str):
        value = datetime.strptime(value, '%Y-%m-%d')
    return value.strftime(format)

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
    )

    # Registrar los Blueprints
    app.register_blueprint(usuarios.bp)
    app.register_blueprint(citas.bp)
    
    # Registrar el filtro de fecha en la aplicación
    app.add_template_filter(format_date, 'format_date')

    @app.route('/')
    def index():
        return render_template('auth.html')

    return app