import difflib

def comparar_strings(s1, s2):
    ratio = difflib.SequenceMatcher(None, s1, s2).ratio()
    return ratio * 100

# Ejemplos de comparación
texto1 = 'VOLT MACA 300ML XPQT'
texto2 = ' VOLTMACAPQT12'

similitud = comparar_strings(texto1, texto2)
print(f'Similitud: {similitud:.2f}%')