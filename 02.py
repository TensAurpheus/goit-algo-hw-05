def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    iter = 0

    if upper_bound < x:
        return -1, iter

    while low <= high:

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return mid, iter
        iter += 1
    # якщо елемент не знайдений
    return -1, iter


if __name__ == '__main__':
    arr = [3.5, 4.1, 10, 40.2, 50.09, 60.3, 70, 80.4, 94.20, 100]
    x = 5

    result = binary_search(arr, x)
    next_el_output = f' next element is {arr[result[0] + 1]}' if result[0] != len(arr) - 1 else ' this is the highest element in the array'

    if result[0] != -1:
        print(f"Element is present at index {str(result[0])}, found in {result[1]} iterations,", next_el_output)
    else:
        print("Element is not present in array")