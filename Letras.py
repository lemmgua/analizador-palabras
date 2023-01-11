import re

def infoLetras(palabra):
    nVocales = len(re.findall("[aeiouÁ-ú]", palabra))
    letras = {}
    [letras.update({i: 0}) for i in palabra]
    [letras.update({i: letras[i]+1}) for i in palabra]
    return {
        "longitud": len(palabra),
        "vocales": nVocales,
        "consonantes": (len(palabra)-nVocales),
        "letras": letras
    }

[print(i + ":", infoLetras("Caralho")[i]) for i in infoLetras("caralho")]