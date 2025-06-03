import json
import os

def escrever_json(dados, arquivo):
    """Escreve dados em um arquivo JSON"""
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em {arquivo}!")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

def ler_json(arquivo):
    """Lê dados de um arquivo JSON"""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return dados
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado. Criando novo arquivo.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def exibir_pessoas(pessoas):
    """Exibe os dados das pessoas formatados"""
    if not pessoas:
        print("Nenhum dado para exibir.")
        return

    print("\nDados das pessoas:")
    print("-" * 40)
    print(f"{'Nome':<20} | {'Idade':^5} | {'Cidade':<15}")
    print("-" * 40)

    for pessoa in pessoas:
        print(f"{pessoa['nome']:<20} | {pessoa['idade']:^5} | {pessoa['cidade']:<15}")

    print("-" * 40)

def main():
    arquivo_json = "pessoas.json"

    # Verifica se o arquivo existe e carrega os dados existentes
    pessoas = ler_json(arquivo_json)
    if pessoas is None:
        return

    # Menu principal
    while True:
        print("\nMenu:")
        print("1 - Adicionar nova pessoa")
        print("2 - Visualizar pessoas cadastradas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Coleta dados da nova pessoa
            print("\nNova pessoa:")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cidade = input("Cidade: ")

            nova_pessoa = {
                "nome": nome,
                "idade": idade,
                "cidade": cidade
            }

            # Adiciona a nova pessoa à lista
            pessoas.append(nova_pessoa)
            # Salva no arquivo JSON
            escrever_json(pessoas, arquivo_json)

        elif opcao == '2':
            # Exibe os dados formatados
            exibir_pessoas(pessoas)

        elif opcao == '3':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()