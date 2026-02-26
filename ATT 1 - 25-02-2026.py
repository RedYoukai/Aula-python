import math

t = input ("Insira o tipo de operação a ser executada:\n1 - Soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - Radiciação\n6 - potência\n\n")
t = int(t)

if (t > 6) or (t < 1):
    print("Como você conseguiu errar isso? É só escolher um número de 1 a 6, cara, nn é difícil, sabe? E eu aposto que nem é a primeira vez que você tá executando esse código, e ele deu erro pq, aparentemente, J não é um número, né? Esse negócio é básico, tipo, é coisa que nem meu irmão erraria, e ele tem tipo, 2 meses de vida. Você se acha o engraçadão da turma? Tá todo mundo passando na sua frente enquanto você tá aqui, rindo de mim pq eu não consigo controlar sua vida. Adivinha, parceiro, você também não controla sua vida. Nesse exato momento alguém pode invadir sua casa e matar sua família toda e você nunca ia saber. Agora vai, vou crashar o código pra você tentar dnv. Dessa vez, tenta ver se você consegue agir como gente, tá? peça desculpas pra você mesmo. melhore.\n\n")
    input()
    exit()

if (t != 5): 
    a = input ("insira o primeiro valor: ")
    a = float(a)
    
    b = input ("Insira o segundo valor: ")
    b = float(b)
    
else:
    a = input ("insira o valor da raíz: ")
    a = float(a)

if (t==1):
    a = a+b
    print("O valor da soma foi ",a)

elif (t==2):
    a = a-b
    print("O valor da subtração foi ",a)

elif (t==3):
    a = a*b
    print("O valor da multiplicação foi ",a)

elif (t==4):
    a = a/b
    print("O valor da divisão foi ",a)

elif (t==5):
	a = math.sqrt(a)
	print("O valor da raíz foi ",a)
	
elif (t==6):
	a = a ** b
	print("O valor da potência foi ",a)
input()