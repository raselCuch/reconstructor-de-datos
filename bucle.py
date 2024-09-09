from pathlib import Path
import xml.etree.ElementTree as ET
import xmltodict, json
from datetime import datetime

path = Path("./xml")
print('-------------------------------------------------------------------------------------------------------------------------------------------------------')

i = 0
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
        # print('Fecha: ', Fecha) # anhomesdia
        fecha_formateada = datetime.strptime(Fecha, "%Y-%m-%d")
        fecha_concatenada = fecha_formateada.strftime("%Y%m%d")
        # print('fecha_concatenada: ', fecha_concatenada) # anhomesdia

        Cliente = obje['cac:AccountingCustomerParty']['cac:Party']['cac:PartyIdentification']['cbc:ID']['#text']
        if Cliente == 'C0000000001':
            TipDocCli = '1'
        else:
            TipDocCli = '6'
        Doc = tipoDocNum

        Serie = "002" # dato repetitivo en db
        Numero = NumeroT    
        TMoneda = "001" # dato repetitivo en db
        NPedido = "" # dato repetitivo en db
        TCambio = "3,748" # ____deshardcodear
        TVenta = "001" # dato repetitivo en db
        NDias = "0" # dato repetitivo en db
        FVence = "1900-01-01" # dato repetitivo en db
        TBruto = "0" # dato repetitivo en db

        TExonerada = obje['cac:LegalMonetaryTotal']['cbc:LineExtensionAmount']['#text']
        TExoneradaFloat = float(TExonerada)
        if TExoneradaFloat.is_integer():
                TExonerada_str = str(int(TExoneradaFloat))  # Convertir a entero y luego a string
        else:
                TExonerada_str = str(TExoneradaFloat)  # Mantener como float

        TInafecta = "0" # dato repetitivo en db
        TGratuita = "0" # dato repetitivo en db
        TIgv = "0" # dato repetitivo en db

        Total = TExonerada
        TotalFloat = float(Total)
        if TotalFloat.is_integer():
                TotalFloat_str = str(int(TotalFloat))  # Convertir a entero y luego a string
        else:
                TotalFloat_str = str(TotalFloat)  # Mantener como float

        TEst = "C" # dato repetitivo en db
        Est = "A" # dato repetitivo en db
        Empresa = EmpresaT
        Almacen = AlmacenT
        Vendedor = "carlos" # dato repetitivo en db
        Usuario = "carlos" # dato repetitivo en db
        ArchXml = "" # ____deshardcodear (dato extenso) pero se repite
        NomArchXml = obje['cac:Signature']['cbc:ID'] + ".xml"
        FecCreacion = obje['cbc:IssueDate'] + " " + obje['cbc:IssueTime']
        
        hora = obje['cbc:IssueTime']
        # hora = '01:00:00'
        # print('hora: ', hora)

        UserCreacion = "carlos" # dato repetitivo en db
        FecModi = ""  # null
        UserModi = ""  # 
        EGratuita = "0" # dato repetitivo en db
        TComp = "02" # dato repetitivo en db
        Dcto = "0" # dato repetitivo en db
        ArchivoXml = ""  # se repide de 'ArchXml'
        ResumenFirma = obje['ext:UBLExtensions']['ext:UBLExtension']['ext:ExtensionContent']['Signature']['SignedInfo']['Reference']['DigestValue']

        ValorFirma = obje['ext:UBLExtensions']['ext:UBLExtension']['ext:ExtensionContent']['Signature']['SignatureValue']

        Cort = "S" # ____deshardcodear es S o N
        TipoPago = "005" # ____deshardcodear es 005, 001 y 002

        # IdCajaApert = ""  # ____deshardcodear solo hay este dato 120240828
        hora_formateada = datetime.strptime(hora, "%H:%M:%S").time()
       
        franja_horaria = ""

        if hora_formateada >= datetime.strptime("08:00:00", "%H:%M:%S").time() and hora_formateada < datetime.strptime("16:00:00", "%H:%M:%S").time():
            franja_horaria = "001" # Mañana
        elif hora_formateada >= datetime.strptime("16:00:00", "%H:%M:%S").time() and hora_formateada < datetime.strptime("23:59:59", "%H:%M:%S").time():
            franja_horaria = "003" # Noche
        else:
            franja_horaria = "004" # Madrugada
        
        # print('IdCajaApert', hora_formateada)
        # print('franja_horaria', franja_horaria)
        # print()

        IdCajaApert = franja_horaria + "" + fecha_concatenada
        # print('IdCajaApert', IdCajaApert)

        TipoPago2 = ""  # dato repetitivo en db
        MontoPago2 = ""  # dato repetitivo en db
        CantArt = obje['cbc:LineCountNumeric']
        i=i+1

        csv_line = ';'.join([
            IdVenta, Fecha, Cliente, TipDocCli, Doc, Serie, Numero, TMoneda, NPedido, TCambio, TVenta, NDias, FVence,
            TBruto, TExonerada_str, TInafecta, TGratuita, TIgv, TotalFloat_str, TEst, Est, Empresa, Almacen, Vendedor, Usuario,
            ArchXml, NomArchXml, FecCreacion,UserCreacion, FecModi, UserModi, EGratuita, TComp, Dcto, ArchivoXml,
            ResumenFirma, ValorFirma, Cort, TipoPago, IdCajaApert, TipoPago2, MontoPago2, CantArt
        ])

        print(csv_line)
print(i)
