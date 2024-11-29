from flask import Flask, render_template
from controllers.animals_controller import animals_bp 
import os


app = Flask(__name__, template_folder='views')


# Importa y registra los blueprints de los controladores
app.register_blueprint(animals_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


