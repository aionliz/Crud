# Guía Pedagógica: Cómo Crear el Proyecto Citas Famosas desde Cero

Esta guía te enseña a construir paso a paso una aplicación web CRUD con Flask, Python y MySQL, usando la arquitectura Modelo-Vista-Controlador (MVC). ¡Ideal para aprender y practicar desarrollo profesional!

---

## 1. Crear la Estructura del Proyecto

Abre la terminal y ejecuta:

```bash
mkdir flask_citas_app
cd flask_citas_app
mkdir base
cd base
mkdir config controllers models static templates
cd ..
type nul > server.py
```

Tu estructura debe verse así:

```
flask_citas_app/
├── server.py
├── base/
│   ├── config/
│   ├── controllers/
│   ├── models/
│   ├── static/
│   ├── templates/
```

---

## 2. Crear y Activar el Entorno Virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Instalar Librerías Esenciales

```bash
pip install Flask PyMySQL Flask-Bcrypt
```

---

## 4. Configurar la Base de Datos en MySQL

1. Abre MySQL Workbench.
2. Crea el esquema `proyecto_crud`.
3. Crea las tablas:
   - `usuarios` (campos: id, nombre, apellido, email, password, creado_en, actualizado_en)
   - `citas` (campos: id, cita, autor_id, creado_en, actualizado_en)
   - `favoritos` (campos: id, usuario_id, cita_id)
4. Define las claves foráneas correctamente.

---

## 5. Crear la Conexión a MySQL

En `base/config/mysqlconnection.py`:

```python
import pymysql.cursors
class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host='localhost', user='root', password='TU_CONTRASEÑA', db=db,
            charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=False)
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, data)
            if query.lower().startswith('select'):
                return cursor.fetchall()
            self.connection.commit()
            return cursor.lastrowid

def connectToMySQL(db):
    return MySQLConnection(db)
```

---

## 6. Inicializar la Aplicación Flask

En `base/__init__.py`:

```python
from flask import Flask, render_template
from base.controllers import usuarios, citas
from datetime import datetime

def format_date(value, format='%Y-%m-%d'):
    if isinstance(value, str):
        value = datetime.strptime(value, '%Y-%m-%d')
    return value.strftime(format)

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev', DEBUG=True)
    app.register_blueprint(usuarios.bp)
    app.register_blueprint(citas.bp)
    app.add_template_filter(format_date, 'format_date')
    @app.route('/')
    def index():
        return render_template('auth.html')
    return app
```

En `server.py`:

```python
from base import create_app
app = create_app()
if __name__ == '__main__':
    app.run(port=3000)
```

---

## 7. Desarrollar los Módulos MVC

- **Modelos:** Crea la lógica de base de datos en `base/models/usuario_model.py` y `base/models/cita_model.py`.
- **Controladores:** Define las rutas y lógica en `base/controllers/usuarios.py` y `base/controllers/citas.py`.
- **Vistas:** Crea los templates HTML en `base/templates/` (`auth.html`, `dashboard.html`, `perfil.html`, etc.).

---

## 8. Implementar Funcionalidades

- Registro e inicio de sesión con validaciones y mensajes de error.
- CRUD de citas con validaciones.
- Botones de editar/remover solo para el usuario dueño.
- Página de perfil con citas y contador.
- Cerrar sesión.
- Marcar citas como favoritas y mostrarlas en tabla aparte.
- Remover favoritos y volver a mostrar en la lista general.

---

## 9. Ejecutar y Probar el Proyecto

Activa el entorno virtual y ejecuta:

```bash
python server.py
```

Abre tu navegador en:

```
http://127.0.0.1:3000
```

---

## 10. Buenas Prácticas

- Usa `pip freeze > requirements.txt` para mantener tus dependencias.
- Borra caché de Python con:

```bash
find . -name "__pycache__" -type d -exec rmdir /s /q {} +
```

- Documenta tu código y mantén la estructura.

---

¡Felicidades! Ahora sabes cómo crear el proyecto Citas Famosas desde cero, paso a paso y con buenas prácticas. Si tienes dudas, revisa los archivos y sigue la arquitectura propuesta.
