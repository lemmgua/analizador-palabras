<<<<<<< Updated upstream:Analizadordepalabras.py
from time import *
import os

'''preparar una lista con todas las vocales
elegir la palabra a analizar
hacer un For Loop por las letras y comparar si son vocales'''

#window = tk.Tk()

'''Forma muyyy simple
import pyphen
b = input("Dime una palabra:\n")
a = pyphen.Pyphen(lang='ca')
print(a.inserted(b))'''

continueSelect = 1

while continueSelect == 1:
    
    sleep(0.3)
    n = input("Dime una palabra:\n")
    nSplitList = []

    vocales = "aeiou"

    def isVocal(letter):
        return (letter in vocales)
        

    for i in range(0, len(n)):
        if i+2 < len(n) and isVocal(n[i+1]) == False and isVocal(n[i+2]) == False:
            nSplitList.append(n[i-1:i+2])
        elif i+1 != len(n) and n[-1] == n[i+1] and isVocal(n[-1]) == False:
            nSplitList.append(n[i-1:])
        elif n[i] == "í":
            nSplitList.append(n[i])
        elif isVocal(n[i]):
            nSplitList.append(n[i-1:i+1])       
    print(" - ".join(nSplitList))
    sleep(1)

    continueSelect = int(input("¿Desea continuar?\nSi: 1\nNo: 0\n"))
    if(continueSelect == 0):
        sleep(0.3)
        print("Finalizado")
        break
    if continueSelect == 1 or continueSelect == 0:
        continue
    else:
        while continueSelect != 1 or continueSelect != 0:
            continueSelect = int(input("El valor introducido no es válido. Introduce otro\nSi: 1\nNo: 0\n"))
            if continueSelect is 1 or continueSelect is 0:
                break

def silabas(palabra):
    nSplitList = []

    vocales = "aeiou"

    def isVocal(letter):
        return (letter in vocales)
    
    for i in range(0, len(n)):
        if i+2 < len(n) and isVocal(n[i+1]) == False and isVocal(n[i+2]) == False:
            nSplitList.append(n[i-1:i+2])
        elif i+1 != len(n) and n[-1] == n[i+1] and isVocal(n[-1]) == False:
            nSplitList.append(n[i-1:])
        elif n[i] == "í":
            nSplitList.append(n[i])
        elif isVocal(n[i]):
            nSplitList.append(n[i-1:i+1]) 
    
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
    n = input("Dime una palabra:\n")
    nSplitList = []

    vocales = "aeiou"

    def isVocal(letter):
        return (letter in vocales)
        

    for i in range(0, len(n)):
        if i+2 < len(n) and isVocal(n[i+1]) == False and isVocal(n[i+2]) == False:
            nSplitList.append(n[i-1:i+2])
        elif i+1 != len(n) and n[-1] == n[i+1] and isVocal(n[-1]) == False:
            nSplitList.append(n[i-1:])
        elif isVocal(n[i]):
            nSplitList.append(n[i-1:i+1])
    print(" - ".join(nSplitList))
    sleep(1)
    continueSelect = int(input("¿Desea continuar?\nSi: 1\nNo: 0\n"))
    if(continueSelect == 0):
        sleep(0.3)
        print("Finalizado")
        break
    if continueSelect == 1 or continueSelect == 0:
        continue
    else:
        while continueSelect != 1 or continueSelect != 0:
            continueSelect = int(input("El valor introducido no es válido. Introduce otro\nSi: 1\nNo: 0\n"))
            if continueSelect is 1 or continueSelect is 0:
                break'''
>>>>>>> Stashed changes:Analizador de palabras.py
