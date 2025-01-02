def selection_sort(arr):
   for i in range(len(arr)):
       min_index = i
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       arr[i], arr[min_index] = arr[min_index], arr[i]

mas = [7, -3, 12, 0, -8, 5, 3, -10, 9, 2, -1, 8, 4, -6, 11]

print(mas)
selection_sort(mas)
print(mas)

