# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
#
# print(factorial(5))
# def mul(num):
#     if num==1:
#         return 3
#     else:
#         return(3+mul(num-1))
#
# for i in range(1,11):
#     print(mul(i))


# lst=[2,4,6,8]
# for i in list:
#     sum+=i
# print(sum)


l=[2,4,6,8]
def sum(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+sum(l[1:])

print(sum(l))
