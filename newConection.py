import mysql.connector
import sys

conexion = mysql.connector.connect(user='root', password="123Server", 
                                   host='localhost', database='dbLocal', 
                                   port='3307')

if not  conexion.is_connected():
    print("Error de conexion: ", conexion)
    sys.exit()

cursor = conexion.cursor()

query = 'SELECT CodArt, Nombre FROM tblarticulos_rebo1'
# query = 'SELECT CodArt, Nombre FROM tblarticulos_rebo2'
cursor.execute(query)
resultados_1 = cursor.fetchall()

captured_data_1 = []
for fila in resultados_1:
    captured_data_1.append({
        'CodArt': fila[0],
        'Nombre': fila[1]
    })

# for item in captured_data_1:
#     CodArt = item['CodArt']
#     Nombre = item['Nombre']

    # info = CodArt + '; ' + Nombre
    # print(info)

print('cantidad de datos', len(captured_data_1))

###################################################################

cursor = conexion.cursor()

# query = 'SELECT CodArt, Nombre FROM tblarticulos_rebo1'
query = 'SELECT CodArt, Nombre FROM tblarticulos_rebo2'
cursor.execute(query)
resultados_2 = cursor.fetchall()

captured_data_2 = []
for fila in resultados_2:
    captured_data_2.append({
        'CodArt': fila[0],
        'Nombre': fila[1]
    })

    
cursor.close()
conexion.close()

# for item in captured_data_2:
#     CodArt = item['CodArt']
#     Nombre = item['Nombre']

    # info = CodArt + '; ' + Nombre
    # print(info)

print('cantidad de datos', len(captured_data_2))