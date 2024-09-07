from pathlib import Path
import xml.etree.ElementTree as ET
import xmltodict, json

path = Path("./cucho")
i = 0

for file in path.rglob('*'):
    if file.is_file():

        file_str = str(file)
        caracteres_a_reemplazar = '\\'
        xml_file = file_str.replace(caracteres_a_reemplazar, '/')
        
        # print("------------------------------- archivo: "+"./"+xml_file + "\n")

        xml_file = open( xml_file )
        obj = "" + xml_file.read() + "" # extrae en bruto el xml
        cleaned_xml = obj.replace('ï»¿', '') # elimina caracteres innecesarios
        obj2 = xmltodict.parse(cleaned_xml) # convierte a xml el string
        json_str = json.dumps(obj2, indent=4)
        newObj = json.loads(json_str) # accede al obj que esta dentro
        obje = newObj['Invoice'] # base
        CantArt = obje['cbc:LineCountNumeric']
        numero = int(CantArt)
        # print('cantidad de articulos: ' + CantArt)

        if numero > 1:
            for i in range(numero):

                Numero = obje['cac:Signature']['cbc:ID'].split('-')[1]

                tipoDoc = obje['cac:Signature']['cbc:ID'][0]
                if tipoDoc == 'B':
                    tipoDocNum = '013'
                elif tipoDoc == 'F':
                    tipoDocNum = '014'
                # print('tipoDocNum', tipoDocNum)

                Empresa = obje['cac:Signature']['cac:SignatoryParty']['cac:PartyIdentification']['cbc:ID'] # ruc de emoresa sin harcodear
                RUCd = obje['cac:AccountingCustomerParty']['cac:Party']['cac:PartyIdentification']['cbc:ID']['#text']
                # print('RUCd', RUCd)
                IdVenta = RUCd + tipoDocNum + '002-' + Numero + Empresa # falta almacen creo y el 002
                           
                Codigo = obje['cac:InvoiceLine'][i]['cac:Item']['cac:SellersItemIdentification']['cbc:ID']
                Marca = ''
                Unidad = ''
                Proced = ''
                PVenta = obje['cac:InvoiceLine'][i]['cac:PricingReference']['cac:AlternativeConditionPrice']['cbc:PriceAmount']['#text']
                Cantidad = obje['cac:InvoiceLine'][i]['cbc:InvoicedQuantity']['#text'].split('.')[0]

                Dcto = '0'
                Igv = '0'

                PVentaN = float(PVenta)  # Convertir a float para manejar decimales
                CantidadN = int(Cantidad)  # Convertir a entero (si solo necesitas la parte entera)

                Importe = PVentaN * CantidadN
                Importe_str = str(Importe)


                # print("PVenta: ", PVenta)
                # print("Cantidad: ", Cantidad)
                # print("Importe: ", Importe)

                Almacen = '002'
                TipPrecio = "01" # falta
                TipImpuesto = "" # falta
                FecCreacion = obje['cbc:IssueDate'] + " " + obje['cbc:IssueTime']
                UserCreacion = "carlos"
                FecModi = ""
                UserModi = ""
                Norden = obje['cac:InvoiceLine'][i]['cbc:ID']
                DescripServ = ""
                PCosto = "" # falta

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
                # print("TipImpuesto: ", TipImpuesto)
                # print("FecCreacion:", FecCreacion)
                # print("UserCreacion:", UserCreacion)
                # print("FecModi:", FecModi)
                # print("UserModi:", UserModi)
                # print("Norden:", Norden)
                # print("DescripServ:", DescripServ)
                # print("PCosto:", PCosto)

                csv_line = ';'.join([
                IdVenta, Codigo, Marca, Unidad, Proced, PVenta, Cantidad, Dcto, Igv, Importe_str, Almacen, Empresa, TipPrecio,
                TipImpuesto, FecCreacion, UserCreacion, FecModi, UserModi, Norden, DescripServ, PCosto
                ])

                print(csv_line)
                # print("-------------")
        else: 
            
            Numero1 = obje['cac:Signature']['cbc:ID'].split('-')[1]

            tipoDoc = obje['cac:Signature']['cbc:ID'][0]
            if tipoDoc == 'B':
                tipoDocNum = '013'
            elif tipoDoc == 'F':
                tipoDocNum = '014'
            # tipoDoc = obje['cac:Signature']['cbc:ID']
            # print('tipoDoc', tipoDoc)

            Empresa1 = obje['cac:Signature']['cac:SignatoryParty']['cac:PartyIdentification']['cbc:ID'] # ruc de emoresa sin harcodear
            RUCd1 = obje['cac:AccountingCustomerParty']['cac:Party']['cac:PartyIdentification']['cbc:ID']['#text']
            # IdVenta = RUCd + '013002-' + Numero + Empresa

            IdVenta1 = RUCd1 + tipoDocNum + '002-' + Numero1 + Empresa1
            Codigo1 = obje['cac:InvoiceLine']['cac:Item']['cac:SellersItemIdentification']['cbc:ID']
            Marca1 = ''
            Unidad1 = ''
            Proced1 = ''
            PVenta1 = obje['cac:InvoiceLine']['cac:PricingReference']['cac:AlternativeConditionPrice']['cbc:PriceAmount']['#text']
            Cantidad1 = obje['cac:InvoiceLine']['cbc:InvoicedQuantity']['#text'].split('.')[0]
            Dcto1 = '0'
            Igv1 = '0'
            
            PVentaN1 = float(PVenta1)  # Convertir a float para manejar decimales
            CantidadN1 = int(Cantidad1)  # Convertir a entero (si solo necesitas la parte entera)

            Importe1 = PVentaN1 * CantidadN1
            Importe_str1 = str(Importe1)


            # Importe1 = '1'

            Almacen1 = '002'

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
            IdVenta1, Codigo1, Marca1, Unidad1, Proced1, PVenta1, Cantidad1, Dcto1, Igv1, Importe_str1,
            Almacen1, Empresa1, TipPrecio1, TipImpuesto1, FecCreacion1, UserCreacion1, FecModi1,
            UserModi1, Norden1, DescripServ1, PCosto1
            ])

            print(csv_line1)
            # print("-------------")
