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

        obje = newObj['Invoice'] # entra a la variable 'Invoice'

        # extrae la info necesaria
        
        Numero = obje['cac:Signature']['cbc:ID'].split('-')[1]
        IdVenta = 'C0000000001013002-'+Numero+'00220610355154'
        Fecha = obje['cbc:IssueDate']
        # Cliente = "C0000000001"
        Cliente = obje['cac:AccountingCustomerParty']['cac:Party']['cac:PartyIdentification']['cbc:ID']['#text']
        TipDocCli = "1"
        Doc = "013"
        Serie = "002"
        # Numero
        TMoneda = "001"
        NPedido = ""

        TCambio = "3,748"
        TVenta = "001"
        NDias = "0"
        FVence = "1900-01-01"
        TBruto = "0"

        TExonerada = obje['cac:LegalMonetaryTotal']['cbc:LineExtensionAmount']['#text']

        TInafecta = "0"
        TGratuita = "0"
        TIgv = "0"
        Total = TExonerada

        TEst = "C"
        Est = "A"
        Empresa = "20610355154"
        Almacen = "002"
        Vendedor = "carlos"
        Usuario = "carlos"
        ArchXml = ""

        NomArchXml = obje['cac:Signature']['cbc:ID'] + ".xml"
        FecCreacion = obje['cbc:IssueDate'] + " " + obje['cbc:IssueTime']

        UserCreacion = "carlos"
        FecModi = ""  # Parece que no hay valor para esta variable
        UserModi = ""  # Parece que no hay valor para esta variable
        EGratuita = "0"
        TComp = "02"
        Dcto = "0"

        ArchivoXml = ""  # Parece que no hay valor para esta variable
        ResumenFirma = ""  # Parece que no hay valor para esta variable
        ValorFirma = ""
        Cort = "S"
        TipoPago = "005"
        IdCajaApert = ""  # Parece que no hay valor para esta variable
        TipoPago2 = ""  # Parece que no hay valor para esta variable
        MontoPago2 = ""  # Parece que no hay valor para esta variable

        CantArt = obje['cbc:LineCountNumeric']

        # i=i+1
        # print(i)
        # print(obj)
        
        # print("-------------------------------archivo: "+"./"+xml_file + " -------------------------------\n")

        # print("IdVenta: ", IdVenta)
        # print("Fecha: ", Fecha)
        # print("Cliente: ", Cliente)
        # print("TipDocCli: ", TipDocCli)
        # print("Doc: ", Doc)
        # print("Serie: ", Serie)
        # print("Numero: ", Numero)
        # print("TMoneda: ", TMoneda)
        # print("NPedido: ", NPedido)
        # print("TCambio:", TCambio)
        # print("TVenta:", TVenta)
        # print("NDias:", NDias)
        # print("FVence:", FVence)
        # print("TBruto:", TBruto)
        # print("TExonerada:", TExonerada)
        # print("TInafecta:", TInafecta)
        # print("TGratuita:", TGratuita)
        # print("TIgv:", TIgv)
        # print("Total:", Total)

        # print("TEst:", TEst)
        # print("Est:", Est)
        # print("Empresa:", Empresa)
        # print("Almacen:", Almacen)
        # print("Vendedor:", Vendedor)
        # print("Usuario:", Usuario)
        # print("ArchXml:", ArchXml)
        # print("NomArchXml:", NomArchXml)
        # print("FecCreacion:", FecCreacion)

        # print("UserCreacion:", UserCreacion)
        # print("FecModi:", FecModi)
        # print("UserModi:", UserModi)
        # print("EGratuita:", EGratuita)
        # print("TComp:", TComp)
        # print("Dcto:", Dcto)

        # print("ArchivoXml:", ArchivoXml)
        # print("ResumenFirma:", ResumenFirma)
        # print("ValorFirma:", ValorFirma)
        # print("Cort:", Cort)
        # print("TipoPago:", TipoPago)
        # print("IdCajaApert:", IdCajaApert)
        # print("TipoPago2:", TipoPago2)
        # print("MontoPago2:", MontoPago2)
        # print("CantArt:", CantArt)

        # Crear la línea CSV
        csv_line = ';'.join([
            IdVenta, Fecha, Cliente, TipDocCli, Doc, Serie, Numero, TMoneda, NPedido, TCambio, TVenta, NDias, FVence,
            TBruto, TExonerada, TInafecta, TGratuita, TIgv, Total, TEst, Est, Empresa, Almacen, Vendedor, Usuario,
            ArchXml, NomArchXml, FecCreacion, UserCreacion, FecModi, UserModi, EGratuita, TComp, Dcto, ArchivoXml,
            ResumenFirma, ValorFirma, Cort, TipoPago, IdCajaApert, TipoPago2, MontoPago2, CantArt
        ])

        # Imprimir la línea CSV
        print(csv_line)

# print(i)
