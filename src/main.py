import re
from Letras import infoLetras

if __name__ == "__main__":
    palabra = input("¡Bienvenido!\nPor favor, introducza una palarba:\n")
    acentos = ["sobreesdrújula", "esdrújula", "plana", "aguda"]
    info = infoLetras(palabra)
    split = ""
    if (info["vocales"] == info["consonantes"]):
        split = [palabra[i:i+2] for i in range(0, len(palabra), 2)]