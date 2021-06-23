def bubble_short(list):
    swap=True
    while swap:
        swap:False
        for i in range (len(list)-1):
            if list[i]>list[i+1]:
                list[1],list[i+1]=list[i+1],list[i]
                swap=True

    return list
print(bubble_short([1,5,8,3]))


#n*n=nO(n^2)-runtime of an algorithm
