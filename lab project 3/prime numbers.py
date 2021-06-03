# # def prime_number(num):
# #     count=0
# #     if num==1:
# #         return (False)
# #     elif num==2:
# #         return(True)
# #     else:
# #         for i in range(1,num+1):
# #             if num%i==0:
# #                 count+=1
# #     if count==2:
# #         return(True)
# #     else:
# #         return(False)
# #
# #
# #
# #
# #
# # num=11
# # print(prime_number(num))
#
# #Armstrong number
# # def armstrong(num):
# #
# #     while num!=0:
# num=5
# def lol(num):
#     for i in range(1,num+1):
#         for j in range (1,i+1):
#             print(j,end="")
#         print()
#
#
# lol(num)
# print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
# k=1
# for i in range (1,6):
#     for j in range(1,i):
#         print(j,end="")
#         k+=1
#     print()
# # n=3
# # def mul3(n):
# #     if n==1:
# #         return 3
# #     else:
# #         return 3+mul3(n-1)
# #
# # print(mul3(n))'

# def armstromg(num):
#     temp=num
#     sum=0
#     while temp>0:
#         rem=temp%10
#         sum+=(rem**3)
#         temp=temp//10
#     if sum==num:
#         return(True)
#     else:
#         return(False)
#
# print(armstromg(13))

# string='bas'
# str=string[::-1]
# print (str)
# import turtle
# pen=turtle
# for i in range(4):
#     pen.forward(200)
#     pen.right(90)
# turtle.done()
# n=0
# def fibonacci(num):
#     if n <= 1:
#         return n
#
#     else:
#         return (fibonacci(num - 1) + fibonacci(num - 2))
# print(fibonacci(5))


myList = []


# def sumofList(myList, nSum):
#     if len(myList):
#         return sumofList(myList[1:], nSum + myList[0])
#     else:
#         return nSum
#
#
# print(sumofList(myList, 0))


# list = [1, 2, 3, 4, 5]
# s = 0
# for i in range(len(myList)):
#     s = s + myList[i]
# print(s)
# print(max(myList))
def mul3(n, i):
    if i > 10:
        return
    print(n, 'x', i, '=', n * i)
    return mul3(n, i + 1)


mul3(3, 1)
