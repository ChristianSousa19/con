s=float(input("qual é o seu salario?"))
a=(s*10/100)+s
i=(s*15/100)+s
if s<=1250.0:
    print("seu novo salario sera {} ".format(i))
else:
    print("seu novo salario sera {} ".format(a))