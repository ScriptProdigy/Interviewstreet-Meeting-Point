import math

Input = "6\n12 -14\n-3 3\n-14 7\n-14 -3\n2 -12\n-1 -6"##raw_input()
Houses = list()

## Push the input into a list of positions
for line in Input.split("\n"):
    line_splt = line.split(" ")
    if(len(line_splt) == 2):
        Houses.append(list({int(line_splt[0]), int(line_splt[1])}))

print Houses

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

print "MIDDLE: " + str(Middle_Home)