"""
Desafío 3 - Limpieza y preparación de datos
Ejercicio 1: Limpieza y Preparación de Datos con Guardado en un Archivo
Tienes un archivo CSV llamado "datos_brutos.csv" con datos que contienen nombres y
edades de personas. Tu objetivo es realizar las siguientes tareas:
Nombre,Edad
Alice,28
Bob,
Carol,45
David,32
Alice,30
Eve,,
1. Cargar los datos desde el archivo CSV.
2. Eliminar registros duplicados.
3. Eliminar registros con valores faltantes.
4. Calcular la edad promedio.
5. Guardar los datos limpios en un nuevo archivo CSV llamado "datos_limpios.csv".
"""
import csv

# 1. Cargar los datos desde el archivo CSV
datos = []
with open('datos_brutos.csv', 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv)
    encabezado = next(csv_reader)  # Leer la primera línea (encabezado)
    for fila in csv_reader:
        datos.append(fila)

# 2. Eliminar registros duplicados
datos_unicos = []
for fila in datos:
    if fila not in datos_unicos:
        datos_unicos.append(fila)

# 3. Eliminar registros con valores faltantes
datos_limpios = [fila for fila in datos_unicos if len(fila) > 1 and fila[1] != '']

# 4. Calcular la edad promedio
edades = [int(fila[1]) for fila in datos_limpios]
if edades:
    edad_promedio = sum(edades) / len(edades)
    print(f'Edad promedio: {edad_promedio}')
else:
    print('No hay edades válidas para calcular la edad promedio.')

# 5. Guardar los datos limpios en un nuevo archivo CSV llamado "datos_limpios.csv".
with open('datos_limpios.csv', 'w', newline='') as archivo_csv:
    csv_writer = csv.writer(archivo_csv)
    csv_writer.writerow(encabezado)  # Escribir el encabezado
    csv_writer.writerows(datos_limpios)

print('Datos limpios guardados en "datos_limpios.csv"')
