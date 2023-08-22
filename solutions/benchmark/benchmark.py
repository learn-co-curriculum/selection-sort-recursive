import time

def selection_sort(list):
    sorted_list = []

    while len(list) > 0:
        min_element = min(list)

        sorted_list.append(min_element)
        list.remove(min_element)

    return sorted_list

def selection_sort_recursive(list):

    if len(list) == 0:
        return []
    
    minElement = min(list)

    list.remove(minElement)

    result = selection_sort_recursive(list)

    result.insert(0, minElement)

    return result

def benchmark(callback):
   
    start_time = time.time()

    for i in range(1000):
        callback()

    return (time.time() - start_time) / 1000

print("Iterative: " + str(benchmark(lambda : selection_sort([2, 3, 4, 1, 4, 56, -2, 20]))))
print("Recursive: " + str(benchmark(lambda : selection_sort_recursive([2, 3, 4, 1, 4, 56, -2, 20]))))