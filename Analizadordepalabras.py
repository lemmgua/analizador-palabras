from time import *
import os

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
        if i+2 < len(palabra) and isVocal(palabra[i+1]) == False and isVocal(palabra[i+2]) == False:
            nSplitList.append(palabra[i-1:i+2])
        elif i+1 != len(palabra) and palabra[-1] == palabra[i+1] and isVocal(palabra[-1]) == False:
            nSplitList.append(palabra[i-1:])
        elif palabra[i] == "í":
            nSplitList.append(palabra[i])
        elif isVocal(palabra[i]):
            nSplitList.append(palabra[i-1:i+1]) 
    
    return nSplitList
    
#=======
from time import *

'''preparar una lista con todas las vocales
elegir la palabra a analizar
hacer un For Loop por las letras y comparar si son vocales'''

#window = tk.Tk()

#Forma muyyy simple xd B==D:
import pyphen
b = input()
a = pyphen.Pyphen(lang='es')
print(a.inserted(b))

'''continueSelect = 1

while continueSelect is 1:
    sleep(0.3)
    palabra = input("Dime una palabra:\palabra")
    nSplitList = []

    vocales = "aeiou"

    def isVocal(letter):
        return (letter in vocales)
        

    for i in range(0, len(palabra)):
        if i+2 < len(palabra) and isVocal(palabra[i+1]) == False and isVocal(palabra[i+2]) == False:
            nSplitList.append(palabra[i-1:i+2])
        elif i+1 != len(palabra) and palabra[-1] == palabra[i+1] and isVocal(palabra[-1]) == False:
            nSplitList.append(palabra[i-1:])
        elif isVocal(palabra[i]):
            nSplitList.append(palabra[i-1:i+1])
    print(" - ".join(nSplitList))
    sleep(1)
    continueSelect = int(input("¿Desea continuar?\nSi: 1\nNo: 0\palabra"))
    if(continueSelect == 0):
        sleep(0.3)
        print("Finalizado")
        break
    if continueSelect == 1 or continueSelect == 0:
        continue
    else:
        while continueSelect != 1 or continueSelect != 0:
            continueSelect = int(input("El valor introducido no es válido. Introduce otro\nSi: 1\nNo: 0\palabra"))
            if continueSelect is 1 or continueSelect is 0:
                break'''
>>>>>>> Stashed changes:Analizador de palabras.py
