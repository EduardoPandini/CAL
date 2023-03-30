import time
import random
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# gerando dados aleatórios para os testes
n = 10000
arr = [random.randint(1, 100000) for _ in range(n)]
x = random.randint(1, 100000)

# medindo o tempo de execução do Heap Sort
start = time.time()
heap_sort(arr)
end = time.time()
heap_sort_time = end - start

# medindo o tempo de execução da Busca Linear
start = time.time()
linear_search(arr, x)
end = time.time()
linear_search_time = end - start

# medindo o tempo de execução da Busca Binária
start = time.time()
binary_search(arr, x)
end = time.time()
binary_search_time = end - start

# gerando o gráfico de linhas
x_axis = ['Heap Sort', 'Busca Linear', 'Busca Binária']
y_axis = [heap_sort_time, linear_search_time, binary_search_time]

plt.plot(x_axis, y_axis)
plt.xlabel('Algoritmo')
plt.ylabel('Tempo de execução (s)')
plt.title('Comparação de complexidade')
plt.show()