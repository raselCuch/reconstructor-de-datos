import mysql.connector
import sys

conexion = mysql.connector.connect(user='root', password="123456", host='localhost', database='rebobackub', port='3306')
if not  conexion.is_connected():
    print("Error de conexion: ", conexion)
    sys.exit()
# print("Conexión exitosa a la base de datos.") hay 530 registros
    
cursor = conexion.cursor()
cursor.execute("SELECT IdVenta ,Fecha ,Cliente ,TipDocCli ,Doc ,Serie ,Numero ,TMoneda ,NPedido ,TCambio ,TVenta ,NDias ,FVence ,TBruto ,TExonerada ,TInafecta ,TGratuita ,TIgv ,Total ,TEst ,Est ,Empresa ,Almacen ,Vendedor ,Usuario ,FecCreacion ,UserCreacion ,FecModi ,UserModi ,EGratuita ,TComp ,Dcto ,ResumenFirma ,Cort ,TipoPago ,IdCajaApert ,TipoPago2 ,MontoPago2 ,CantArt"+
               " FROM tblventa")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

print(f"Número de filas obtenidas: {len(resultados)}")

# IdVenta ,Fecha ,Cliente ,TipDocCli ,Doc ,Serie ,Numero ,TMoneda ,NPedido ,TCambio ,TVenta ,NDias ,FVence ,TBruto ,TExonerada ,TInafecta ,TGratuita ,TIgv ,Total ,TEst ,Est ,Empresa ,Almacen ,Vendedor ,Usuario ,ArchXml ,NomArchXml ,FecCreacion ,UserCreacion ,FecModi ,UserModi ,EGratuita ,TComp ,Dcto ,ArchivoXml ,ResumenFirma ,ValorFirma ,Cort ,TipoPago ,IdCajaApert ,TipoPago2 ,MontoPago2 ,CantArt