import sys
import math

def get_travel_time(From, To):
    x_travel = From[0] - To[0]
    y_travel = From[1] - To[1]

    if(x_travel < 0):
        x_travel = x_travel * -1
    if(y_travel < 0):
        y_travel = y_travel * -1

    return (x_travel + y_travel)

Input = sys.stdin.readlines()#"4\n0 1\n2 5\n3 1\n4 0"#"6\n12 -14\n-3 3\n-14 7\n-14 -3\n2 -12\n-1 -6"##raw_input()
Houses = list()

## Push the input into a list of positions
for line in Input:
    line_splt = line.split(" ")
    if(len(line_splt) == 2):
        Houses.append(list({int(line_splt[0]), int(line_splt[1])}))

TravelTimes = list()
x = 0
for travel_to in Houses:
    TravelTimes.append(0)
    for travel_from in Houses:
        TravelTimes[x] += get_travel_time(travel_from, travel_to)
    x+=1

Total_Time = TravelTimes[0]
for Time in TravelTimes:
    if(Time < Total_Time):
        Total_Time = Time

#print TravelTimes
print Total_Time