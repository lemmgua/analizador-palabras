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
    nucleos = []
    vocales = "aeiouáàéèíóòú"

    def isVocal(letter):
        return (letter in vocales)
    
    """ for i in range(len(palabra)):
        if i+2 < len(palabra) and isVocal(palabra[i+1]) == False and isVocal(palabra[i+2]) == False:
            nSplitList.append(palabra[i-1:i+2])
        elif i+1 != len(palabra) and palabra[-1] == palabra[i+1] and isVocal(palabra[-1]) == False:
            nSplitList.append(palabra[i-1:])
        elif palabra[i] == "í":
            nSplitList.append(palabra[i])
        elif isVocal(palabra[i]):
            nSplitList.append(palabra[i-1:i+1])"""

    return nucleos

if __name__ == "__main__":
    print(silabas(input("Dame una palabra\n")))