import re, numpy as np

def silabas(palabra):
    digrafs = np.array(["rr", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx", "nj", "ps", "ll", "ny", "gu", "qu", "l·l", "rl", "nl", "lv", "st", "mb", "tz"])
    silabas = []
    
    #consonante o unidad consonántica seguida de una vocal
    #ll, ny, gu y qu seguida de vocal es una sola sílaba

    #utilizar regex para detectar las reglas
    if (len(re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)) > 0):
        silabas = re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)
    elif (len(re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]|[b-df-hj-np-tv-xz]{1,2}[aeiou]", palabra)) > 0):
        silabas = re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]|[b-df-hj-np-tv-xz]{1,2}[aeiou]", palabra)
    
    #Separa según los dígrafos
    for i in range(len(silabas)):
        for j in digrafs:
            if silabas[i].startswith(j):
                silabas[i-1] += silabas[i][0]
                silabas[i] = silabas[i][1:]


    #Añadir la última letra en caso de que no esté
    silabas[-1] += palabra[-1] if silabas[-1][-1] != palabra[-1] else ""

    #Elimina posibles "·" de las l·l
    for i in range(len(silabas)):
        search = re.search("·", silabas[i])
        if (search != None):
            silabas[i] = silabas[i][:search.start()] + silabas[i][search.end():]

    return silabas

if __name__ == "__main__":
    print(silabas(input("Dame una palabra:\n")))