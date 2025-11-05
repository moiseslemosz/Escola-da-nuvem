# -1 Calculdaora em Python -------------------------------------------------------------
operacoes = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação ( + , - , * , / ) ").strip()
    except ValueError:
        print("\nERRO: Entrada inválida. Por favor, insira apenas números.")
        continue

    if operacao not in operacoes:
        print("\nERRO: Operação inválida. Use apenas ( + , - , * ou / )")
        continue

    try:
        resultado = operacoes[operacao](numero1, numero2)
    except ZeroDivisionError:
        print("\nERRO: Divisão por zero não é permitida.")
        continue

    print(f"\nResultado da operação: {numero1} {operacao} {numero2} = {resultado}")
    break


# -----------------------------------------------------------------------------------------
# 2- Programa de Notas
notas = []

while True:
    entrada = input("Digite a nota (0-10) ou 'fim' para terminar: ").strip().lower()

    if entrada == "fim":
        break

    try:
        nota = float(entrada)

        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida, deve estar entre 0 e 10. Tente novamente")

    except ValueError:
        print("Entrada inválida, digite um número ou 'fim'. Tente novamente")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida registrada.")


#--------------------------------------------------------------------------
# 3- Programa de senhas
def verificar_forca_senha(senha: str) -> bool:
    tem_comprimento_minimo = len(senha) >= 8
    
    # Checa o conteúdo numérico
    # Itera sobre cada caractere (c) na senha e checa se algum é um dígito.
    tem_numero = any(c.isdigit() for c in senha)
    
    # A senha é forte se AMBAS as condições forem Verdadeiras
    return tem_comprimento_minimo and tem_numero

while True:
    entrada = input("Crie uma senha (ou digite 'sair'): ").strip()
    
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break 
        
    # Chama a função de verificação
    if verificar_forca_senha(entrada):
        print("Senha forte! Cadastro realizado com sucesso.")
        break 
    else:
        if len(entrada) < 8:
            print("Falha: A senha deve ter pelo menos 8 caracteres.")
        if not any(c.isdigit() for c in entrada):
             print("Falha: A senha deve conter pelo menos um número.")
        print("Tente novamente.")


#-------------------------------------------------------------------------------
# 4- Programa de números inteiros, pares ou impares
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip().lower()

    if entrada == "fim":
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é impar.")
            impares += 1
    except ValueError:
        print("Erro! Digite apenas números inteiros ou 'fim' para sair!")

print("\n--- Resultado Final ---")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")