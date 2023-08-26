def selection_sort_recursive(list):

    if len(list) == 0:
        return []
    
    minElement = min(list)

    list.remove(minElement)

    result = selection_sort_recursive(list)

    result.insert(0, minElement)

    return result

if __name__ == '__main__':
    print("Expecting: [-1, 2, 3, 5]")
    print(selection_sort_recursive([3, -1, 5, 2]))

    print("")

    print("Expecting: [5]")
    print(selection_sort_recursive([5]))

    print("")

    print("Expecting: [-1, 2, 2, 3, 3, 5]")
    print(selection_sort_recursive([3, 2, -1, 3, 5, 2]))

    print("")

    print("Expecting: [3, 5]")
    print(selection_sort_recursive([5, 3]))

    print("")