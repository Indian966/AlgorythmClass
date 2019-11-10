S = [5, 8, 1, 3, 7, 2, 6, 9]


def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            return mid

print(binary_search(S, 9))