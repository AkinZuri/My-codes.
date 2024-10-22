def reservar(sala, fileira, assento):
    if sala[fileira-1][assento-1] == 0:
        sala[fileira-1][assento-1] = 1
        print(f"Você reservou a poltrona{assento} da fileira{fileira}!")
    else:
        print("Este lugar já está reservado!")

def cancelar(sala, fileira, assento):
    if sala[fileira-1][assento-1] == 1:
        sala[fileira-1][assento-1] = 0
        print(f"Você cancelou a reserva da {assento}° poltrona.")
    else:
        print("este lugar não está reservado")


def exibir_sala(sala):
    for fila in sala:
        print(" ".join(map(str,fila)))

sala = [[0]*8 for fila in range (5)] 

print("MAPA DAS POLTRONAS:")
exibir_sala(sala)

def main():    
    fileira = int(input("Qual fileira você deseja reservar?"))
    assento = int(input("Qual assento você deseja reservar?"))
    print("O que você quer fazer?\nDigite 1. para AGENDAR \n2. para CANCELAR\n")
    menu = int(input())
    if menu == 1:
        reservar(sala, fileira, assento)
    elif menu == 2:
        cancelar(sala, fileira, assento)
    else:
        print("ESSE COMANDO NÂO EXISTE!")        
    
while True:
    main()
    exibir_sala(sala)                     
   