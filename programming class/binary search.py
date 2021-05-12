def binary_search(list, st):
    min = 0
    max = len(list) - 1
    while min < max:
        mid = min + max // 2
        if st == list[mid]:
            return mid

        elif st < list[mid]:
            max = mid - 1

        else:
            min = mid + 1

    return -1


l1 = [6, 2, 1, 4, 5, 8, 6]
l1.sort()
l2=[2,4,6,8,10]
print(l1)
item = 10
print(binary_search(l2, item))
