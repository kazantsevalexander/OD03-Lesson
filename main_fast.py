def quick_sort(s):
   if len(s) <= 1:
       return s

   element = s[0]
   left = list(filter(lambda i: i < element, s))
   center = [i for i in s if i==element]
   right = list(filter(lambda i: i > element, s))

   return quick_sort(left) + center + quick_sort(right)

mas = [7, -3, 12, 0, -8, 5, 3, -10, 9, 2, -1, 8, 4, -6, 11]
print(mas)
print(quick_sort(mas))
