import random
import time
computador=random.randint(0,10)
print("irei pensar em um numero de 0 a 10")
jogador=(input("em qual numero eu pesnei"))
print("Analisando sua escolha...")
time.sleep(3)
if jogador== computador:
    print("Parabens você ganhou")
else:
    print("você perdeu")



