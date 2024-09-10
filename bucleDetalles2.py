from pathlib import Path
import xml.etree.ElementTree as ET
import xmltodict, json

path = Path("./xml")
iContador = 0

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
        # print('cantidad de articulos: ' + CantArt)

        # Unificar la lógica para uno o más productos
        for i in range(numero):

            Numero = obje['cac:Signature']['cbc:ID'].split('-')[1]
            tipoDoc = obje['cac:Signature']['cbc:ID'][0]
            tipoDocNum = '013' if tipoDoc == 'B' else '014'

            Empresa = obje['cac:Signature']['cac:SignatoryParty']['cac:PartyIdentification']['cbc:ID']
            RUCd = obje['cac:AccountingCustomerParty']['cac:Party']['cac:PartyIdentification']['cbc:ID']['#text']
            Almacen = '002'
            IdVenta = RUCd + tipoDocNum + '002-' + Numero + Almacen + Empresa
                           
            # Acceder a la línea de factura
            invoice_line = obje['cac:InvoiceLine'][i] if numero > 1 else obje['cac:InvoiceLine']

            Codigo = invoice_line['cac:Item']['cac:SellersItemIdentification']['cbc:ID']
            Marca = ''
            Unidad = ''
            Proced = ''
            PVenta = invoice_line['cac:PricingReference']['cac:AlternativeConditionPrice']['cbc:PriceAmount']['#text']
            Cantidad = invoice_line['cbc:InvoicedQuantity']['#text'].split('.')[0]

            Dcto = '0'
            Igv = '0'



            PVentaN = float(PVenta)  # Convertir a float para manejar decimales
            CantidadN = int(Cantidad)  # Convertir a entero

            if PVentaN.is_integer():
                PVentaN_str = str(int(PVentaN))  # Convertir a entero y luego a string
            else:
                PVentaN_str = str(PVentaN)  # Mantener como flo
            # print('pventta: ', PVentaN_str)
            # print('CantidadN: ', CantidadN)

            Importe = PVentaN * CantidadN

            # Importe_str = str(Importe)
            if Importe.is_integer():
                Importe_str = str(int(Importe))  # Convertir a entero y luego a string
            else:
                Importe_str = str(Importe)  # Mantener como float
            # print('\n')
            # print('Importe_str: ', Importe_str)

            TipPrecio = "01"
            TipImpuesto = "20"
            FecCreacion = obje['cbc:IssueDate'] + " " + obje['cbc:IssueTime']
            UserCreacion = "carlos"
            FecModi = ""
            UserModi = ""
            Norden = invoice_line['cbc:ID']
            DescripServ = ""
            PCosto = ""

            csv_line = ';'.join([
                IdVenta, Codigo, Marca, Unidad, Proced, PVentaN_str, Cantidad, Dcto, Igv, Importe_str, 
                Almacen, Empresa, TipPrecio, TipImpuesto, FecCreacion, UserCreacion, FecModi, 
                UserModi, Norden, DescripServ, PCosto
            ])

            print(csv_line)
            
            iContador=iContador+1
print(iContador)