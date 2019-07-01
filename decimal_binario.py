quociente = input("Digite um numero: ")
bina = ''
while True:
    resto = quociente % 2
    quociente = quociente // 2

    convert_str = str(resto)
    bina = bina + convert_str

    if quociente == 0:
        break

print(bina[::-1])
