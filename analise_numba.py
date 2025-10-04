import numpy as np
from numba import jit
import time
import sys

# --- CONFIGURAÇÃO ---
# Número de simulações (pontos)
NUM_PONTOS = 10**7 # 10 milhões de pontos

# 1. FUNÇÃO EM PYTHON PURO (LINHA DE BASE)
def calcula_pi_python(num_pontos):
    """Calcula Pi usando o Método de Monte Carlo (Python puro)."""
    pontos_dentro_circulo = 0
    # Gera pontos aleatórios usando numpy para otimização do vetor
    x = np.random.uniform(0, 1, num_pontos)
    y = np.random.uniform(0, 1, num_pontos)
    
    # Executa o loop para contar pontos dentro do círculo
    for i in range(num_pontos):
        if x[i]**2 + y[i]**2 <= 1.0:
            pontos_dentro_circulo += 1
            
    return 4 * pontos_dentro_circulo / num_pontos

# 2. FUNÇÃO ACELERADA COM NUMBA JIT
# O decorador @jit(nopython=True) diz ao Numba para compilar esta função
@jit(nopython=True)
def calcula_pi_numba(num_pontos):
    """Calcula Pi usando o Método de Monte Carlo (ACELERADO com Numba)."""
    pontos_dentro_circulo = 0
    # Gera pontos aleatórios DENTRO do Numba para máxima aceleração
    x = np.random.uniform(0, 1, num_pontos)
    y = np.random.uniform(0, 1, num_pontos)
    
    for i in range(num_pontos):
        if x[i]**2 + y[i]**2 <= 1.0:
            pontos_dentro_circulo += 1
            
    return 4 * pontos_dentro_circulo / num_pontos

# --- EXECUÇÃO E MEDIÇÃO ---

print(f"Executando simulação de Pi (Monte Carlo) com {NUM_PONTOS} pontos...")

# Fase 1: Aquecimento (Warm-up) - Essencial para o Numba
# A primeira chamada aciona a compilação JIT, por isso não medimos o tempo.
try:
    _ = calcula_pi_numba(100) 
except Exception as e:
    print(f"\nERRO: A biblioteca Numba pode não estar instalada. Erro: {e}")
    sys.exit(1)


# Fase 2: Medição do Python Puro
tempo_inicio_py = time.perf_counter()
pi_py = calcula_pi_python(NUM_PONTOS)
tempo_fim_py = time.perf_counter()
tempo_py = tempo_fim_py - tempo_inicio_py

# Fase 3: Medição do Numba (Compilado)
tempo_inicio_nb = time.perf_counter()
pi_nb = calcula_pi_numba(NUM_PONTOS)
tempo_fim_nb = time.perf_counter()
tempo_nb = tempo_fim_nb - tempo_inicio_nb

# --- SAÍDA DOS RESULTADOS ---

print("\n--- RESULTADOS DE DESEMPENHO (Numba vs Python Puro) ---")
print(f"Número de Pontos Simulados: {NUM_PONTOS}")
print("-" * 50)
print(f"Método | Pi Aproximado | Tempo (s)")
print("-" * 50)
print(f"Python Puro | {pi_py:.6f} | {tempo_py:.4f}")
print(f"Numba JIT | {pi_nb:.6f} | {tempo_nb:.4f}")
print("-" * 50)
aceleracao = tempo_py / tempo_nb
print(f"Ganho de Desempenho (Aceleração): {aceleracao:.2f}x")
print("-------------------------------------------------------")