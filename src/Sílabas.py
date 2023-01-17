import re

def silabas(palabra):
    consonantes = "[b-df-hj-np-tv-xz]"
    vocales = "[aeiou]"
    
    #consonante o unidad consonántica seguida de una vocal
    #ll, ny, gu y qu seguida de vocal es una sola sílaba

    #utilizar regex para detectar las reglas
    if (len(re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)) > 0):
        return re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)
    return re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]|[b-df-hj-np-tv-xz]{1,2}[aeiou]", palabra)

print(" - ".join(silabas(input("Dame una palabra\n"))))
