import json
import time
import numpy as np
from datetime import datetime

def log_training_metrics(model, X_test, y_test, execution_times, resource_usage):
    """Função para gerar logs no formato padrão"""

    # Calcula métricas de tempo
    time_stats = {
        "mean_execution_time_seconds": np.mean(execution_times),
        "std_dev_execution_time_seconds": np.std(execution_times),
        "min_time": min(execution_times),
        "max_time": max(execution_times),
        "total_training_time": sum(execution_times)
    }

    # Calcula métricas de desempenho
    y_pred = model.predict(X_test)
    performance_metrics = {
        "accuracy": model.score(X_test, y_test),
        # Adicionar outras métricas conforme necessário
    }

    # Cria estrutura completa do log
    training_log = {
        "timestamps": {
            "start_time": datetime.utcnow().isoformat() + "Z",
            # Outros timestamps
        },
        "execution_metrics": {
            "time_stats": time_stats,
            "resource_usage": resource_usage
        },
        "performance_metrics": performance_metrics,
        # Outras seções
    }

    # Salva em arquivo JSON
    with open(f"training_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
        json.dump(training_log, f, indent=4)