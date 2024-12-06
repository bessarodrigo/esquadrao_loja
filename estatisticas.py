import numpy as np
from scipy.stats import mode, skew, kurtosis

# Função para calcular as estatísticas
def calcular_estatisticas(amostra):
    moda_result = mode(amostra, keepdims=True)  # Garantir que a moda é retornada como array
    estatisticas = {
        "Média": np.mean(amostra),
        "Mediana": np.median(amostra),
        "Moda": moda_result.mode[0] if len(moda_result.mode) > 0 else np.nan,
        "Variância": np.var(amostra, ddof=1),
        "Desvio Padrão": np.std(amostra, ddof=1),
        "Assimetria": skew(amostra),
        "Curtose": kurtosis(amostra, fisher=False),  # fisher=False retorna a curtose de momento
        "1º Quartil": np.percentile(amostra, 25),
        "2º Quartil (Mediana)": np.percentile(amostra, 50),
        "3º Quartil": np.percentile(amostra, 75)
    }
    return estatisticas
    