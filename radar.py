velocidade=int(input("qual e a velocidade atual do carro?"))
if velocidade > 80:
    print("voce esta multado")
multa=(velocidade-80)*7
print("voce devera pagar {} reais".format(multa))

