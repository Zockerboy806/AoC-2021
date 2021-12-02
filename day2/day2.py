totalForward = 0
totalDown = 0
aim = 0

with open("day2_input", "r") as f:
    for i in f:
        if i.__contains__("forward"):
            totalForward = totalForward + int(i[8])
            totalDown = totalDown + (int(i[8]) * aim)

        elif i.__contains__("up"):
            totalDown = totalDown - int(i[3])
            aim = aim - int(i[3])

        elif i.__contains__("down"):
            totalDown = totalDown + int(i[5])
            aim = aim + int(i[5])

    print("Depth: " + str(totalForward) + " Forward: " + str(totalDown) + " Result: " + str(totalForward * totalDown) + "\n" +
        "Aim: " + str(aim))