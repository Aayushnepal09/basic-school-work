#you live 4 miles from the university, the bus drives at 25mph but spend 2 min at each of the 10 stops on
#the way . how long the bus journey take? alternatively, you could run to the university .yo joh the first
#mile at 7mph, then run next 2 at 15mph, before jogging last at 7mph again will this be quicker or
# slower then the bus
distance_to_university=4
speed_of_bus=25
time_taken=((distance_to_university/speed_of_bus)*60)
no_of_stop=10
time_spend_at_stop=2
total_time_bus_stops=(no_of_stop*time_spend_at_stop)
Total_time_by_bus=(time_taken+total_time_bus_stops)
print(f"total time taken by bus is {Total_time_by_bus}")

jog_one=((1/7)*60)
jog_two=((2/15)*60)
jog_three=((1/7)*60)
total_time_by_jog= jog_one+jog_two+jog_three
print(f"total time taken by jog is {total_time_by_jog}")

if (total_time_by_jog > Total_time_by_bus):
    print("taking bus is quicker then running")
else:
    print("Taking bus is slower then running")
