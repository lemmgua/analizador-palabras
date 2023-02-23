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
            "crecientes": re.findall("[iu][aeo]", palabra) if re.search("[iu][aeo][iu]", palabra) == None else "",
            "decrecientes": re.findall("[aeiou][iu]", palabra) if re.search("[iu][aeo][iu]", palabra) == None else ""
        },
        "triptongos": re.findall("[iu][aeo][iu]", palabra),
        "hiatos": re.findall("[aeo]{2}", palabra),
        "acentos": (re.findall("[\u00C0-\u00FF]", palabra)),
        "diéresis": re.findall("[ïü]{1}", palabra),
        "letras": letras
    }

@eel.expose
def silabas(palabraAAnalizar):
    '''Devuelve la palabra separada en sílabas'''
    palabra = palabraAAnalizar
    #digrafs = np.array(["pt", "rr", "rd", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx", "nj", "ps", "ll", "ny", "gu", "qu", "l·l", "rl", "nz"])
    silabas = []
    busqueda = None
    #acentos -> \u00C0-\u00FF
    #sacar valor ascii de letra -> ord("{letra}")
    #sacar letra de valor ascii -> chr({valor})
    #ARREGLAR -> etíop
    while (len(palabra) > 0):
        try:
            if (re.search("^trans", palabra)):
                busqueda = re.search("^trans", palabra)
            elif (re.search("^des", palabra)):
                busqueda = re.search("^des", palabra)
            elif (re.search("^in", palabra)):
                busqueda = re.search("^in", palabra)
            #CCVC - [plat - ja] nyeria
            elif (re.search("^[b-df-hj-np-tv-xz\u00E7]{2}[aeiou][b-df-hj-np-tv-xz\u00E7]", palabra) and re.search("^[b-df-hj-np-tv-xz\u00E7]{2}[aeiou][b-df-hj-np-tv-xz\u00E7][aeiou]", palabra) == None):
                busqueda = re.search("^[b-df-hj-np-tv-xz\u00E7]{2}[aeiou][b-df-hj-np-tv-xz\u00E7]", palabra)
            #CVCC - [comp - ta - dor]
            elif (re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7]{2}", palabra) and re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7]{2}[aeiou\u00C0-\u00FF]", palabra) == None):
                busqueda = re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7]{2}", palabra)
            #CVVC - caut
            elif (re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou]{2}[b-df-hj-np-tv-xz\u00E7]", palabra) and re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou]{2}[b-df-hj-np-tv-xz\u00E7][aeiou]", palabra) == None):
                busqueda = re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou]{2}[b-df-hj-np-tv-xz\u00E7]", palabra)
            #CVC
            elif (re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7]", palabra) != None and re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF]", palabra) == None):
                busqueda = re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7]", palabra)
            #VCV
            #elif (re.search("^[aeiou][b-df-hj-np-tv-xz][aeiou]", palabra) != None):
            #    busqueda = re.search("^[aeiou][b-df-hj-np-tv-xz][aeiou]", palabra)
            #CCV
            elif (re.search("^[b-df-hj-np-tv-xz\u00E7]{2}[aeiou]|^[b-df-hj-np-tv-xz\u00E7]{2}[aeiou\u00C0-\u00FF][iu]", palabra) != None):
                busqueda = re.search("^[b-df-hj-np-tv-xz\u00E7]{2}[aeiou]|^[b-df-hj-np-tv-xz\u00E7]{2}[aeiou\u00C0-\u00FF][iu]", palabra)
            #VC
            elif (re.search("^[aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7]", palabra) and re.search("^[aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF]", palabra) == None):
                busqueda = re.search("^[aeiou\u00C0-\u00FF][b-df-hj-np-tv-xz\u00E7]", palabra)
            #CVV
            elif (re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00FC][iu\u00ED]|^[b-df-hj-np-tv-xz\u00E7][iu\u00ED][aeiou\u00FC]", palabra) and re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF]{2}[b-df-hj-np-tv-xz\u00E7]", palabra) == None):
                busqueda = re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou\u00FC][iu\u00ED]|^[b-df-hj-np-tv-xz\u00E7][iu][aeiou\u00FC]", palabra)
            #CV - tíop
            elif (re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou][iu]|^[b-df-hj-np-tv-xz\u00E7][iu][aeiou]|^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF\u00ED]", palabra) != None):
                busqueda = re.search("^[b-df-hj-np-tv-xz\u00E7][aeiou][iu]|^[b-df-hj-np-tv-xz\u00E7][iu][aeiou]|^[b-df-hj-np-tv-xz\u00E7][aeiou\u00C0-\u00FF\u00ED]", palabra)
            #Diftong Decreixent
            elif (re.search("^[aeiou][iu]", palabra)):
                busqueda = re.search("^[aeiou][iu]", palabra)
            #Diftong Creixent
            elif (re.search("^[iu][aeo]", palabra)):
                busqueda = re.search("^[iu][aeo]", palabra)
            #V
            elif (re.search("^[aeiou\u00C0-\u00FF]", palabra)):
                busqueda = re.search("^[aeiou\u00C0-\u00FF]", palabra)
            #Guión (-)
            elif (re.search("^-", palabra)):
                guion = re.search("^-", palabra)
                busqueda = re.search(palabra[guion.start():], palabra)
            #Apostrofe (')
            elif (re.search("^\'", palabra)):
                apost = re.search("^\'", palabra)
                busqueda = re.search(palabra[apost.start():], palabra)
            """ #Hiatos
            elif (re.search("^[aeo]{2}", palabra)):
                busqueda = re.search("^[aeo]", palabra) """
            silabas.append(palabra[busqueda.start():busqueda.end()])
            palabra = palabra[busqueda.end():]
            
        except Exception as e:
            print(e)
            break
    
    #Juntar consonantes solitarias
    """ for i, silaba in enumerate(silabas):
        #Si no encuentra vocales
        if (re.search("[aeiou]", silaba) == None):
            silabas[i-1] += silabas[i]
            del silabas[i] """
    
    """ for i, silaba in enumerate(silabas):
        if (re.search("[aeiou][iu]|[iu][aeiou]", silabas[i-1][-1]+silaba[0])):
            #Si encuentra diftongo
            silabas[i-1] += silabas[i]
            del silabas[i] """
    #Juntar dígrafos
    """ for i in range(len(silabas)):
        for j in digrafs:
            if silabas[i].startswith(j):
                silabas[i-1] += silabas[i][0]
                silabas[i] = silabas[i][1:] """

    #Unir dos consonantes - EXCEPCIÓN
    expecciones = np.array(["cl", "ll", "ny", "br"])
    for i, sil in enumerate(silabas):
        for exc in expecciones:
            try:
                #noc - lei -> if c == cl[0] and l == cl[1]
                if (sil[-1] == exc[0] and silabas[i+1][0] == exc[1]):
                    silabas[i+1] = sil[-1] + silabas[i+1]
                    silabas[i] = sil[:-1]
            except Exception:
                None
                
    #Elimina posibles "·" de las l·l
    for i in range(len(silabas)):
        search = re.search('[·*-\']', silabas[i])
        if (search):
            silabas[i] = silabas[i][:search.start()] + silabas[i][search.end():]

    return silabas

if __name__ == "__main__":
    eel.start("Index.html", size=(1000, 800))