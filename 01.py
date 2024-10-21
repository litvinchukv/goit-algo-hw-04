import random
import timeit

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Вбудована функція sorted() для Timsort
def timsort(arr):
    return sorted(arr)

# Генерація тестових даних
def generate_data(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# Замір часу виконання
def measure_time(func, data):
    return timeit.timeit(lambda: func(data.copy()), number=1)

if __name__ == "__main__":
    # Розмір тестових масивів
    sizes = [100, 1000, 5000, 10000]

    # Збереження результатів
    results = []

    for size in sizes:
        data = generate_data(size)
        insertion_time = measure_time(insertion_sort, data)
        merge_time = measure_time(merge_sort, data)
        timsort_time = measure_time(timsort, data)
        results.append({
            'Size': size,
            'Insertion Sort': insertion_time,
            'Merge Sort': merge_time,
            'Timsort': timsort_time
        })
    # Приклад запуску
    # {'Size': 100, 'Insertion Sort': 0.0001038750633597374, 'Merge Sort': 7.804203778505325e-05, 'Timsort': 8.66700429469347e-06}
    # {'Size': 1000, 'Insertion Sort': 0.013534125057049096, 'Merge Sort': 0.0010875830193981528, 'Timsort': 9.03749605640769e-05}
    # {'Size': 5000, 'Insertion Sort': 0.35631125001236796, 'Merge Sort': 0.006258708075620234, 'Timsort': 0.00048679206520318985}
    # {'Size': 10000, 'Insertion Sort': 1.4137817079899833, 'Merge Sort': 0.013777291984297335, 'Timsort': 0.001078665954992175}
    for item in results:
        print(item)