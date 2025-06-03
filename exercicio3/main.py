import csv

def ler_e_exibir_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            print("\nDados das pessoas:")
            print("-" * 40)
            print(f"{'Nome':<20} | {'Idade':^5} | {'Cidade':<15}")
            print("-" * 40)

            for linha in leitor_csv:
                print(f"{linha['Nome']:<20} | {linha['Idade']:^5} | {linha['Cidade']:<15}")

            print("-" * 40)
            print(f"Total de registros: {leitor_csv.line_num - 1}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# Nome do arquivo CSV a ser lido
nome_arquivo = "pessoas.csv"

# Chamando a função para ler e exibir os dados
ler_e_exibir_csv(nome_arquivo)