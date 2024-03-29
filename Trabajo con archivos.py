# Crear el archivo my_notes.txt y escribir algunas notas personales
with open('my_notes.txt', 'w') as file:
    file.write("Nota 1: Despertarse a las 6 am\n")
    file.write("Nota 2: Llevar a los niños al colegio\n")
    file.write("Nota 3: Ir al Gym\n")
    file.write("Nota 4: Prepararse para ir al trabajo\n")
    file.write("Nota 5: Rumbo al trabajo\n")
    file.write("Nota 6: Terminada la mañana\n")

# Abrir el archivo my_notes.txt en modo lectura
with open('my_notes.txt', 'r') as file:
    # Leer la primera línea
    line = file.readline()
    # Mientras haya líneas en el archivo
    while line:
        # Mostrar la línea en la consola
        print(line.strip())  # strip() para eliminar espacios en blanco adicionales y saltos de línea
        # Leer la siguiente línea
        line = file.readline()

# El archivo se cierra automáticamente al salir del bloque "with"