#Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
	for i in range(d):
		leftRotatebyOne(arr,n)

#Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr,n):
	temp = arr[0]
	for i in range(n-1):