import xmltodict, json

print("================= rasel cucho ===================")

obj = xmltodict.parse("""
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:ccts="urn:un:unece:uncefact:documentation:2" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:sac="urn:sunat:names:specification:ubl:peru:schema:xsd:SunatAggregateComponents-1" xmlns:udt="urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ext:UBLExtensions>
<ext:UBLExtension>
<ext:ExtensionContent>
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#" Id="SignOpenInvoice">
<SignedInfo>
<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
<Reference URI="">
<Transforms>
<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
</Transforms>
<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
<DigestValue>GCLV1iwa9M/w5ekZhCCpdfyFmaY=</DigestValue>
</Reference>
</SignedInfo>
<SignatureValue>Xh/wYlrqCC4aSDp7hO/SGl3byOWNXN+77tmtAopNzk1FV7RklFE4R72m8/VvTDT2OTSnEDbIIyG0CnPR4VW1xE//sb3vynyLVQWBJJMaGyJFTOWVxrbpJYxSSywg7ikEE0ScrpIUi98tYX55HKmR1ExKWI31gB3mupXoWgXbrlv66lPwvz3ATsIuFbvj25n8i2lapFFoK8djTdqTUJoBYc0c005XdKFSpw9VOfrO6xUOBld+6gnfkxBEi9fVHheGoXkJjaOxa5vaS+KrQLQvu8+EAV6NoS9WvEh0C4cRz6sQKjlAidRESlL1JcMWTFMYu+4xKpnVmUTPqKSwOwvcag==</SignatureValue>
<KeyInfo>
<X509Data>
<X509SubjectName>Description=Certificado para Facturación Electrónica, OID.1.3.6.1.4.1.47286.30.2=RUC, OID.1.3.6.1.4.1.47286.30.3=20610355154, OID.1.3.6.1.4.1.47286.30.4=DNI, E=c88javier@gmail.com, CN=JAVIER ANDRES CHAVEZ CORAL, SERIALNUMBER=71643028, G=JAVIER ANDRES, SN=CHAVEZ CORAL, T=TITULAR-GERENTE, OU=GERENCIA, OU=20610355154, O=SERVICIOS Y SUMINISTROS GENERALES SSG E.I.R.L., L=CORONEL PORTILLO - YARINACOCHA, C=PE</X509SubjectName>
<X509Certificate>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</X509Certificate>
</X509Data>
</KeyInfo>
</Signature>
</ext:ExtensionContent>
</ext:UBLExtension>
</ext:UBLExtensions>
<cbc:UBLVersionID>2.1</cbc:UBLVersionID>
<cbc:CustomizationID>2.0</cbc:CustomizationID>
<cbc:ID>B002-00000022</cbc:ID>
<cbc:IssueDate>2024-08-10</cbc:IssueDate>
<cbc:IssueTime>13:08:54</cbc:IssueTime>
<cbc:DueDate>2024-08-10</cbc:DueDate>
<cbc:InvoiceTypeCode listID="0101" listAgencyName="PE:SUNAT" listName="Tipo de Documento" listURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo01">03</cbc:InvoiceTypeCode>
<cbc:Note languageLocaleID="1000">QUINCE CON 50/100 SOLES</cbc:Note>
<cbc:DocumentCurrencyCode listID="ISO 4217 Alpha" listName="Currency" listAgencyName="United Nations Economic Commission for Europe">PEN</cbc:DocumentCurrencyCode>
<cbc:LineCountNumeric>1</cbc:LineCountNumeric>
<cac:Signature>
<cbc:ID>B002-00000022</cbc:ID>
<cac:SignatoryParty>
<cac:PartyIdentification>
<cbc:ID>20610355154</cbc:ID>
</cac:PartyIdentification>
<cac:PartyName>
<cbc:Name>REBO MARKET</cbc:Name>
</cac:PartyName>
</cac:SignatoryParty>
<cac:DigitalSignatureAttachment>
<cac:ExternalReference>
<cbc:URI>20610355154-B002-00000022</cbc:URI>
</cac:ExternalReference>
</cac:DigitalSignatureAttachment>
</cac:Signature>
<cac:AccountingSupplierParty>
<cac:Party>
<cac:PartyIdentification>
<cbc:ID schemeID="6" schemeName="Documento de Identidad" schemeAgencyName="PE:SUNAT" schemeURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo06">20610355154</cbc:ID>
</cac:PartyIdentification>
<cac:PartyName>
<cbc:Name>
<![CDATA[ REBO MARKET ]]>
</cbc:Name>
</cac:PartyName>
<cac:PartyLegalEntity>
<cbc:RegistrationName>
<![CDATA[ REBO MARKET ]]>
</cbc:RegistrationName>
<cac:RegistrationAddress>
<cbc:AddressTypeCode>0000</cbc:AddressTypeCode>
</cac:RegistrationAddress>
</cac:PartyLegalEntity>
</cac:Party>
</cac:AccountingSupplierParty>
<cac:AccountingCustomerParty>
<cac:Party>
<cac:PartyIdentification>
<cbc:ID schemeID="1" schemeName="Documento de Identidad" schemeAgencyName="PE:SUNAT" schemeURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo06">C0000000001</cbc:ID>
</cac:PartyIdentification>
<cac:PartyLegalEntity>
<cbc:RegistrationName>
<![CDATA[ CLIENTES VARIOS ]]>
</cbc:RegistrationName>
</cac:PartyLegalEntity>
</cac:Party>
</cac:AccountingCustomerParty>
<cac:PaymentTerms>
<cbc:ID>FormaPago</cbc:ID>
<cbc:PaymentMeansID>Contado</cbc:PaymentMeansID>
</cac:PaymentTerms>
<cac:TaxTotal>
<cbc:TaxAmount currencyID="PEN">0.00</cbc:TaxAmount>
<cac:TaxSubtotal>
<cbc:TaxableAmount currencyID="PEN">15.50</cbc:TaxableAmount>
<cbc:TaxAmount currencyID="PEN">0.00</cbc:TaxAmount>
<cac:TaxCategory>
<cbc:ID schemeID="UN/ECE 5305" schemeName="Tax Category Identifier" schemeAgencyName="United Nations Economic Commission for Europe">E</cbc:ID>
<cac:TaxScheme>
<cbc:ID schemeID="UN/ECE 5305" schemeAgencyID="6">9997</cbc:ID>
<cbc:Name>EXO</cbc:Name>
<cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
</cac:TaxScheme>
</cac:TaxCategory>
</cac:TaxSubtotal>
</cac:TaxTotal>
<cac:LegalMonetaryTotal>
<cbc:LineExtensionAmount currencyID="PEN">15.50</cbc:LineExtensionAmount>
<cbc:TaxInclusiveAmount currencyID="PEN">15.50</cbc:TaxInclusiveAmount>
<cbc:PayableAmount currencyID="PEN">15.50</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
<cac:InvoiceLine>
<cbc:ID>1</cbc:ID>
<cbc:InvoicedQuantity unitCode="NIU" unitCodeListID="UN/ECE rec 20" unitCodeListAgencyName="United Nations Economic Commission for Europe">1.00</cbc:InvoicedQuantity>
<cbc:LineExtensionAmount currencyID="PEN">15.50</cbc:LineExtensionAmount>
<cac:PricingReference>
...
</cac:PricingReference>
<cac:TaxTotal>
<cbc:TaxAmount currencyID="PEN">0.00</cbc:TaxAmount>
<cac:TaxSubtotal>
<cbc:TaxableAmount currencyID="PEN">15.50</cbc:TaxableAmount>
<cbc:TaxAmount currencyID="PEN">0.00</cbc:TaxAmount>
<cac:TaxCategory>
<cbc:ID schemeID="UN/ECE 5305" schemeName="Codigo de tributos" schemeAgencyName="PE:SUNAT">E</cbc:ID>
<cbc:Percent>18.00</cbc:Percent>
<cbc:TaxExemptionReasonCode listAgencyName="PE:SUNAT" listName="Afectacion del IGV" listURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo07">20</cbc:TaxExemptionReasonCode>
<cac:TaxScheme>
<cbc:ID schemeID="UN/ECE 5153" schemeName="Codigo de tributos" schemeAgencyName="PE:SUNAT">9997</cbc:ID>
<cbc:Name>EXO</cbc:Name>
<cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
</cac:TaxScheme>
</cac:TaxCategory>
</cac:TaxSubtotal>
</cac:TaxTotal>
<cac:Item>
<cbc:Description>HUEVO X JABA</cbc:Description>
<cac:SellersItemIdentification>
<cbc:ID>001196</cbc:ID>
</cac:SellersItemIdentification>
</cac:Item>
<cac:Price>
<cbc:PriceAmount currencyID="PEN">15.50</cbc:PriceAmount>
</cac:Price>
</cac:InvoiceLine>
</Invoice> 
                      """)

json_str = json.dumps(obj, indent=4)

# print(json_str)
newObj = json.loads(json_str)

obje = newObj['Invoice']

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
# csv_line = ','.join([
#     IdVenta, Fecha, Cliente, TipDocCli, Doc, Serie, Numero, TMoneda, NPedido, TCambio, TVenta, NDias, FVence,
#     TBruto, TExonerada, TInafecta, TGratuita, TIgv, Total, TEst, Est, Empresa, Almacen, Vendedor, Usuario,
#     ArchXml, NomArchXml, FecCreacion, UserCreacion, FecModi, UserModi, EGratuita, TComp, Dcto, ArchivoXml,
#     ResumenFirma, ValorFirma, Cort, TipoPago, IdCajaApert, TipoPago2, MontoPago2, CantArt
# ])

# # Imprimir la línea CSV
# print(csv_line)
