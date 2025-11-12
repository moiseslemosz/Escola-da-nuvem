# 1- ----------------------------------------------------------------------------
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    # Converte a porcentagem (ex: 15) para decimal (0.15) 
    taxa = porcentagem_gorjeta / 100
    
    # Calcula o valor da gorjeta
    valor_gorjeta = valor_conta * taxa
    
    return valor_gorjeta

valor_conta_exemplo = 75.50
porcentagem_exemplo = 15
gorjeta_calculada = calcular_gorjeta(valor_conta_exemplo, porcentagem_exemplo)

print("--- 1. Calculadora de Gorjeta ---")
print(f"Conta: R$ {valor_conta_exemplo:.2f}")
print(f"Porcentagem: {porcentagem_exemplo}%")
print(f"Valor da gorjeta: R$ {gorjeta_calculada:.2f}")

# 2- -----------------------------------------------------------------------------

import re # Módulo usado para Expressões Regulares (Regex)

def verificar_palindromo(frase: str) -> str:
    # 1. Limpeza: Remove todos os caracteres não alfanuméricos (incluindo espaços e pontuação)
    # e converte para minúsculas.
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    
    # 2. Inversão: Inverte a string limpa.
    frase_invertida = frase_limpa[::-1]
    
    # 3. Comparação e Retorno:
    if frase_limpa == frase_invertida:
        return "Sim"
    else:
        return "Não"

frase1 = str(input("Digite a primeira frase/palavra:"))
frase2 = str(input("Digite a segunda frase/palavra:"))

print("\n--- 2. Verificador de Palíndromo ---")
print(f"'{frase1}' é palíndromo? {verificar_palindromo(frase1)}")
print(f"'{frase2}' é palíndromo? {verificar_palindromo(frase2)}")


# 3- -----------------------------------------------------------------------------------------------
def calculadora_desconto():
    print("\n--- 3. Calculadora de Desconto ---")
    
    try:
        # Requisito: Permitir entrada do usuário
        preco_original = float(input("Digite o preço original do produto (ex: 250.75): R$ "))
        percentual_desconto = float(input("Digite o percentual de desconto (ex: 10): "))
        
        # Validar entradas básicas
        if preco_original < 0 or percentual_desconto < 0 or percentual_desconto > 100:
            print("Erro: Valores inválidos. O preço e a porcentagem devem ser positivos, e a porcentagem não pode exceder 100.")
            return

    except ValueError:
        print("Erro: Entrada não numérica. Por favor, insira apenas números.")
        return

    # Cálculo: 
    # 1. Converte o percentual para a taxa decimal
    taxa_desconto = percentual_desconto / 100
    
    # 2. Calcula o valor do desconto (operação matemática)
    valor_do_desconto = preco_original * taxa_desconto
    
    # 3. Calcula o preço final (operação matemática)
    preco_final = preco_original - valor_do_desconto
    
    # Exibir o resultado com duas casas decimais
    print("-" * 35)
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto Aplicado ({percentual_desconto:.0f}%): R$ {valor_do_desconto:.2f}")
    print(f"Preço Final: R$ {preco_final:.2f}")

calculadora_desconto()

# 4- -----------------------------------------------------------------------------------------
from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    # Data de hoje
    hoje = date.today()
    
    # Data de nascimento (assumindo 1º de janeiro do ano de nascimento)
    data_nascimento = date(ano_nascimento, 1, 1)
    
    diferenca = hoje - data_nascimento
    
    # Retorna a diferença em dias
    return diferenca.days

ano_nascimento_exemplo = int(input("Digite o ano de nascimento: "))
dias_vividos = calcular_idade_em_dias(ano_nascimento_exemplo)

print("\n--- 4. Calculadora de Idade em Dias ---")
print(f"Se você nasceu em {ano_nascimento_exemplo}, você viveu aproximadamente {dias_vividos} dias (até a data de cálculo).")