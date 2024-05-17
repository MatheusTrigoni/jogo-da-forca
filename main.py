from os import system
from time import sleep
from getpass import getpass

def display():
    global tentativas
    system("cls")
    boneco()
    for i in palavraJogo:
        print(i, end=' ' if i != ' ' else '')
    print(f"\n\nTentativas: {tentativas}\n")

    print("Letras tentadas: ", end='')
    for i in letrasTentadas:
        print(i, end=' ')
    print()

def boneco():
    global tentativas
    print("_______")
    print("|     |")
    if tentativas == 6:
        print("|       ")
        print("|       ")
        print("|       ")
    elif tentativas == 5:
        print("|     O ")
        print("|       ")
        print("|       ")
    elif tentativas == 4:
        print("|     O ")
        print("|     | ")
        print("|       ")
    elif tentativas == 3:
        print("|     O ")
        print("|    /| ")
        print("|       ")
    elif tentativas == 2:
        print("|     O ")
        print("|    /|\\")
        print("|        ")
    elif tentativas == 1:
        print("|     O ")
        print("|    /|\\")
        print("|    / ")
    else:
        print("|     O")
        print("|    /|\\")
        print("|    / \\")
    print("|     \n")

def converte_letra(letra: str):
    if letra in ('á', 'ã', 'â', 'Á', 'Ã', 'Â'):
        return 'a'
    elif letra in ('é', 'ê', 'É', 'Ê'):
        return 'e'
    elif letra in ('í', 'î', 'Í', 'Î'):
        return 'i'
    elif letra in ('ó', 'õ', 'ô', 'Ó', 'Õ', 'Ô'):
        return 'o'
    elif letra in ('ú', 'û', 'Ú', 'Û'):
        return 'u'
    elif letra in ('ç', 'Ç'):
        return 'c'
    return letra

#async def timer(tempo):
#    print(f"Tempo restante: {tempo}...")
#    if tempo == 0:
#       return tempo
#    return timer(tempo - 1)
        
def jogo_da_forca():
    system("cls")
    palavra = getpass(prompt="Digite a palavra a ser descoberta: ")
    for i in palavra:
        palavraRef.append(i)
        if i == ' ':
            palavraJogo.append(' ')
        else:
            palavraJogo.append('_')
    
    global tentativas
    #for i in palavra:
    #    if i != ' ':
    #        tentativas += 1

    while tentativas > 0:
        display()
        if '_' not in palavraJogo:
            print(f'\nVocê venceu! A palavra era "{palavra}".\n')
            return

        #await timer(10)
        tentativa = input("\nDigite uma letra (ou a palavra): ")

        if tentativa == palavra:
            for i in palavraRef:
                index = palavraRef.index(i)
                if palavraJogo[index] == '_':
                    palavraRef[index] = '_'
                    palavraJogo[index] = i
            
            display()
            print(f'\nVocê venceu! A palavra era "{palavra}".\n')
            return
        elif len(tentativa) > 1:
            display()
            print(f'\nVocê perdeu! A palavra era "{palavra}".\n')
            return
        elif tentativa in letrasTentadas:
            print("\nVocê já tentou essa letra!")
            sleep(1)
            continue
        elif tentativa == '':
            continue

        errou_letra = True
        for i in palavraRef:
            if converte_letra(tentativa).lower() == converte_letra(i).lower():
                errou_letra = False
                index = palavraRef.index(i)
                palavraRef[index] = '_'
                palavraJogo[index] = i
        
        if tentativa not in letrasTentadas and len(tentativa) == 1:
            letrasTentadas.append(tentativa.lower())

        if errou_letra:
            tentativas -= 1

    display()
    print(f'\nVocê perdeu! A palavra era "{palavra}".\n')

while True:
    # Variáveis globais
    palavraRef = []
    palavraJogo = []
    letrasTentadas = []
    tentativas = 6

    jogo_da_forca()

    while True:
        continuar = input("Continuar jogando? S/N ").upper()
        if continuar == 'S':
            break
        elif continuar == 'N':
            system("cls")
            exit()
        else:
            print("\nOpção inválida, tente novamente.\n")