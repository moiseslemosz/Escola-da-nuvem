import warnings
from urllib3.exceptions import InsecureRequestWarning
import requests

warnings.filterwarnings('ignore', category=InsecureRequestWarning)

# 1- ---------------------------------------------------------------------------------
import random
import string

def gerar_senha_aleatoria():
    print("\n--- 1. Gerador de Senha Aleatória ---")
    
    try:
        # Pede o comprimento da senha, garantindo que seja um número inteiro.
        comprimento = int(input("Digite a quantidade de caracteres desejada para a senha (mín. 8): "))
        if comprimento < 8:
            print("O comprimento mínimo sugerido é 8. Usando 8.")
            comprimento = 8
    except ValueError:
        print("Entrada inválida. Usando comprimento padrão de 12.")
        comprimento = 12

    # Define o conjunto de caracteres a serem usados:
    # Letras (maiúsculas e minúsculas), dígitos e pontuação (caracteres especiais)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha: escolhe aleatoriamente 'comprimento' caracteres do conjunto.
    senha_gerada = ''.join(random.choice(caracteres) for i in range(comprimento))
    
    print(f"Senha Gerada: {senha_gerada}")
    print("-" * 50)

gerar_senha_aleatoria()

# 2- -------------------------------------------------------------------------------
def gerar_perfil_aleatorio():
    print("\n--- 2. Gerador de Perfil de Usuário Aleatório ---")
    
    # URL da API para solicitar um único usuário
    API_URL = "https://randomuser.me/api/"
    
    try:
        # Faz a requisição GET
        response = requests.get(API_URL, verify=False)
        response.raise_for_status() # Verifica erros HTTP
        dados = response.json()
        
        # Extração de Dados:
        usuario = dados['results'][0]
        
        # Nome completo
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        
        # País
        pais = usuario['location']['country']
        
        # Exibe as informações
        print("Perfil Gerado com Sucesso:")
        print(f"Nome: {nome}")
        print(f"Email: {usuario['email']}")
        print(f"País: {pais}")
        
    except requests.exceptions.RequestException as e:
        print(f"ERRO de Conexão: Não foi possível acessar a API. {e}")
    except KeyError:
        print("ERRO de Processamento: O formato dos dados da API mudou.")
        
    print("-" * 50)

gerar_perfil_aleatorio()

# 3- -------------------------------------------------------------------------
def consultar_endereco_por_cep():
    print("\n--- 3. Consulta de Endereço por CEP (ViaCEP) ---")
    
    # Pede o CEP e remove caracteres não numéricos
    cep = input("Digite o CEP (apenas números): ").strip().replace('-', '').replace('.', '')
    
    if len(cep) != 8 or not cep.isdigit():
        print("ERRO: CEP deve conter exatamente 8 dígitos.")
        return

    # URL da API ViaCEP
    API_URL = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(API_URL, verify=False)
        response.raise_for_status() 
        dados = response.json()
        
        # Verifica se o CEP é inválido (retorna 'erro' no JSON)
        if 'erro' in dados:
            print(f"ERRO: CEP {cep} não encontrado ou inválido.")
            return

        # Exibe as informações
        print("Endereço Encontrado:")
        print(f"  Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"  Bairro: {dados.get('bairro', 'N/A')}")
        print(f"  Cidade/UF: {dados.get('localidade', 'N/A')}/{dados.get('uf', 'N/A')}")
        
    except requests.exceptions.RequestException as e:
        print(f"ERRO de Conexão: Não foi possível acessar a ViaCEP. {e}")
        
    print("-" * 50)

consultar_endereco_por_cep()

# 4- ---------------------------------------------------------------------------------
def consultar_cotacao_moeda():
    print("\n--- 4. Consulta de Cotação de Moeda (AwesomeAPI) ---")
    
    moeda_code = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    
    # Define a paridade em relação ao Real Brasileiro (BRL)
    paridade = f"{moeda_code}-BRL"
    
    # URL da AwesomeAPI
    API_URL = f"https://economia.awesomeapi.com.br/json/last/{paridade}"
    
    try:
        response = requests.get(API_URL, verify=False)
        response.raise_for_status()
        dados = response.json()
        
        # A chave principal no JSON é a paridade formatada (ex: 'USDBRL')
        cotacao_data = dados.get(paridade.replace('-', ''))
        
        if not cotacao_data:
            print(f"ERRO: Moeda '{moeda_code}' não encontrada ou inválida na API.")
            return
            
        # Extração de Dados
        valor_atual = float(cotacao_data['bid'])
        valor_maximo = float(cotacao_data['high'])
        valor_minimo = float(cotacao_data['low'])
        
        # Formata a data/hora de atualização (Unix Timestamp para legível)
        timestamp = int(cotacao_data['timestamp'])
        from datetime import datetime
        data_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        # Exibe as informações
        print("Dados da Cotação Encontrados:")
        print(f"Moeda: {moeda_code} (Paridade: {paridade})")
        print(f"Valor Atual (Compra): R$ {valor_atual:.4f}")
        print(f"Máximo do Dia (High): R$ {valor_maximo:.4f}")
        print(f"Mínimo do Dia (Low): R$ {valor_minimo:.4f}")
        print(f"Última Atualização: {data_atualizacao}")

    except requests.exceptions.RequestException as e:
        print(f"ERRO de Conexão: Não foi possível acessar a AwesomeAPI. {e}")
    except ValueError:
        print("ERRO de Processamento: Dados numéricos inválidos retornados pela API.")
        
    print("-" * 50)

consultar_cotacao_moeda()