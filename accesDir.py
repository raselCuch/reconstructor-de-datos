import xml.etree.ElementTree as ET
import xmltodict, json

try:
    xml_file = open( './cucho/20610355154-01-F002-00000002.xml')
    # xml_file = open( '20610355154-01-F002-00000001.xml')
    obj = "" + xml_file.read() + "" # extrae en bruto el xml
    # print(obj)

    caracteres_a_eliminar = 'ï»¿'
    stringLimpio = obj.replace(caracteres_a_eliminar, '') # elimina caracteres innecesarios
    # print(stringLimpio)


    obj2 = xmltodict.parse(stringLimpio) # convierte a xml el string
    json_str = json.dumps(obj2, indent=4) # convierte a json y da identacion
    # print(json_str)

    newObj = json.loads(json_str) # accede al objto que esta dentro

    obje = newObj['Invoice'] # entra a la variable 'Invoice'

    # extrae la info necesaria
    
    Numero = obje['cac:Signature']['cbc:ID'].split('-')[1]
    print("Numero: ", Numero)

    # Crear la línea CSV
    # csv_line = ','.join([
    #     IdVenta, Fecha, Cliente, TipDocCli, Doc, Serie, Numero, TMoneda, NPedido, TCambio, TVenta, NDias, FVence,
    #     TBruto, TExonerada, TInafecta, TGratuita, TIgv, Total, TEst, Est, Empresa, Almacen, Vendedor, Usuario,
    #     ArchXml, NomArchXml, FecCreacion, UserCreacion, FecModi, UserModi, EGratuita, TComp, Dcto, ArchivoXml,
    #     ResumenFirma, ValorFirma, Cort, TipoPago, IdCajaApert, TipoPago2, MontoPago2, CantArt
    # ])

    # # Imprimir la línea CSV
    # print(csv_line)


except Exception as err:
    print("error: ", err)
finally:
    pass