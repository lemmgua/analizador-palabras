import re

def silabas(palabraAAnalizar):
    palabra = palabraAAnalizar
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
    
    return silabas


if __name__ == "__main__":
    print(silabas(input("carlos los taxis:\n")))