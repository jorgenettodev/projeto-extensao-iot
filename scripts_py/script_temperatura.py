import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Configurações
dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
num_readings_per_day = 43200  # 24 horas * 60 minutos * 30 leituras por minuto
total_readings = num_readings_per_day * 7
tempo_total = total_readings * 2  # Tempo total em segundos
intervalo = 2  # Intervalo de 2 segundos

# Gerar dados simulados
np.random.seed(42)  # Para reprodutibilidade
tempos = np.arange(0, tempo_total, intervalo)
temperaturas = [random.uniform(15, 21) for _ in range(total_readings)]  # Temperaturas entre 15 e 21 graus

# Criar DataFrame
data = pd.DataFrame({
    'Tempo (s)': tempos,
    'Temperatura (°C)': temperaturas
})

# Adicionar coluna para dia da semana
data['Dia da Semana'] = np.repeat(dias_da_semana, num_readings_per_day)

# Cálculo da média de temperatura por dia
media_por_dia = data.groupby('Dia da Semana')['Temperatura (°C)'].mean()

# Encontrar picos de temperatura
pico_alto = data['Temperatura (°C)'].max()
pico_baixo = data['Temperatura (°C)'].min()

# Dia mais quente
dia_mais_quente = media_por_dia.idxmax()

# Exibir resultados
print("Média de Temperatura por Dia da Semana:")
print(media_por_dia)
print(f"Pico de Temperatura Alto: {pico_alto:.2f} °C")
print(f"Pico de Temperatura Baixo: {pico_baixo:.2f} °C")
print(f"Dia da Semana Mais Quente: {dia_mais_quente}")

# Gráfico da média de temperatura por dia
plt.figure(figsize=(10, 5))
media_por_dia.plot(kind='bar', color='skyblue')
plt.axhline(y=18, color='r', linestyle='--', label='Temperatura Ideal (18 °C)')
plt.title('Média de Temperatura por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Média de Temperatura (°C)')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()