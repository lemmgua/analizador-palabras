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
    #for i in palabra:
    #    letras.update({i: 0})
    [letras.update({i: letras[i]+1}) for i in palabra]
    #for i in palabra:
    #    letras.update({i: letras[i]+1})
    return {
        "longitud": len(palabra),
        "vocales": nVocales,
        "consonantes": (len(palabra)-nVocales),
        "diptongos": {
            "crecientes": re.findall("[iu][aeo]", palabra),
            "decrecientes": re.findall("[aeiou][iu]", palabra)
        },
        "triptongos": re.findall("[iu][aeo][iu]", palabra),
        "hiatos": re.findall("[aeo]{2}", palabra),
        "acentos": (len(re.findall("[Á-ú]", palabra))),
        "diéresis": re.findall("[ïü]{1}", palabra),
        "letras": letras
    }

@eel.expose
def silabas(palabraAAnalizar):
    palabra = palabraAAnalizar
    digrafs = np.array(["rr", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx", "nj", "ps", "ll", "ny", "gu", "qu", "l·l", "rl", "nz"])
    silabas = []
    busqueda = None

    while (len(palabra) > 0):
        try:
            #CVC
            if (re.search("^[b-df-hj-np-tv-xz]{1}[aeiou]{1}[b-df-hj-np-tv-xz]{2}", palabra) != None):
                busqueda = re.search("^[b-df-hj-np-tv-xz]{1}[aeiou]{1}[b-df-hj-np-tv-xz]{1}", palabra)
            #CCV
            elif (re.search("^[b-df-hj-np-tv-xz]{2}[aeiou]{1}", palabra) != None):
                busqueda = re.search("^[b-df-hj-np-tv-xz]{2}[aeiou]{1}", palabra)
            #CV
            elif (re.search("^[b-df-hj-np-tv-xz]{1}[aeiouÀ-ÿ]{1}", palabra) != None):
                busqueda = re.search("^[b-df-hj-np-tv-xz]{1}[aeiouÀ-ÿ]{1}", palabra)
            #VCV
            elif (re.search("^[aeiou]{1}[b-df-hj-np-tv-xz]{1}[aeiou]{1}", palabra) != None):
                busqueda = re.search("^[aeiou]{1}[b-df-hj-np-tv-xz]{1}", palabra)
            #VC
            elif (re.search("^[aeiouÀ-ÿ]{1}[b-df-hj-np-tv-xz]{2}", palabra) != None):
                busqueda = re.search("^[aeiouÀ-ÿ]{1}[b-df-hj-np-tv-xz]{1}", palabra)
            silabas.append(palabra[busqueda.start():busqueda.end()])
            palabra = palabra[busqueda.end():]
        
        except Exception as err:
            print(f"HA PETAO -> {err}")
            break
    
    #Juntar consonantes solitarias
    for i, silaba in enumerate(silabas):
        #Si no encuentra vocales
        if (re.search("[aeiou]", silaba) == None):
            silabas[i-1] += silabas[i]
            del silabas[i]
    
    for i in range(len(silabas)):
        for j in digrafs:
            if silabas[i].startswith(j):
                silabas[i-1] += silabas[i][0]
                silabas[i] = silabas[i][1:]

    #Elimina posibles "·" de las l·l
    for i in range(len(silabas)):
        search = re.search("·", silabas[i])
        if (search != None):
            silabas[i] = silabas[i][:search.start()] + silabas[i][search.end():]
    
    return silabas

eel.start("Index.html", size=(1000, 800))