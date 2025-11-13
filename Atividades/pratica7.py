# 1- ----------------------------------------------------------------------------
import numpy as np # Biblioteca padrão em ciência de dados para cálculos estatísticos

def analisar_log_treinamento(nome_arquivo="./log_machine_learning.txt"):
    tempos = []
    
    print(f"\n--- 1. Análise Estatística do Log ({nome_arquivo}) ---")

    try:
        # Abre o arquivo em modo de leitura ('r')
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                # Remove espaços em branco e quebras de linha e tenta converter para float
                try:
                    tempo = float(linha.strip())
                    tempos.append(tempo)
                except ValueError:
                    # Ignora linhas que não são números
                    continue
        
        if not tempos:
            print("Erro: O arquivo não contém dados numéricos válidos.")
            return

        # Converte a lista para um array NumPy para facilitar os cálculos
        tempos_array = np.array(tempos)
        
        # Cálculos Estatísticos
        media = np.mean(tempos_array)
        desvio_padrao = np.std(tempos_array)
        
        print("Análise Concluída:")
        print(f"Número de Execuções: {len(tempos_array)}")
        print(f"Média do Tempo de Execução: {media:.2f} segundos")
        print(f"Desvio Padrão do Tempo: {desvio_padrao:.2f} segundos")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

analisar_log_treinamento()

######################################################################################
# 2- ----------------------------------------------------------------------------------
import csv

def escrever_csv(nome_arquivo="dados_pessoas.csv"):
    dados = [
        ["Nome", "Idade", "Cidade"], # Cabeçalho
        ["João Silva", 35, "São Paulo"],
        ["Maria Santos", 28, "Rio de Janeiro"],
        ["Carlos Ferreira", 42, "Belo Horizonte"]
    ]
    
    print(f"\n--- 2. Escrevendo no CSV ({nome_arquivo}) ---")
    
    try:
        # Abre o arquivo em modo de escrita ('w'). newline='' evita linhas em branco.
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            escritor_csv = csv.writer(arquivo)
            
            # Escreve todas as linhas de uma vez
            escritor_csv.writerows(dados)
            
        print(f"Dados escritos com sucesso em '{nome_arquivo}'.")

    except Exception as e:
        print(f"Erro ao escrever no arquivo CSV: {e}")

escrever_csv()


######################################################################################
# 3- --------------------------------------------------------------------------------
def ler_csv(nome_arquivo="dados_pessoas.csv"):
    print(f"\n--- 3. Lendo do CSV ({nome_arquivo}) ---")
    
    try:
        # Abre o arquivo em modo de leitura ('r')
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            
            print("Conteúdo do Arquivo CSV:")
            print("-" * 50)
            
            # Itera sobre cada linha lida
            for linha in leitor_csv:
                # O 'linha' é uma lista de strings (ex: ['Nome', 'Idade', 'Cidade'])
                print(f"| {linha[0]:<15} | {linha[1]:<5} | {linha[2]:<15} |")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

ler_csv()


###########################################################################################
# 4- ------------------------------------------------------------------------------------------
import json

def manipular_json(nome_arquivo="dados_pessoa.json"):
    dados_escrita = {
        "nome": "Fernando Souza",
        "idade": 30,
        "cidade": "Curitiba"
    }
    
    # PARTE 1: ESCREVER NO JSON
    print(f"\n--- 4. Manipulação de JSON ({nome_arquivo}) ---")
    
    try:
        # Abre em modo de escrita ('w')
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # json.dump escreve o dicionário diretamente no arquivo
            # indent=4 formata o JSON com recuos legíveis
            json.dump(dados_escrita, arquivo, indent=4)
        
        print(f"Dados da pessoa escritos com sucesso em '{nome_arquivo}'.")

    except Exception as e:
        print(f"Erro ao escrever no arquivo JSON: {e}")
        return

    # PARTE 2: LER DO JSON
    try:
        # Abre em modo de leitura ('r')
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # json.load lê o conteúdo do arquivo e o converte em um dicionário Python
            dados_leitura = json.load(arquivo)

        print("\nDados lidos do arquivo JSON:")
        print(f"  Nome: {dados_leitura['nome']}")
        print(f"  Idade: {dados_leitura['idade']}")
        print(f"  Cidade: {dados_leitura['cidade']}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON: {e}")

manipular_json()