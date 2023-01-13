import re


patronAcentos = "[Á-ú]"

palabra = input("Dame una palabra:\n")

print(len(re.findall("[Á-ú]", palabra)), "acentos")
print(len(re.findall("[aeiouÁ-ú]", palabra)), "vocales")
if re.findall("[Á-ú]n$|[Á-ú]s$|[Á-ú]$", palabra):
    print("Aguda")