#a school decides to replace the desk in three clasroom. each desk sits two students.
# given the number of students in  each class , print the smallest possible number of
# desks that can be purchased
#he program should read three integers the number of students in each of three classes a , b, c respectively
#in the first test there are  three groups. the first group has 20 student thus needs 10 desk, the second has 21
#so the can get by with fewer then 11 desk. 11 desks are also enough for the third group sowe need 32 desk in total
no_of_student_class1=int(input("enter the number sof students in class 1"))
no_of_student_class2=int(input("enter the number of student in class 2"))
no_of_student_class3=int(input("enter the number of students in class 3"))

desk_for_class1=(no_of_student_class1//2)
desk_for_class2=(no_of_student_class2//2)
desk_for_class3=(no_of_student_class3//2)

print(f"the require number of desk for first class is{desk_for_class1}")
print(f"the number of desk for second class is{desk_for_class2}")
print(f'the number of desk for third class is{desk_for_class3}')

remain_class1=no_of_student_class1 % 2
print(f"remaining desk for class 1 {remain_class1} ")

remain_class2=no_of_student_class2 % 2
print(f'remaining desk for class 2 {remain_class2}')

remain_class3=no_of_student_class3 % 2
print(f'remaining desk for class 2 {remain_class3}')

total_desk=desk_for_class1+desk_for_class2+desk_for_class3+remain_class1+remain_class2+remain_class3
print(f"total number of desk that can be purchase is {total_desk}")