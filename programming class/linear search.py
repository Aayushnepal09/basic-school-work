def Linear_search(list, search_item):
    for i in range(len(list)):
        if search_item == list[i]:
            return i

    return -1


l1 = [6, 2, 1, 8, 0, 3]

item = 3
print(Linear_search(l1, item))
