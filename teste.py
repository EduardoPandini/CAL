import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def generate_random_array(n):
    return [random.randint(1, 100) for _ in range(n)]

def time_function(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

def compare_sort_algorithms():
    insertion_times = []
    bubble_times = []
    quick_times = []
    merge_times = []

    for i in range(100, 1100, 100):
        arr = generate_random_array(i)
        insertion_times.append(time_function(insertion_sort, arr))
        bubble_times.append(time_function(bubble_sort, arr))
        quick_times.append(time_function(quick_sort, arr))
        merge_times.append(time_function(merge_sort, arr))

    n_values = range(100, 1100, 100)

    plt.plot(n_values, insertion_times, label='Insertion Sort')
    plt.plot(n_values, bubble_times, label='Bubble Sort')
    plt.plot(n_values, quick_times, label='QuickSort')
    plt.plot(n_values, merge_times, label='MergeSort')

    plt.xlabel('Tamanho do array')
    plt.ylabel('Tempo (s)')
    plt.title('Comparação de algoritmos de ordenação')
    plt.legend()
    plt.show()

compare_sort_algorithms()
