from flask import Blueprint, jsonify, request

estudiantes_endpoints = Blueprint('estudiantes_endpoints', __name__)

# --- PRÁCTICA 2 ---
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


# --- PRÁCTICA 3: MÉTODOS HTTP ---

# 1. GET: Obtener todos los estudiantes
@estudiantes_endpoints.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    # Simulamos una lista de estudiantes
    return jsonify({
        "mensaje": "Lista de estudiantes obtenida correctamente.",
        "estudiantes": ["Ana", "Carlos", "Maria"]
    }), 200

# 2. POST: Agregar un estudiante
@estudiantes_endpoints.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    data = request.get_json(silent=True)
    
    # Validamos que envíen el nombre
    if not data or 'nombre' not in data:
        return jsonify({"error": "Debe de ingresar el nombre del estudiante."}), 400
    
    nombre = data.get('nombre')
    
    return jsonify({
        "mensaje": "Estudiante agregado correctamente.",
        "estudiante": nombre
    }), 201 # 201 significa "Created" (Creado)

# 3. PUT: Actualizar un estudiante
@estudiantes_endpoints.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    data = request.get_json(silent=True)
    
    if not data or 'nombre' not in data:
        return jsonify({"error": "Debe de ingresar el nombre del estudiante."}), 400
    
    # Simulamos la actualización usando el ID que viene en la URL
    return jsonify({
        "mensaje": "Estudiante actualizado correctamente.",
        "id": id
    }), 200

# 4. DELETE: Eliminar un estudiante
@estudiantes_endpoints.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    # Simulamos la eliminación usando el ID
    return jsonify({
        "mensaje": "Estudiante eliminado correctamente.",
        "id": id
    }), 200