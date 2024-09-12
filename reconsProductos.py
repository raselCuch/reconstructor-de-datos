from pathlib import Path
import xml.etree.ElementTree as ET
import xmltodict, json

path = Path("./xml")
iContador = 0
iContadorUnicos = 0
iContadorCantidadProductosVendidos = 0
productos_unicos = set()  # Crear un conjunto para almacenar los códigos únicos

for file in path.rglob('*'):
    if file.is_file():
        file_str = str(file)
        caracteres_a_reemplazar = '\\'
        xml_file = file_str.replace(caracteres_a_reemplazar, '/')
        # print("------------------------------- archivo: "+"./"+xml_file + "\n")
        xml_file = open(xml_file)
        obj = xml_file.read()  # Extrae en bruto el XML
        cleaned_xml = obj.replace('ï»¿', '')  # Elimina caracteres innecesarios
        obj2 = xmltodict.parse(cleaned_xml)  # Convierte el string a XML dict
        json_str = json.dumps(obj2, indent=4)
        newObj = json.loads(json_str)  # Convierte el dict en JSON
        obje = newObj['Invoice']  # Base
        CantArt = obje['cbc:LineCountNumeric']
        numero = int(CantArt)
        for i in range(numero):
            iContador = iContador + 1
            Numero = obje['cac:Signature']['cbc:ID']
            invoice_line = obje['cac:InvoiceLine'][i] if numero > 1 else obje['cac:InvoiceLine'] ###
            
            Codigo = invoice_line['cac:Item']['cac:SellersItemIdentification']['cbc:ID']
            nombre = invoice_line['cac:Item']['cbc:Description']
            
            PVenta = invoice_line['cac:PricingReference']['cac:AlternativeConditionPrice']['cbc:PriceAmount']['#text']
            Cantidad = invoice_line['cbc:InvoicedQuantity']['#text'].split('.')[0]

            PVentaN = float(PVenta)  # Convertir a float para manejar decimales
            CantidadN = int(Cantidad)  # Convertir a entero
            iContadorCantidadProductosVendidos = iContadorCantidadProductosVendidos + CantidadN 

            if PVentaN.is_integer():
                PVentaN_str = str(int(PVentaN))  # Convertir a entero y luego a string
            else:
                PVentaN_str = str(PVentaN)  # Mantener como flo

            Importe = PVentaN * CantidadN
            if Importe.is_integer():
                Importe_str = str(int(Importe))  # Convertir a entero y luego a string
            else:
                Importe_str = str(Importe)  # Mantener como float

            # print('Codigo: ', Codigo)
            # print('nombre: ', nombre)
            # print('PVentaN_str: ', PVentaN_str)
            # print('CantidadN: ', CantidadN)
            # print('Importe_str: ', Importe_str)

            if Codigo not in productos_unicos:  # si código ya procesado
                iContadorUnicos = iContadorUnicos + 1
                productos_unicos.add(Codigo)  # Agregar el código al conjunto de productos únicos
                csv_line = ';'.join([Codigo, nombre, PVentaN_str, str(CantidadN), Importe_str])
                print(csv_line)
            # else:
            #     csv_line = ';'.join([Codigo, nombre, str(iContador)])
            #     print(csv_line)
print('--------------------------------------------------------------')
print('Total de productos: ',iContador)
print('Total de productos unicos: ',iContadorUnicos)
print('Total de productos vendidos: ',iContadorCantidadProductosVendidos)
# print(f'Total de productos únicos: {len(productos_unicos)}')