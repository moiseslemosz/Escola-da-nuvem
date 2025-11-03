# 1- Conversor de Moeda 

valor_em_reais = 100.00 
taxa_dolar = 5.60
taxa_euro = 6.60

def formula_dolar(valor_em_reais, taxa_dolar):
    dolares = valor_em_reais / taxa_dolar
    print(f"R$ {valor_em_reais:.2f} equivalem a US$ {dolares:.2f}")
    
def formula_euro(valor_em_reais, taxa_euro):
    euro = valor_em_reais / taxa_euro
    print(f"R$ {valor_em_reais:.2f} equivalem a € {euro:.2f}")
    
formula_dolar(valor_em_reais, taxa_dolar)
formula_euro(valor_em_reais, taxa_euro)

##############################################################
# 2- Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
desconto = 20

valor_desconto = preco_original * (desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Nome do produto: {produto}")
print(f"Preço original: R${preco_original:.2f}")
print(f"Porcentagem de desconto: {desconto}%")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Preço final do produto '{produto}': R${preco_final:.2f}")

#################################################################
# 3- Calculadora de Média Escolar 
nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Nota 1: {nota_1}")
print(f"Nota 2: {nota_2}")
print(f"Nota 3: {nota_3}")
print(f"Média final: {media:.2f}")

#################################################################
# 4- Calculadora de Consumo de Combustível
distancia_percorrida = 300
combustivel_gasto = 25

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Distância percorrida: {distancia_percorrida}km")
print(f"Combustível gasto: {combustivel_gasto}L")
print(f"Consumo médio: {consumo_medio:.2f}km/L")

#################################################################
# 5- Calculadora de Soma com Entrada do Usuário
A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))

X = A + B

print(f"X = {X}")

#################################################################
# 6- Calculadora de salário por horas trabalhadas
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Valor da hora trabalhada: "))

salario = horas_trabalhadas * valor_por_hora

print(f"Número do funcionário = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")