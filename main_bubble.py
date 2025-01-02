mas = [7, -3, 12, 0, -8, 5, 3, -10, 9, 2, -1, 8, 4, -6, 11]
print(mas)

n = len(mas)
for run in range(n-1):
   for i in range(n-1-run):
       if mas[i] > mas[i + 1]:
           mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)

