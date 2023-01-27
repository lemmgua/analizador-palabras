import eel, re, numpy as np

eel.init("web")

@eel.expose
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
        "diéresis": 0,
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

@eel.expose
def silabas(palabra):
    #digrafs = ("rr","l·l", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx")
    digrafs = np.array(["rr", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx", "nj", "ps", "ll", "ny", "gu", "qu", "l·l", "rl", "nz"])
    silabas = []
    
    #consonante o unidad consonántica seguida de una vocal
    #ll, ny, gu y qu seguida de vocal es una sola sílaba

    #utilizar regex para detectar las reglas
    if (len(re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)) > 0):
        silabas = re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)
    silabas = re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]|[b-df-hj-np-tv-xz]{1,2}[aeiou]", palabra)
    for i in range(len(silabas)):
        for j in digrafs:
            if silabas[i].startswith(j):
                silabas[i-1] += silabas[i][0]
                silabas[i] = silabas[i][1:]
    return silabas

eel.start("Index.html", size=(800, 600))