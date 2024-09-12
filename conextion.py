import mysql.connector
import sys

# conexion = mysql.connector.connect(user='root', password="123456", host='localhost', database='rebobackub2', port='3306')
conexion = mysql.connector.connect(user='root', password="Server123", host='26.23.122.162', database='bdrebomarket', port='3306')
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

# print("Captured Data:")
for item in captured_data:
    CodArt = item['CodArt']
    Nombre = item['Nombre']
    # FecCreacion = item['FecCreacion'].strftime('%Y-%m-%d %H:%M:%S') if item['FecCreacion'] else None
    # FecModi = item['FecModi'].strftime('%Y-%m-%d %H:%M:%S') if item['FecModi'] else "No modificado"
    FecCreacion = item['FecCreacion'].date().strftime('%Y-%m-%d') if item['FecCreacion'] else None
    HoraCreacion = item['FecCreacion'].time().strftime('%H:%M:%S') if item['FecCreacion'] else None

    FecModi = item['FecModi'].date().strftime('%Y-%m-%d') if item['FecModi'] else "No modificado"
    HoraModi = item['FecModi'].time().strftime('%H:%M:%S') if item['FecModi'] else ""

    info = CodArt + '; ' + Nombre + '; ' + FecCreacion+ '    ' + HoraCreacion + '; ' + FecModi + '    ' + HoraModi

    print(info)
    # print(item)

print(f"Número de filas obtenidas: {len(captured_data)}")
