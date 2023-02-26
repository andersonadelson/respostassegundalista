num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 + num3 or num2 > num1 + num3 or num3 > num1 + num2:
    print("Pelo menos um dos números é maior que a soma dos outros dois!")
else:
    print("Nenhum dos números é maior que a soma dos outros dois.")