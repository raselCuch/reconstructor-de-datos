import mysql.connector
import sys
import difflib

def comparar_strings(s1, s2):
    ratio = difflib.SequenceMatcher(None, s1, s2).ratio()

    # txt1 = s1 + ' - ' + s2 + 'Coincidencia encontrada'
    # print(txt1)
    
    return ratio * 100

conexion = mysql.connector.connect(user='root', password="123Server", 
                                   host='localhost', database='dbLocal', 
                                   port='3307')

if not  conexion.is_connected():
    print("Error de conexion: ", conexion)
    sys.exit()

cursor = conexion.cursor()

query = 'SELECT CodArt, Nombre, PVenta FROM tblarticulos_rebo1'
cursor.execute(query)
resultados_1 = cursor.fetchall()

captured_data_1 = []
for fila in resultados_1:
    captured_data_1.append({
        'CodArt': fila[0],
        'Nombre': fila[1],
        'Precio': fila[2]
    })

# print('cantidad de datos', len(captured_data_1))

###################################################################

query = 'SELECT CodArt, Nombre, PVenta FROM tblarticulos_rebo2'
cursor.execute(query)
resultados_2 = cursor.fetchall()

captured_data_2 = []
for fila in resultados_2:
    captured_data_2.append({
        'CodArt': fila[0],
        'Nombre': fila[1],
        'Precio': fila[2]
    })

cursor.close()
conexion.close()



# print('cantidad de datos', len(captured_data_2))

i = 0
for item_1 in captured_data_1:
    CodArt_1 = item_1['CodArt']
    Nombre_1 = item_1['Nombre']
    Precio_1 = item_1['Precio']
    Precio_1_Str = str(Precio_1)

    for item_2 in captured_data_2:
        CodArt_2 = item_2['CodArt']
        Nombre_2 = item_2['Nombre']
        Precio_2 = item_2['Precio']
        Precio_2_Str = str(Precio_2)

        # if Nombre_1 == Nombre_2:
        similitud = comparar_strings(Nombre_1, Nombre_2)
        if similitud >= 80 and abs(Precio_1 - Precio_2) < 10:
            i = i + 1
            print()
            print(f'Similitud: {similitud:.2f}%')

            txt1 = '[' + CodArt_1 +'] ' + Nombre_1 + ' {' + Precio_1_Str +'} ------------------- ' + '[' + CodArt_2 + '] ' + Nombre_2 + ' {'+ Precio_2_Str + "}"
            print(txt1)
            
        # else:
        #     print('La similitud es menor al 50%.')



        # txt = Nombre_1 + ' - ' + Nombre_2
        # print(txt)


print(i)