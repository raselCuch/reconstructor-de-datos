from pathlib import Path
import xml.etree.ElementTree as ET
import xmltodict, json

path = Path("./cucho")
# i = 0
for file in path.rglob('*'):  # rglob permite buscar archivos recursivamente
    if file.is_file():
        file_str = str(file)
        caracteres_a_reemplazar = '\\'  # Usar doble backslash
        xml_file = file_str.replace(caracteres_a_reemplazar, '/') # elimina caracteres innecesarios
        # print("-------------------------------archivo: "+"./"+xml_file + " -------------------------------")
        xml_file = open( xml_file )
        obj = "" + xml_file.read() + "" # extrae en bruto el xml
        caracteres_a_eliminar = 'ï»¿'
        stringLimpio = obj.replace(caracteres_a_eliminar, '') # elimina caracteres innecesarios
        obj2 = xmltodict.parse(stringLimpio) # convierte a xml el string
        json_str = json.dumps(obj2, indent=4)
        newObj = json.loads(json_str) # accede al objto que esta dentro

        ##########
        obje = newObj['Invoice'] # entra a la variable 'Invoice'

        NumeroT = obje['cac:Signature']['cbc:ID'].split('-')[1]
        tipoDoc = obje['cac:Signature']['cbc:ID'][0]
        tipoDocNum = '013' if tipoDoc == 'B' else '014'
        EmpresaT = obje['cac:Signature']['cac:SignatoryParty']['cac:PartyIdentification']['cbc:ID']
        RUCd = obje['cac:AccountingCustomerParty']['cac:Party']['cac:PartyIdentification']['cbc:ID']['#text']
        AlmacenT = '002'
        ######################
        IdVenta = RUCd + tipoDocNum + '002-' + NumeroT + AlmacenT + EmpresaT
        
        Fecha = obje['cbc:IssueDate']
        Cliente = obje['cac:AccountingCustomerParty']['cac:Party']['cac:PartyIdentification']['cbc:ID']['#text']
        if Cliente == 'C0000000001':
            TipDocCli = '1'
        else:
            TipDocCli = '6'
        Doc = tipoDocNum
        Serie = "002"
        Numero = NumeroT
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
        Empresa = EmpresaT
        Almacen = AlmacenT
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

        csv_line = ';'.join([
            IdVenta, Fecha, Cliente, TipDocCli, Doc, Serie, Numero, TMoneda, NPedido, TCambio, TVenta, NDias, FVence,
            TBruto, TExonerada, TInafecta, TGratuita, TIgv, Total, TEst, Est, Empresa, Almacen, Vendedor, Usuario,
            ArchXml, NomArchXml, FecCreacion, UserCreacion, FecModi, UserModi, EGratuita, TComp, Dcto, ArchivoXml,
            ResumenFirma, ValorFirma, Cort, TipoPago, IdCajaApert, TipoPago2, MontoPago2, CantArt
        ])

        print(csv_line)
