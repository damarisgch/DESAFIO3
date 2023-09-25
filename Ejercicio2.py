"""
Ejercicio 2: Limpieza y Preparación de Datos con Guardado en un Archivo
Tienes un archivo CSV llamado "ventas.csv" con los siguientes datos:
Fecha,Producto,Ventas
2023-01-01,A,100
2023-01-01,B,150
2023-01-02,A,120
2023-01-02,B,130
2023-01-03,A,80
2023-01-03,B,
1. Cargar los datos desde el archivo CSV.
2. Eliminar registros con valores faltantes en la columna "Ventas".
3. Convertir la columna "Fecha" al formato de fecha adecuado.
4. Calcular la suma total de ventas por producto.
5. Calcular el promedio de ventas por día.
6. Guardar los datos procesados en un nuevo archivo CSV llamado "ventas_procesadas.csv".
"""
import csv
from datetime import datetime

# almacenar los datos en listas
fechas = []
productos = []
ventas = []

# 1.Cargar los datos desde el archivo CSV.
with open('ventas.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    
    cabecera = next(lector)  # Lee la primera línea (encabezado)
    
    for fila in lector:
        # 2. 3. puntos 
        if len(fila) == 3:
            fecha_str, producto, venta_str = fila
            try:
                fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
                venta = int(venta_str)
                fechas.append(fecha)
                productos.append(producto)
                ventas.append(venta)
            except ValueError:
                # Ignorar filas con valores incorrectos
                pass

# 4. Calcular la suma total de ventas por producto
ventas_por_producto = {}
for i in range(len(productos)):
    producto = productos[i]
    venta = ventas[i]
    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0
    ventas_por_producto[producto] += venta

# 5. Calcular el promedio de ventas por día
ventas_por_dia = {}
for i in range(len(fechas)):
    fecha = fechas[i].date()
    venta = ventas[i]
    if fecha not in ventas_por_dia:
        ventas_por_dia[fecha] = []
    ventas_por_dia[fecha].append(venta)

promedio_ventas_por_dia = {}
for fecha, ventas_diarias in ventas_por_dia.items():
    promedio = sum(ventas_diarias) / len(ventas_diarias)
    promedio_ventas_por_dia[fecha] = promedio

# 6. Guardar los datos procesados en un nuevo archivo CSV llamado "ventas_procesadas.csv".
with open('ventas_procesadas.csv', 'w', newline='') as archivo_salida:
    escritor = csv.writer(archivo_salida)
    escritor.writerow(['Fecha', 'Producto', 'Ventas'])
    for i in range(len(fechas)):
        fecha = fechas[i].strftime('%Y-%m-%d')
        producto = productos[i]
        venta = ventas[i]
        escritor.writerow([fecha, producto, venta])
