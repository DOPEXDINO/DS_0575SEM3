#binarysearch
def binary_search(arr, low, high, x):

	if high >= low:

		mid = (high + low) // 2

		
		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1


arr = []
lim = int(input("limit: "))

for i in range(lim):
          elm = int(input("elm: "))
          arr.append(elm)
          lim = lim-1
pivot = int(input("pivot: "))
result = binary_search(arr, 0, len(arr)-1, pivot)

if result != -1:
	print("Element is present at: ", str(result))
else:
	print("Element not present")
