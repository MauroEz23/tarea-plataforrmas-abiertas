from flask import Blueprint, jsonify, request

# ESTA ES LA VARIABLE QUE BUSCA EL __init__.py (Asegúrate de que se llame así)
estudiantes_endpoints = Blueprint('estudiantes_endpoints', __name__)

@estudiantes_endpoints.route('/hola', methods=['GET'])
def hola():
    return jsonify("hola mundo"), 200

@estudiantes_endpoints.route('/saludo', methods=['GET'])
def saludar():
    data = request.get_json(silent=True)
    
    if not data or 'nombre' not in data:
        return jsonify({"error": "Debe de ingresar el nombre del estudiante."}), 400
    
    nombre = data.get('nombre')
    apellido = data.get('apellido', '')
    
    saludo = f"Hola {nombre} {apellido}".strip()
    
    return jsonify({"saludo": saludo}), 200