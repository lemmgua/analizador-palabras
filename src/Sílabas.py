import re, numpy as np

def silabas(palabra):
    #digrafs = ("rr","l·l", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx")
    digrafs = np.array(["rr", "ss", "sc", "ix", "tl", "tll", "tj", "tg", "tm", "tn", "tx", "nj", "ps", "ll", "ny", "gu", "qu", "l·l", "rl", "nl", "lv", "st", "mb"])
    silabas = []
    
    #consonante o unidad consonántica seguida de una vocal
    #ll, ny, gu y qu seguida de vocal es una sola sílaba

    #utilizar regex para detectar las reglas
    if (len(re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)) > 0):
        silabas = re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)
    elif (len(re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]|[b-df-hj-np-tv-xz]{1,2}[aeiou]", palabra)) > 0):
        silabas = re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]|[b-df-hj-np-tv-xz]{1,2}[aeiou]", palabra)
    for i in range(len(silabas)):
        for j in digrafs:
            if silabas[i].startswith(j):
                silabas[i-1] += silabas[i][0]
                silabas[i] = silabas[i][1:]
    silabas[-1] += palabra[-1] if silabas[-1][-1] != palabra[-1] else ""

    return silabas

if __name__ == "__main__":
    print(silabas(input("Dame una palabra:\n")))