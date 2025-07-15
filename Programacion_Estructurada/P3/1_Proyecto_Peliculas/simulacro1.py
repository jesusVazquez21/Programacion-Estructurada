Lista=[]
if len(Lista) == 0:
    resp=True
    while resp:
        Lista.append(input("Dame una palabra o frase: ").upper())
        resp=input("¿Desea solicitar otra frase? (SI/NO): ").lower().strip()
        if resp=="no":
            resp=False
    print(Lista)