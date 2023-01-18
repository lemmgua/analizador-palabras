x = input()
while not x.isalpha():
    print("\x1b[1;33m" + "Error")
    x = input()