def soma():
    print("soma: ", N1+N2)
def subtracao():
    print("subtracao: ", N1-N2)
def multiplicacao():
    print("multiplicacao: ", N1*N2)
def divisao():
    print("divisao: ", N1/N2)
while True:
    print("1. soma")
    print("2. subtracao")
    print("3. multiplicacao")
    print("4. divisao")
    print("5. sair")
    escolha = input("Escolha um tipo: ")
    if escolha == "1":
        N1 = int(input())
        N2 = int(input())
        soma = N1+N2
        resultado = soma
        print (resultado)
        pass
    elif escolha == "2":
        N1 = int(input())
        N2 = int(input())
        subtracao = N1-N2
        resultado = subtracao
        print(resultado)
        pass
    elif escolha == "3":
        N1 = int(input())
        N2 = int(input())
        multiplicacao = N1*N2
        resultado = multiplicacao
        print(resultado)
        pass
    elif escolha == "4":
        N1 = int(input())
        N2 = int(input())
        divisao = N1/N2
        resultado = divisao
        print(resultado)
        pass
    elif escolha == "5":
        print("vai desistir agora mano?: ")
        break
    else:
        print("escolha invalida")