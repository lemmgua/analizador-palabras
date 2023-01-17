import re

def silabas(palabra):
    consonantes = "[b-df-hj-np-tv-xz]"
    vocales = "[aeiou]"
    #consonante o unidad consonántica seguida de una vocal
    #ll, ny, gu y qu seguida de vocal es una sola sílaba

    #utilizar regex para detectar las reglas
    return re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]|[b-df-hj-np-tv-xz]{1,2}[aeiou]", palabra)

print(silabas(input("Dame una palabra\n")))
