import mysql.connector
import sys

conexion = mysql.connector.connect(user='root', password="123456", host='localhost', database='rebobackub2', port='3306')
if not  conexion.is_connected():
    print("Error de conexion: ", conexion)
    sys.exit()
    
cursor = conexion.cursor()
cursor.execute("SELECT CodArt, Nombre, FecCreacion, FecModi FROM tblarticulos")

resultados = cursor.fetchall()

captured_data = []
for fila in resultados:
    # Capture each row into a list
    captured_data.append({
        'CodArt': fila[0],
        'Nombre': fila[1],
        'FecCreacion': fila[2],
        'FecModi': fila[3]
    })

    
cursor.close()
conexion.close()

print("Captured Data:")
for item in captured_data:
    CodArt = item['CodArt']
    Nombre = item['Nombre']
    FecCreacion = item['FecCreacion'].strftime('%Y-%m-%d %H:%M:%S') if item['FecCreacion'] else None
    FecModi = item['FecModi'].strftime('%Y-%m-%d %H:%M:%S') if item['FecModi'] else "No modificado"

    info = CodArt + '; ' + Nombre + '; ' + FecCreacion + '; ' + FecModi

    print(info)
    # print(item)

print(f"Número de filas obtenidas: {len(captured_data)}")
