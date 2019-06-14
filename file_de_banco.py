ultimo = 10
fila = list(range(1,ultimo+1))
count = int(0)
while True:
    print("\n Existem % clientes na fila" % len(fila))
    print("Fila atual: " , fila)
    print("Digite F para adicionar um cliente ao fim da lista,")
    print("Ou A para realizar o atendimento um cliente (S para sair)")
    operacao = "AAAAAFFS"
    if operacao [count: count+1] == "A":
        if(len(fila))>0:
            atendido = fila.pop(0)
            print("Cliente % d atendido" % atendido)
        else:
            print("Fila vazia! Ninguem para atender")
    elif operacao [count: count+1] == "F":
        ultimo = ultimo + 1 #incrementa o ticket novo
        fila.append(ultimo)
    elif operacao [count: count+1] == "S":
        break
    else:
        print("Operacao invalida! Digite apenas F, A e S!")
    count = count + 1
    
    
