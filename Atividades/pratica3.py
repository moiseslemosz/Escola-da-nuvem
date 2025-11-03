#--------------------------------------------------------------------------------
# 1 - Área da Circunferência
PI = 3.14159265
raio = float(input("Digite o valor do raio: "))
area = PI * (raio ** 2)
print(f"A={area:.4f}")

#--------------------------------------------------------------------------------
# 2 - Classificador de Idade
idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"

print(f"Classificação: {categoria}")

#--------------------------------------------------------------------------------
# 3 - Calculadora de IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"IMC: {imc:.2f} - Classificação: {classificacao}")

#--------------------------------------------------------------------------------
# 4 - Conversor de Temperatura
temp = float(input("Digite a temperatura: "))
origem = input("Converter de (C/F/K): ").upper()
destino = input("Para (C/F/K): ").upper()

# Converte para Celsius como base
if origem == "F":
    temp_c = (temp - 32) * 5/9
elif origem == "K":
    temp_c = temp - 273.15
else:
    temp_c = temp

# Converte de Celsius para destino
if destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    resultado = temp_c

print(f"{temp:.2f}{origem} equivalem a {resultado:.2f}{destino}")

#--------------------------------------------------------------------------------
# 5 - Verificador de Ano Bissexto
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

#--------------------------------------------------------------------------------
# 6 - Calculadora de Comissão
nome = input("Nome do vendedor: ")
salario_fixo = float(input("Salário fixo: R$ "))
vendas = float(input("Total de vendas: R$ "))

total = salario_fixo + (vendas * 0.15)
print(f"TOTAL = R$ {total:.2f}")

#--------------------------------------------------------------------------------
# 7 - Calculadora da Média
N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

media = (N1*2 + N2*3 + N3*4 + N4*1) / 10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input("Nota do exame: "))
    print(f"Nota do exame: {exame:.1f}")
    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
#--------------------------------------------------------------------------------