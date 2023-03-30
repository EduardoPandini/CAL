import random
import time
import matplotlib.pyplot as plt

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Gerando listas aleatórias de diferentes tamanhos
sizes = [100, 1000, 10000, 100000, 1000000]
arrays = []
for size in sizes:
    arrays.append(random.sample(range(size * 10), size))

# Medindo o tempo de execução dos algoritmos para cada lista
heap_sort_times = []
linear_search_times = []
binary_search_times = []
for arr in arrays:
    start = time.time()
    heap_sort(arr)
    end = time.time()
    heap_sort_times.append(end - start)

    x = random.randint(0, size * 10)
    start = time.time()
    linear_search(arr, x)
    end = time.time()
    linear_search_times.append(end - start)

    arr.sort()
    x = random.randint(0, size * 10)
    start = time.time()
    binary_search(arr, x)
    end = time.time()
    binary_search_times.append(end - start)

# Plotando os resultados
plt.plot(sizes, heap_sort_times, label='Heap Sort')
plt.plot(sizes, linear_search_times, label='Busca Linear')
plt.plot(sizes, binary_search_times, label='Busca Binária')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.legend()
plt.show()
