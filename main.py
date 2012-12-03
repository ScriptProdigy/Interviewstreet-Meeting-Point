import math

def get_travel_time(From, To):
    x_travel = From[0] - To[0]
    y_travel = From[1] - To[1]

    if(x_travel < 0):
        x_travel = x_travel * -1
    if(y_travel < 0):
        y_travel = y_travel * -1

    return (x_travel + y_travel)

Input = "6\n12 -14\n-3 3\n-14 7\n-14 -3\n2 -12\n-1 -6"##raw_input()
Houses = list()

## Push the input into a list of positions
for line in Input.split("\n"):
    line_splt = line.split(" ")
    if(len(line_splt) == 2):
        Houses.append(list({int(line_splt[0]), int(line_splt[1])}))

## Find the middle position of all the houses
Middle_Position = list(Houses[0])

for House in Houses:
    Middle_Position[0] += House[0]
    Middle_Position[1] += House[1]

Middle_Position[0] = int(Middle_Position[0]/len(Houses))
Middle_Position[1] = int(Middle_Position[1]/len(Houses))

## Finally, find the house closest to the Middle Position
Middle_Home = Houses[0] ## The position of the home in the list Houses, default 0

for House in Houses:
    x2 = (Middle_Position[0]-House[0])^2
    y2 = (Middle_Position[1]-House[1])^2

    added = x2 + y2
    if(added < 0):
        added = added * -1

    new_distance = math.sqrt(added)

    x2 = (Middle_Position[0]-Middle_Home[0])^2
    y2 = (Middle_Position[1]-Middle_Home[1])^2

    added = x2 + y2
    if(added < 0):
        added = added * -1

    cur_distance = math.sqrt(added)

    if(new_distance < cur_distance):
        Middle_Home = House

Middle_Position = Middle_Home

## Lastly, Add the sum of the distance to the new middle home
Total_Time = 0
for House in Houses:
    x2 = (Middle_Position[0]-House[0])^2
    y2 = (Middle_Position[1]-House[1])^2

    added = x2 + y2
    if(added < 0):
        added = added * -1

    distance = math.sqrt(added)
    Total_Time += round(math.sqrt(added))

print Total_Time