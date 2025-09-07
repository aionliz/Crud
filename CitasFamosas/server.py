# server.py

from base import create_app

app = create_app()


app = create_app()

# Punto de entrada principal de la aplicación Flask
# Crea la instancia de la app y la ejecuta.

if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug para desarrollo
    app.run(port=3000, debug=True)
