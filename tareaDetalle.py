import xmltodict, json

print("================= rasel cucho ===================")

obj = xmltodict.parse("""<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:ccts="urn:un:unece:uncefact:documentation:2" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:sac="urn:sunat:names:specification:ubl:peru:schema:xsd:SunatAggregateComponents-1" xmlns:udt="urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
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
<DigestValue>0OTn5zozOKfAhphGB/CKUbrUHSA=</DigestValue>
</Reference>
</SignedInfo>
<SignatureValue>it9plGafLRXnAq6CENStR5/GBDKK/ClNPZCqyEtM6zHzF0G2rQqR2mjdX4swjMJ3CiZvGU6nyYck9KAr7b3zlYPdSRd9BLMAInVsEFV4+QCyEorI0vXrteP4JN1YE655Sotst2bVMxxTSAWH0WlflLq3PXoucrTCAh+7acM1S6DHGid7pM4RxZ/vVozMQWZN6EZzJr3hEtWjJ89Aiai9rO6XoQwwg4BD8231wZNLqmDzMdrJ7nIZuXSTyDOHSWRVdIOff9JV/7bw6PvrNXZQvh8Ejze2rinvZEN+OQ80fdjjYomkJAzSOV0YNnHulRdESVt39/b/yrTVLvbIBcy3ng==</SignatureValue>
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
<cbc:ID>F002-00000001</cbc:ID>
<cbc:IssueDate>2024-08-19</cbc:IssueDate>
<cbc:IssueTime>13:20:00</cbc:IssueTime>
<cbc:DueDate>2024-08-19</cbc:DueDate>
<cbc:InvoiceTypeCode listID="0101" listAgencyName="PE:SUNAT" listName="Tipo de Documento" listURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo01">01</cbc:InvoiceTypeCode>
<cbc:Note languageLocaleID="1000">NOVENTA Y SEIS CON 00/100 SOLES</cbc:Note>
<cbc:DocumentCurrencyCode listID="ISO 4217 Alpha" listName="Currency" listAgencyName="United Nations Economic Commission for Europe">PEN</cbc:DocumentCurrencyCode>
<cbc:LineCountNumeric>4</cbc:LineCountNumeric>
<cac:Signature>
<cbc:ID>F002-00000001</cbc:ID>
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
<cbc:URI>20610355154-F002-00000001</cbc:URI>
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
<cbc:ID schemeID="6" schemeName="Documento de Identidad" schemeAgencyName="PE:SUNAT" schemeURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo06">10710741374</cbc:ID>
</cac:PartyIdentification>
<cac:PartyLegalEntity>
<cbc:RegistrationName>
<![CDATA[ MARIN AMASIFUEN SARITA ]]>
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
<cbc:TaxableAmount currencyID="PEN">96.00</cbc:TaxableAmount>
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
<cbc:LineExtensionAmount currencyID="PEN">96.00</cbc:LineExtensionAmount>
<cbc:TaxInclusiveAmount currencyID="PEN">96.00</cbc:TaxInclusiveAmount>
<cbc:PayableAmount currencyID="PEN">96.00</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
<cac:InvoiceLine>
<cbc:ID>1</cbc:ID>
<cbc:InvoicedQuantity unitCode="NIU" unitCodeListID="UN/ECE rec 20" unitCodeListAgencyName="United Nations Economic Commission for Europe">3.00</cbc:InvoicedQuantity>
<cbc:LineExtensionAmount currencyID="PEN">36.00</cbc:LineExtensionAmount>
<cac:PricingReference>
<cac:AlternativeConditionPrice>
<cbc:PriceAmount currencyID="PEN">12.00</cbc:PriceAmount>
<cbc:PriceTypeCode listName="Tipo de Precio" listAgencyName="PE:SUNAT" listURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo16">01</cbc:PriceTypeCode>
</cac:AlternativeConditionPrice>
</cac:PricingReference>
<cac:TaxTotal>
<cbc:TaxAmount currencyID="PEN">0.00</cbc:TaxAmount>
<cac:TaxSubtotal>
<cbc:TaxableAmount currencyID="PEN">36.00</cbc:TaxableAmount>
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
<cbc:Description>SABOR DE ORO 350MLXPQT</cbc:Description>
<cac:SellersItemIdentification>
<cbc:ID>000099</cbc:ID>
</cac:SellersItemIdentification>
</cac:Item>
<cac:Price>
<cbc:PriceAmount currencyID="PEN">12.00</cbc:PriceAmount>
</cac:Price>
</cac:InvoiceLine>
<cac:InvoiceLine>
<cbc:ID>2</cbc:ID>
<cbc:InvoicedQuantity unitCode="NIU" unitCodeListID="UN/ECE rec 20" unitCodeListAgencyName="United Nations Economic Commission for Europe">3.00</cbc:InvoicedQuantity>
<cbc:LineExtensionAmount currencyID="PEN">36.00</cbc:LineExtensionAmount>
<cac:PricingReference>
<cac:AlternativeConditionPrice>
<cbc:PriceAmount currencyID="PEN">12.00</cbc:PriceAmount>
<cbc:PriceTypeCode listName="Tipo de Precio" listAgencyName="PE:SUNAT" listURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo16">01</cbc:PriceTypeCode>
</cac:AlternativeConditionPrice>
</cac:PricingReference>
<cac:TaxTotal>
...
</cac:TaxTotal>
<cac:Item>
<cbc:Description>BIG COLA NEGRA350MLXPQT</cbc:Description>
<cac:SellersItemIdentification>
<cbc:ID>000096</cbc:ID>
</cac:SellersItemIdentification>
</cac:Item>
<cac:Price>
...
</cac:Price>
</cac:InvoiceLine>
<cac:InvoiceLine>
<cbc:ID>3</cbc:ID>
<cbc:InvoicedQuantity unitCode="NIU" unitCodeListID="UN/ECE rec 20" unitCodeListAgencyName="United Nations Economic Commission for Europe">1.00</cbc:InvoicedQuantity>
<cbc:LineExtensionAmount currencyID="PEN">12.00</cbc:LineExtensionAmount>
<cac:PricingReference>
<cac:AlternativeConditionPrice>
<cbc:PriceAmount currencyID="PEN">12.00</cbc:PriceAmount>
<cbc:PriceTypeCode listName="Tipo de Precio" listAgencyName="PE:SUNAT" listURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo16">01</cbc:PriceTypeCode>
</cac:AlternativeConditionPrice>
</cac:PricingReference>
<cac:TaxTotal>
...
</cac:TaxTotal>
<cac:Item>
<cbc:Description>KR NARANJA 350MLXPQT</cbc:Description>
<cac:SellersItemIdentification>
<cbc:ID>000088</cbc:ID>
</cac:SellersItemIdentification>
</cac:Item>
<cac:Price>
<cbc:PriceAmount currencyID="PEN">12.00</cbc:PriceAmount>
</cac:Price>
</cac:InvoiceLine>
<cac:InvoiceLine>
<cbc:ID>4</cbc:ID>
<cbc:InvoicedQuantity unitCode="NIU" unitCodeListID="UN/ECE rec 20" unitCodeListAgencyName="United Nations Economic Commission for Europe">1.00</cbc:InvoicedQuantity>
<cbc:LineExtensionAmount currencyID="PEN">12.00</cbc:LineExtensionAmount>
<cac:PricingReference>
<cac:AlternativeConditionPrice>
<cbc:PriceAmount currencyID="PEN">12.00</cbc:PriceAmount>
<cbc:PriceTypeCode listName="Tipo de Precio" listAgencyName="PE:SUNAT" listURI="urn:pe:gob:sunat:cpe:see:gem:catalogos:catalogo16">01</cbc:PriceTypeCode>
</cac:AlternativeConditionPrice>
</cac:PricingReference>
<cac:TaxTotal>
<cbc:TaxAmount currencyID="PEN">0.00</cbc:TaxAmount>
<cac:TaxSubtotal>
<cbc:TaxableAmount currencyID="PEN">12.00</cbc:TaxableAmount>
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
<cbc:Description>KR PIÑA 350MLXPQT</cbc:Description>
<cac:SellersItemIdentification>
<cbc:ID>000090</cbc:ID>
</cac:SellersItemIdentification>
</cac:Item>
<cac:Price>
<cbc:PriceAmount currencyID="PEN">12.00</cbc:PriceAmount>
</cac:Price>
</cac:InvoiceLine>
</Invoice>""")

json_str = json.dumps(obj, indent=4)

# print(json_str)
newObj = json.loads(json_str)

obje = newObj['Invoice'] # base

CantArt = obje['cbc:LineCountNumeric']

numero = int(CantArt)
print("CantArt (cantidad de productos): ", CantArt)

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

    # print('-------')
