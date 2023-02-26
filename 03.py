idade = int(input("Digite a idade da pessoa: "))
autorizacao_pais = input("A pessoa tem autorização dos pais? (sim/não): ")

if idade >= 18 or autorizacao_pais == "sim":
    print("A pessoa pode participar.")
else:
    print("A pessoa não pode participar.")