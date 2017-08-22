array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

for i in range(1, len(array)):
	if (array[i - 1] > array[i]):
		temp = array[i]
		index = i
		while index > 0 and array[index - 1] > temp:
			array[index] = array[index - 1]
			index -= 1
		array[index] = temp

print(array)