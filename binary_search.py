def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    array = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    target = 3
    print(binary_search(array, target)) # index -1
    target = 1
    print(binary_search(array, target)) # index 0
