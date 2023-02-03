import re

def silabas(palabraAAnalizar):
    palabra = palabraAAnalizar
    silabas = []
    busqueda = None

    while (len(palabra) > 0):
        if (re.search("[b-df-hj-np-tv-xz]{2}[aeiou]{1}", palabra) != None):
            busqueda = re.search("[b-df-hj-np-tv-xz]{2}[aeiou]{1}", palabra)
        elif (re.search("[b-df-hj-np-tv-xz]{1}[aeiou]{1}", palabra) != None):
            busqueda = re.search("[b-df-hj-np-tv-xz]{1}[aeiou]{1}", palabra)
        silabas.append(palabra[busqueda.start():busqueda.end()])
        palabra = palabra[busqueda.end():]
    
    return silabas


if __name__ == "__main__":
    print(silabas(input("carlos los taxis:\n")))