from pathlib import Path
import xml.etree.ElementTree as ET
import xmltodict, json

# Path del directorio
path = Path("./cucho")
i = 0
# Obtener todos los archivos en el directorio
for file in path.rglob('*'):  # rglob permite buscar archivos recursivamente
    if file.is_file():
        # print(file)

        file_str = str(file)
        
        caracteres_a_reemplazar = '\\'  # Usar doble backslash

        xml_file = file_str.replace(caracteres_a_reemplazar, '/') # elimina caracteres innecesarios
        
        # print("./"+xml_file + "")
        
        # print("\n")
        # print("-------------------------------archivo: "+"./"+xml_file + " -------------------------------")

        xml_file = open( xml_file )
        obj = "" + xml_file.read() + "" # extrae en bruto el xml

        caracteres_a_eliminar = 'ï»¿'
        stringLimpio = obj.replace(caracteres_a_eliminar, '') # elimina caracteres innecesarios
        # print("-------------------------------otro archivo-------------------------------\n")
        # print(stringLimpio)

        obj2 = xmltodict.parse(stringLimpio) # convierte a xml el string
        json_str = json.dumps(obj2, indent=4)
        # print(json_str)

        newObj = json.loads(json_str) # accede al objto que esta dentro

        obje = newObj['Invoice'] # base

        CantArt = obje['cbc:LineCountNumeric']

        numero = int(CantArt)

        NomArchXml = obje['cac:Signature']['cbc:ID'] + ".xml"

        # print(NomArchXml+" cantidad de productos: ", CantArt)


        if numero > 1:
            for i in range(numero):
                # print(obje['cac:InvoiceLine'][i]['cbc:ID'])

                Numero = obje['cac:Signature']['cbc:ID'].split('-')[1]
                IdVenta = 'C0000000001013002-' + Numero + '00220610355154'
                Codigo = obje['cac:InvoiceLine'][i]['cac:Item']['cac:SellersItemIdentification']['cbc:ID']
                Marca = ''
                Unidad = ''
                Proced = ''

                # PVenta = obje['cac:InvoiceLine'][i]['cbc:LineExtensionAmount']['#text']
                PVenta = obje['cac:InvoiceLine'][i]['cac:PricingReference']['cac:AlternativeConditionPrice']['cbc:PriceAmount']['#text']

                Cantidad = obje['cac:InvoiceLine'][i]['cbc:InvoicedQuantity']['#text'].split('.')[0]
                # Cantidad = obje['cac:InvoiceLine'][i]['cbc:InvoicedQuantity']['#text']

                Dcto = ''
                Igv = ''
                Importe = '1'
                Almacen = '002'
                Empresa = "20610355154"
                TipPrecio = "01"
                TipImpuesto = ""
                FecCreacion = obje['cbc:IssueDate'] + " " + obje['cbc:IssueTime']

                UserCreacion = "carlos"
                FecModi = ""
                UserModi = ""
                Norden = obje['cac:InvoiceLine'][i]['cbc:ID']
                DescripServ = ""
                PCosto = ""

                # print("IdVenta: ", IdVenta)
                # print("Codigo: ", Codigo)
                # print("Marca: ", Marca)
                # print("Unidad: ", Unidad)
                # print("Proced: ", Proced)

                # print("PVenta: ", PVenta)
                # print("Cantidad: ", Cantidad)
                # print("Dcto: ", Dcto)
                # print("Igv: ", Igv)
                # print("Importe: ", Importe)
                # print("Almacen: ", Almacen)
                # print("Empresa: ", Empresa)
                # print("TipPrecio: ", TipPrecio)
                # print("TipImpuesto: ", Empresa)
                # print("FecCreacion:", FecCreacion)
                # print("UserCreacion:", UserCreacion)
                # print("FecModi:", FecModi)
                # print("UserModi:", UserModi)
                # print("Norden:", Norden)
                # print("DescripServ:", DescripServ)
                # print("PCosto:", PCosto)

                csv_line = ';'.join([
                IdVenta, Codigo, Marca, Unidad, Proced, PVenta, Cantidad, Dcto, Igv, Importe, Almacen, Empresa, TipPrecio,
                TipImpuesto, FecCreacion, UserCreacion, FecModi, UserModi, Norden, DescripServ, PCosto
                ])

                print(csv_line)
                # print("-------------")
        else: 
            # print("salta del bucle")
            Numero1 = obje['cac:Signature']['cbc:ID'].split('-')[1]
            IdVenta1 = 'C0000000001013002-' + Numero1 + '00220610355154'
            Codigo1 = obje['cac:InvoiceLine']['cac:Item']['cac:SellersItemIdentification']['cbc:ID']

            Marca1 = ''
            Unidad1 = ''
            Proced1 = ''
            PVenta1 = obje['cac:InvoiceLine']['cac:PricingReference']['cac:AlternativeConditionPrice']['cbc:PriceAmount']['#text']

            Cantidad1 = obje['cac:InvoiceLine']['cbc:InvoicedQuantity']['#text'].split('.')[0]

            Dcto1 = ''
            Igv1 = ''
            Importe1 = '1'
            Almacen1 = '002'
            Empresa1 = "20610355154"
            TipPrecio1 = "01"
            TipImpuesto1 = ""
            FecCreacion1 = obje['cbc:IssueDate'] + " " + obje['cbc:IssueTime']

            UserCreacion1 = "carlos"
            FecModi1 = ""
            UserModi1 = ""
            Norden1 = obje['cac:InvoiceLine']['cbc:ID']
            DescripServ1 = ""
            PCosto1 = ""

            # print("IdVenta1: ", IdVenta1)
            # print("Codigo1: ", Codigo1)
            # print("Marca: ", Marca1)
            # print("Unidad: ", Unidad1)
            # print("Proced: ", Proced1)
            # print("PVenta: ", PVenta1)
            # print("Cantidad: ", Cantidad1)
            # print("Dcto: ", Dcto1)
            # print("Igv: ", Igv1)
            # print("Importe: ", Importe1)
            # print("Almacen: ", Almacen1)
            # print("Empresa: ", Empresa1)
            # print("TipPrecio: ", TipPrecio1)
            # print("TipImpuesto: ", Empresa1)
            # print("FecCreacion:", FecCreacion1)
            
            # print("UserCreacion:", UserCreacion1)
            # print("FecModi:", FecModi1)
            # print("UserModi:", UserModi1)
            # print("Norden:", Norden1)
            # print("DescripServ:", DescripServ1)
            # print("PCosto:", PCosto1)

            csv_line1 = ';'.join([
            IdVenta1, Codigo1, Marca1, Unidad1, Proced1, PVenta1, Cantidad1, Dcto1, Igv1, Importe1,
            Almacen1, Empresa1, TipPrecio1, TipImpuesto1, FecCreacion1, UserCreacion1, FecModi1,
            UserModi1, Norden1, DescripServ1, PCosto1
            ])

            print(csv_line1)

            # print("-------------")
