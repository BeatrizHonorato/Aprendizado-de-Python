cont = 0
num = int(input("Insira um numero: "))

while cont <= num:
    print("{} x {} = {}".format(cont, num, (cont*num)))
    cont +=1
