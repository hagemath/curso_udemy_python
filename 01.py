lista_palavras = []
while True:
    lista_palavras.append(str(input("Quer adicionar qual palavra? ")))

    continuar = int(input("Deseja adicionar mais palavras? [1- Sim] [0 - Não]"))
    if continuar == 0:
        for i in lista_palavras:
            if len(i) > 4:
                print(i)
                break