from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Asegúrate de que el directorio de subidas existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def procesar_urls(archivo):
    urls_unicas = set()

    # Abrir el archivo de manera eficiente para leer línea por línea
    with open(archivo, 'r') as file:
        for url in (line.strip() for line in file):
            if 'shop' in url and url.endswith('.html'):
                urls_unicas.add(url)

    return urls_unicas

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verificar si el archivo fue enviado
        if 'file' not in request.files:
            return "No se subió ningún archivo", 400
        
        file = request.files['file']

        # Verificar si el archivo tiene un nombre
        if file.filename == '':
            return "Nombre de archivo no válido", 400

        # Guardar el archivo
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Procesar el archivo y obtener las URLs válidas
        urls_validas = procesar_urls(file_path)

        # Mostrar las URLs filtradas en la página
        return render_template('result.html', urls=urls_validas)

    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
