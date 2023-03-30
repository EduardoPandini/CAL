import time
import matplotlib.pyplot as plt
import numpy as np

# Função para gerar lista aleatória
def gerar_lista(tamanho):
    return list(np.random.randint(0, 1000, tamanho))

# Função para o algoritmo Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i-1
        while j >= 0 and chave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave

# Função para o algoritmo Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Função para comparar os algoritmos
def comparar_algoritmos(tamanhos, repeticoes):
    tempos_insertion_sort = []
    tempos_bubble_sort = []
    for tamanho in tamanhos:
        lista = gerar_lista(tamanho)
        tempo_total_insertion_sort = 0
        tempo_total_bubble_sort = 0
        for _ in range(repeticoes):
            # Executa o algoritmo Insertion Sort
            lista_copia = lista.copy()
            inicio = time.time()
            insertion_sort(lista_copia)
            fim = time.time()
            tempo_total_insertion_sort += fim - inicio
            
            # Executa o algoritmo Bubble Sort
            lista_copia = lista.copy()
            inicio = time.time()
            bubble_sort(lista_copia)
            fim = time.time()
            tempo_total_bubble_sort += fim - inicio
            
        # Calcula a média dos tempos
        media_insertion_sort = tempo_total_insertion_sort / repeticoes
        media_bubble_sort = tempo_total_bubble_sort / repeticoes
        
        tempos_insertion_sort.append(media_insertion_sort)
        tempos_bubble_sort.append(media_bubble_sort)
        
    # Plota o gráfico comparando os tempos
    plt.plot(tamanhos, tempos_insertion_sort, label='Insertion Sort')
    plt.plot(tamanhos, tempos_bubble_sort, label='Bubble Sort')
    plt.legend()
    plt.title('Comparação de complexidade - Insertion Sort x Bubble Sort')
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo (s)')
    plt.show()

# Testando a função comparar_algoritmos
tamanhos = [10, 100, 1000, 10000]
repeticoes = 5
comparar_algoritmos(tamanhos, repeticoes)
