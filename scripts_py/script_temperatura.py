import matplotlib.pyplot as plt
import requests
import time

# O projeto será implantado posteriormente, pois ainda não foi realizada compra dos sensores e equipamentos necessários para medição, então este script serve como plano de ação 
# de treinamento e futura implementação.

# URL do sensor de temperatura 
url = 'http://<IP_DO_SENSOR>/temperatura'  # Substitua <IP_DO_SENSOR> pelo IP do seu dispositivo

# Listas para armazenar os dados
temperaturas = []
tempos = []

# Configurações do gráfico
plt.ion()  # Modo interativo
fig, ax = plt.subplots()
line, = ax.plot(tempos, temperaturas, label='Temperatura (°C)')
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Temperatura (°C)')
ax.set_title('Monitoramento de Temperatura')
ax.legend()

# Contador de tempo
tempo_inicial = time.time()

try:
    while True:
        # Requisição para obter a temperatura
        response = requests.get(url)
        temperatura = response.json().get('temperatura')  # Ajuste conforme a estrutura do JSON

        # Atualiza listas
        temperaturas.append(temperatura)
        tempos.append(time.time() - tempo_inicial)

        # Atualiza o gráfico
        line.set_xdata(tempos)
        line.set_ydata(temperaturas)
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(2)  # Atualiza a cada 2 segundos

except KeyboardInterrupt:
    print("Monitoramento encerrado.")