#linearsearch

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1
arr = [2,5,6,1,5]
x = 6
res = search(arr,x)
print("elm is at index: ",res)
