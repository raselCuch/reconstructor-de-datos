import mysql.connector
import sys

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

###################################################################

query = 'SELECT CodArt, Nombre, PVenta, UserModi FROM tblarticulos_rebo2'
cursor.execute(query)
resultados_2 = cursor.fetchall()

captured_data_2 = []
for fila in resultados_2:
    captured_data_2.append({
        'CodArt': fila[0],
        'Nombre': fila[1],
        'Precio': fila[2],
        'UserModi': fila[3],
    })

cursor.close()
conexion.close()


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
        UserModi_2 = item_2['UserModi']

        UserModi_2_No_Null = str(UserModi_2) if UserModi_2 is not None else "Null"
        Precio_2_Str = str(Precio_2)

        if CodArt_1 == CodArt_2:
            if Nombre_1 != Nombre_2: # si los nombres son diferente 
                i = i + 1
                txt1 = '[' + CodArt_1 +'] ' + Nombre_1 + ' ------------------- ' + '[' + CodArt_2 + '] ' + Nombre_2 + " ------------------- userModi: " + UserModi_2_No_Null
                txt1 = '' + CodArt_1 +';' + Nombre_1 + ';' + CodArt_2+ ";" + Nombre_2 + ";" + UserModi_2_No_Null
                print(txt1)

        Nombre_1_1 = Nombre_1.replace(' ', '') 
        Nombre_2_1 = Nombre_2.replace(' ', '') 

        # if Nombre_1 == Nombre_2: # si los nombres son diferente 
        #     txt1 = '' + CodArt_1 +';' + Nombre_1 + ';' + CodArt_2+ ";" + Nombre_2 + ";" + UserModi_2_No_Null
        #     print(txt1)
        #     print("coinside")

        #     print("coinside")

print(i)