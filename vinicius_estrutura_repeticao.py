
num1 = int(input("Digite o o primeiro número: "))
num2 = int(input("Digite o o segundo número: "))

 
if num1 > num2:
    num1,num2 = num2,num1 #troca de posição 


    print(f"Números entre {num1} e {num2}:")
    for i in range(num1 +1, num2):
        print(i)
