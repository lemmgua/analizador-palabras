import re

def infoLetras(palabra):
    '''
    Devuelve un diccionario con información sobre la
    palabra proporcionada
    
    Parametros:
        palabra (str)

    Devuelve:
        diccionario (dict)
    
    >>> infoletras("palabra")
    {
        "longitud": 7,
        "vocales": 3,
        "consonantes": 4,
        "acentos": 0,
        "letras": {
            "p": 1,
            "a": 3,
            "l": 1,
            "b": 1,
            "r": 1
        }
    }
    '''
    nVocales = len(re.findall("[aeiouÁ-ú]", palabra))
    letras = {}
    [letras.update({i: 0}) for i in palabra]
    [letras.update({i: letras[i]+1}) for i in palabra]
    return {
        "longitud": len(palabra),
        "vocales": nVocales,
        "consonantes": (len(palabra)-nVocales),
        "diptongos": re.findall("[aeiou]{2}", palabra),
        "triptongos": re.findall("[aeiou]{3}", palabra),
        "acentos": (len(re.findall("[Á-ú]", palabra))),
        "letras": letras
    }

print(infoLetras("caedro")["triptongos"])