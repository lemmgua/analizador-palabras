from time import *
import re

'''preparar una lista con todas las vocales
elegir la palabra a analizar
hacer un For Loop por las letras y comparar si son vocales'''

#window = tk.Tk()

'''Forma muyyy simple
import pyphen
b = input("Dime una palabra:\palabra")
a = pyphen.Pyphen(lang='ca')
print(a.inserted(b))'''

def silabas(palabra):
    nSplitList = []
    
    vocales = "aeiou"

    def isVocal(letter):
        return (letter in vocales)
    
    for i in range(0, len(palabra)):
        if (len(re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)) > 0):
            return re.findall(".*?[b-df-hj-np-tv-xz]{1}[aeiou]", palabra)
        if i+2 < len(palabra) and isVocal(palabra[i+1]) == False and isVocal(palabra[i+2]) == False:
            nSplitList.append(palabra[i-1:i+2])
        elif i+1 != len(palabra) and palabra[-1] == palabra[i+1] and isVocal(palabra[-1]) == False:
            nSplitList.append(palabra[i-1:])
        elif palabra[i] == "í":
            nSplitList.append(palabra[i])
        elif isVocal(palabra[i]):
            nSplitList.append(palabra[i-1:i+1]) 
        else:
            nSplitList.append(palabra[i])
    
    return nSplitList

print(" - ".join(silabas(input("Dame una palabra\n"))))