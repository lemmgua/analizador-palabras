import re
from Letras import infoLetras

palabra = input("¡Bienvenido!\nPor favor, introducza una palarba:\n")
acentos = ["sobreesdrújula", "esdrújula", "plana", "aguda"]
info = infoLetras(palabra)
split = ""
if (info["vocales"] == info["consonantes"]):
    split = [palabra[i:i+2] for i in range(0, len(palabra), 2)]

for i in split.reverse():
    if (len(re.findall("[Á-ú]", i) )> 0):
        if i > 3:
            print(acentos[3])
        else:
            print(acentos[i])