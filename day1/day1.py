totalCount1 = 0
totalCount2 = 0
lastNumber = 9999999
measurement1 = 0
measurement2 = 0
measurement3 = 0
lastSum = 0

with open("day1_input", "r") as f:
    '''
    for i in f:
        if int(lastNumber) < int(i):
            totalCount1 += 1
        lastNumber = i
    print(totalCount1)
    '''

    for i in f:
        measurementSum = int(measurement1) + int(measurement2) + int(measurement3)
        if int(measurementSum) > int(lastSum):
            totalCount2 += 1
        measurement3 = measurement2
        measurement2 = measurement1
        measurement1 = i
        lastSum = measurementSum
    print(totalCount2 - 2)


