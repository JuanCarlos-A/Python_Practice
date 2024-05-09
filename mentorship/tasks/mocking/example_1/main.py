def obtener_nombres_usuarios(db):
            resultado = db.query('SELECT id, nombre FROM usuarios')
            return [usuario['nombre'] for usuario in resultado]