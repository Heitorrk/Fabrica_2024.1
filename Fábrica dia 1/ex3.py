# ex3
# faça um programa que fale o nome de cinco times de futebol

import random

times = ["Palmeiras", "Vasco", "BotaFogo", "São Paulo", "Grêmio", "Fortaleza", "Bahia", "Cruzeiro", "Santos"]

for i in range(5):
    time = times[random.randint(0, len(times))]
    print(f"Time {i+1}:", time)