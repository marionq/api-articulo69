from flask import Flask, request
import base64
from datetime import datetime
import requests
from flask_cors import CORS

from Consulta import Consulta

# app Flask
app = Flask(__name__)

# Configurar CORS para una ruta específica
CORS(app, resources={r"/*": {"origins": "*"}})

#zipkin = Zipkin(app, sample_rate=100)
#app.config['ZIPKIN_DSN'] = "http://10.14.102.132:9411/"

@app.route('/nafinapp/v1/consulta', methods = ['POST'])
def consulta_db():
    try:
        request_body = request.json
        consulta_rfc = Consulta().consulta(request_body['rfc'])

        return (consulta_rfc)
    except Exception as ex:
        return ex

def pagina_no_encontrada(error):
    return "<h1>La página a la que intentas acceder no existe....</h1>", 404


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(port=5000)
    app.run(host='0.0.0.0', debug=False)
