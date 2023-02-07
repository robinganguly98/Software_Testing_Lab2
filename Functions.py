def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        for j in range(arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def searching(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1

def membership(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return 1
    return 0



if __name__ == "__main__":
    arr1 = [1, 0, 9, 6, 7, 1, 0]
    bubble_sort(arr1)
    print(arr1)

    arr2 = [1, 0, 9, 6, 7, 1, 0]
    print(searching(arr2, 0))