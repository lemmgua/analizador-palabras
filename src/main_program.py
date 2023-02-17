import eel, re, numpy as np, unidecode

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
    [letras.update({i: 0}) for i in palabra if i.isalpha()]
    #for i in palabra:
    #    letras.update({i: 0})
    [letras.update({i: letras[i]+1}) for i in palabra if i.isalpha()]
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
    '''Devuelve la palabra separada en sílabas'''
    palabra = unidecode.unidecode(palabraAAnalizar)
    digrafs = np.array(["pt", "rr", "rd", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx", "nj", "ps", "ll", "ny", "gu", "qu", "l·l", "rl", "nz"])
    silabas = []
    busqueda = None

    while (len(palabra) > 0):
        try:
            if (re.search("^trans", palabra)):
                busqueda = re.search("^trans", palabra)
            elif (re.search("^des", palabra)):
                busqueda = re.search("^des", palabra)
            #CVCC
            #elif (re.search("^[b-df-hj-np-tv-xz][aeiou][b-df-hj-np-tv-xz]{3}|[b-df-hj-np-tv-xz][aeiou][b-df-hj-np-tv-xz]{2}", palabra)):
            #    busqueda = re.search("^[b-df-hj-np-tv-xz][aeiou][b-df-hj-np-tv-xz]{2}", palabra)
            #CVC
            elif (re.search("^[b-df-hj-np-tv-xz][aeiou][b-df-hj-np-tv-xz]{2}|^[b-df-hj-np-tv-xz][aeiou][b-df-hj-np-tv-xz]", palabra) != None and re.search("^[b-df-hj-np-tv-xz][aeiou][b-df-hj-np-tv-xz][aeiou]", palabra) == None):
                busqueda = re.search("^[b-df-hj-np-tv-xz]{1}[aeiou]{1}[b-df-hj-np-tv-xz]{1}", palabra)
            #VCV
            elif (re.search("^[aeiou][b-df-hj-np-tv-xz][aeiou]", palabra) != None):
                busqueda = re.search("^[aeiou]", palabra)
            #VC
            elif (re.search("^[aeiou][b-df-hj-np-tv-xz]{2}|^[aeiou][b-df-hj-np-tv-xz]", palabra) and re.search("^[aeiou][b-df-hj-np-tv-xz][aeiou]", palabra) == None):
                busqueda = re.search("^[aeiou][b-df-hj-np-tv-xz]", palabra)
            #CCV
            elif (re.search("^[b-df-hj-np-tv-xz]{2}[aeiouàèéíòóú]{1}", palabra) != None):
                busqueda = re.search("^[b-df-hj-np-tv-xz]{2}[aeiouàèéíòóú]{1}", palabra)
            #CV
            elif (re.search("^[b-df-hj-np-tv-xz][aeiou][iu]|^[b-df-hj-np-tv-xz][iu][aeiou]|^[b-df-hj-np-tv-xz]{1}[aeiou]{1}", palabra) != None):
                busqueda = re.search("^[b-df-hj-np-tv-xz][aeiou][iu]|^[b-df-hj-np-tv-xz][iu][aeiou]|^[b-df-hj-np-tv-xz]{1}[aeiou]{1}", palabra)
            #V
            elif (re.search("^[aeiou]", palabra)):
                busqueda = re.search("^[aeiou]", palabra)
            """ #Hiatos
            elif (re.search("^[aeo]{2}", palabra)):
                busqueda = re.search("^[aeo]", palabra) """
            """ #Diftong Creixent
            elif (re.search("^[iu][aeo]", palabra)):
                busqueda = re.search("^[iu][aeo]", palabra)
            #Diftong Decreixent
            elif (re.search("^[aeiou][iu]", palabra)):
                busqueda = re.search("^[aeiou][iu]", palabra) """
            silabas.append(palabra[busqueda.start():busqueda.end()])
            palabra = palabra[busqueda.end():]
        
        except AttributeError:
            if not busqueda:
                None
            break
    
    #Juntar consonantes solitarias
    for i, silaba in enumerate(silabas):
        #Si no encuentra vocales
        if (re.search("[aeiou]", silaba) == None):
            silabas[i-1] += silabas[i]
            del silabas[i]
    
    """ for i, silaba in enumerate(silabas):
        if (re.search("[aeiou][iu]|[iu][aeiou]", silabas[i-1][-1]+silaba[0])):
            #Si encuentra diftongo
            silabas[i-1] += silabas[i]
            del silabas[i] """
    #Juntar dígrafos
    for i in range(len(silabas)):
        for j in digrafs:
            if silabas[i].startswith(j):
                silabas[i-1] += silabas[i][0]
                silabas[i] = silabas[i][1:]

    #Unir dos consonantes - EXCEPCIÓN
    expecciones = np.array(["cl", "ll", "ny"])
    for i, sil in enumerate(silabas):
        for exc in expecciones:
            try:
                #noc - lei -> if c == cl[0] and l == cl[1]
                if (sil[-1] == exc[0] and silabas[i+1][0] == exc[1]):
                    silabas[i+1] = sil[-1] + silabas[i+1]
                    silabas[i] = sil[:-1]
            except:
                None
                
    #Elimina posibles "·" de las l·l
    for i in range(len(silabas)):
        search = re.search("[·*]", silabas[i])
        if (search != None):
            silabas[i] = silabas[i][:search.start()] + silabas[i][search.end():]
    
    
    return silabas

if __name__ == "__main__":
    eel.start("Index.html", size=(1000, 800))