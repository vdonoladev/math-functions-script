from random import randint
from time import sleep
from datetime import date
from tkinter import*


def contagem():
    nome = input("Digite um nome e o programa irá contar as letras: ").strip()
    print("{} Tem {} letras".format(nome,len(nome)))

def palindromo():
    nome = input("Digite um nome e o programa irá verificar se é um palindrimo: ").strip().upper()
    sp = nome.split()
    juntar = ''.join(sp)
    texto = juntar[::-1]

    if juntar == texto:
        print("{} - {} ... É UM PALINDROMO !!".format(juntar,texto))
    else:
        print("{} - {} Não é um palindromo".format(juntar,texto))
def interface():
    janela = Tk()

    label = Label(janela,text='Primeiro número: ')
    label.place(x=50,y=100)

    label2 = Label(janela,text="Segundo número: ")
    label2.place(x=50,y=150)

    result = Label(janela,text='')
    result.place(x=200,y=250)

    entrada1 = Entry(janela)
    entrada1.place(x=150,y=100)

    entrada2 = Entry(janela)
    entrada2.place(x=150,y=150)

    botao1 = Button(janela, text='OK', width=25)
    botao1.place(x=150,y=200)

    janela.geometry('800x300')
    janela.mainloop()

def jogo():
    computador = randint(0,2)
    escolha = ("Pedra",'Papel','Tesoura')
    print("-="*20)
    print('BEM VINDO AO JOGO DE JOKENPO !!!')
    print("-="*20)
    print("Opcoes:\n[0] Pedra\n[1] Papel\n[2] Tesoura")
    jogador = int(input("Digite sua opção: "))
    print("")
    print("JOOOO")
    sleep(1)
    print("KEEEEN")
    sleep(1)
    print("POOOO !!!")
    print("-="*20)
    print("Computador jogou {} e você jogou {}".format(escolha[computador],escolha[jogador]))
    print("-="*20)

    if computador == 0:
        if jogador == 0:
            print("EMPATE!")
        elif jogador ==1:
            print("VOCÊ VENCEU !!")
        elif jogador ==2:
            print("COMPUTADOR VENCEU !!")
        else:
            print("Jogada inválida")
    elif computador ==1:
        if jogador == 0:
            print("COMPUTADOR VENCEU !!")
        elif jogador ==1:
            print("EMPATE!!")
        elif jogador ==2:
            print("JOGADOR VENCEU !!")
        else:
            print("Jogada inválida")
    elif computador ==2:
        if jogador ==0:
            print("VOCÊ VENCEU!!")
        elif jogador ==1:
            print("COMPUTADOR VENCEU !!")
        elif jogador ==2:
            print("EMPATE!!")
        else:
            print("Jogada inválida.")
    else:
        print("Opção inválida!!")

def ano():
    data = date.today().year
    print("Estamos no ano de {}".format(data))

def divisao():
    num = float(input("Digite o primeiro número a dividir: "))
    num2 = float(input("Digite o segundo número a dividir: "))

    result = num/num2
    print("O resultado da divisao de {} % {} é igual a {}".format(num,num2,result))

def multiplicacao():
    num = int(input("Digite o primeiro número a multiplicar: "))
    num2 = int(input("Digite o segundo número a multiplicar: "))

    result = num*num2
    print("O resultado da multiplição de {} x {} é igual a {}".format(num,num2,result))

def subtracao():
    num = int(input("Digite o primeiro número a subtrair: "))
    num2 = int(input("Digite o segundo número a subtrair: "))

    result = num-num2
    print("O resultado da subtração de {} - {} é igual a {}".format(num,num2,result))

def soma():
    num = int(input("Digite o primeiro número a somar: "))
    num2 = int(input("Digite o segundo número a somar: "))

    result = num+num2
    print('O resultado da operação {} + {} é igual a {} '.format(num,num2,result))

def tabuada():
    pergunta = int(input("Digite um número para ver a tabuada: "))

    for c in range(1,11):
        soma = pergunta * c
        print(pergunta, "X", c, "=", soma)

print("-="*30)
print("---- O PROGRAMA ---")
print("by: Víctor Donola (vdonoladev) :)")
print("-"*20)
print("Escolha:\n[1] Contar letras de um nome\n[2] Verificar se é palindromo\n[3] Uma interface gráfica de soma\n[4] Jogo de JOKENPO com o computador\n[5] Verificar o ano atual\n[6] Dividir dois números\n[7] Multiplicar um número\n[8] Subtrair dois números\n[9] Somar dois números\n[10] Ver a tabuada de um número")
escolha = int(input("Digite uma opção: "))

if escolha ==1:
    contagem()
elif escolha ==2:
    palindromo()
elif escolha ==3:
    interface()
elif escolha ==4:
    jogo()
elif escolha ==5:
    ano()
elif escolha ==6:
    divisao()
elif escolha ==7:
    multiplicacao()
elif escolha ==8:
    subtracao()
elif escolha ==9:
    soma()
elif escolha ==10:
    tabuada()
else:
    print("Escolha inválida")