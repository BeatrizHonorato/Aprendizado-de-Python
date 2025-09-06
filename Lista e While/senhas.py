senha = 'python123'

numero = str(input("Insira a senha correta: "))

while senha != numero:
    print("Resposta Errada!")
    numero = str(input("Insira a senha correta: "))
print("Resposta correta!")
