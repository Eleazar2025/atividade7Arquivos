import csv

# Dados das pessoas a serem escritos no arquivo CSV
pessoas = [
    {"Nome": "João Silva", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Maria Oliveira", "Idade": 32, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos Souza", "Idade": 19, "Cidade": "Belo Horizonte"},
    {"Nome": "Ana Costa", "Idade": 42, "Cidade": "Porto Alegre"},
    {"Nome": "Pedro Santos", "Idade": 28, "Cidade": "Salvador"}
]

# Nome do arquivo CSV que será criado
nome_arquivo = "pessoas.csv"

# Escrevendo os dados no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Definindo os nomes das colunas
    campos = ['Nome', 'Idade', 'Cidade']

    # Criando o escritor CSV
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)

    # Escrevendo o cabeçalho
    escritor_csv.writeheader()

    # Escrevendo os dados das pessoas
    escritor_csv.writerows(pessoas)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")