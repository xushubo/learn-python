array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

# insert_sort
for i in range(1, len(array)):
    if array[i - 1] > array[i]:
        temp = array[i]     # 当前需要排序的元素
        index = i           # 用来记录排序元素需要插入的位置
        while index > 0 and array[index - 1] > temp:
            array[index] = array[index - 1]     # 把已经排序好的元素后移一位，留下需要插入的位置
            index -= 1
        array[index] = temp # 把需要排序的元素，插入到指定位置

# print sort result.
print(array)