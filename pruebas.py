from pykozo.pykozo import Html
from flask import Flask

app = Flask(__name__)

def button_component(text, **attrs):
    """Crea un botón reutilizable."""
    return Html().button(**attrs) << text  # Usa el operador << para el texto

@app.route('/')
def index():
    with Html() as doc:
        with doc.html():
            with doc.body():
                doc << button_component("Click me!", class_="btn-primary", id_="boton1")
    return doc.compile()

if __name__ == '__main__':
    app.run(debug=True,port=8001)