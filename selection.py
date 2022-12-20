def selectionSort(arr, size):
    flag = 0
    for i in range(size):
        min_index = i

        for j in range(ind + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
                flag = 1
        if flag == 1:
            (arr[i], arr[min_index]) = (arr[min_index], arr[i])


arr = []
lim = int(input("limit: "))
i = 0
for i in range(lim):
    elm = int(input("elm: "))
    arr.append(elm)
    lim = lim - 1

selectionSort(arr, lim)
print('final array:')
print(arr)
