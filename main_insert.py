mas = [7, -3, 12, 0, -8, 5, 3, -10, 9, 2, -1, 8, 4, -6, 11]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print(mas)
insert_sort(mas)
print(mas)
