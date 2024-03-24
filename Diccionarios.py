# Crear el diccionario con información personal
informacion_personal = {
    "nombre": "Angel",
    "edad": 42,
    "ciudad": "Limón Indanza",
    "profesion": "Docente"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Puyo"

# Agregar una nueva clave-valor representando la profesión
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0960669008"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario resultante
print(informacion_personal)