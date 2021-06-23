#WAP which accepts marks of four subject and display total marks, percentage and
#grade
mark_of_1st_subject=int(input("enter the mark of first subject"))
mark_of_2nd_subject=int(input("enter the mark of second subject"))
mark_of_3rd_subject=int(input("enter the mark of third subject"))
mark_of_4th_subject=int(input("enter the value of fourth subject"))

total_mark=400
total_mark_scored=(mark_of_4th_subject+mark_of_2nd_subject+mark_of_3rd_subject+mark_of_1st_subject)
percentage=(total_mark_scored/total_mark)*100

if percentage>= 70:
    print(f"your percentage is{percentage}% and have scored total mark of{total_mark_scored} out of {total_mark} and your grade is A")
elif percentage<70 and >