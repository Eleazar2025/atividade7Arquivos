import pandas as pd

def processar_logs_treinamentos(nome_arquivo='logs_treinamento.csv'):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()

        print(f'Média do tempo de execução: {media_tempo:.2f}')
        print(f'Desvio padrão do tempo de execução: {desvio_padrao:.2f}')
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

processar_logs_treinamentos()