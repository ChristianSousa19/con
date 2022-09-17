v1=int(input("digiteo primeiro valor"))
v2=int(input("digite o segundo valor"))
v3=int(input("digite o terceiro valor"))
menor=v1
if v2<v3 and v2<v1:
    menor=v2
if v3<v1 and v3<v2:
    menor=v3
print("o menor valor e {}".format(menor))
maior=v3
if v2>v1 and v2>v3:
    maior=v2
if v1>v2 and v1>v3:
    maior=v1
print(" o maior valor valor {}".format(maior))
