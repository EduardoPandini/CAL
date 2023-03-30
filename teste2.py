import time
import random
import matplotlib.pyplot as plt

def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return None

def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

tempos_linear = []
tempos_binaria = []
tamanhos = [10**i for i in range(1, 6)]

for tamanho in tamanhos:
    lista = [random.randint(0, tamanho) for _ in range(tamanho)]
    item = random.randint(0, tamanho)

    inicio = time.time()
    busca_linear(lista, item)
    fim = time.time()
    tempos_linear.append(fim - inicio)

    inicio = time.time()
    busca_binaria(sorted(lista), item)
    fim = time.time()
    tempos_binaria.append(fim - inicio)

plt.plot(tamanhos, tempos_linear, 'r', label='Busca Linear')
plt.plot(tamanhos, tempos_binaria, 'b', label='Busca Binária')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.title('Comparação de Busca Linear e Busca Binária')
plt.legend()
plt.show()
