import re, numpy as np

def silabas(palabra):
    digrafs = np.array(["rr", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx", "nj", "ps", "ll", "ny", "gu", "qu", "l·l"])
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

print(" - ".join(silabas(input("Dame una palabra\n"))))
