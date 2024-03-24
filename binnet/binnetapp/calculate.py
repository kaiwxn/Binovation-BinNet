import datetime

def splitWeekDay(measurements):
    # Split measurements into weekdays
    ans = []
    for measurement in measurements:
        if measurement.measureDate.getWeekday() == datetime.datetime.now().weekday():
            ans.append(measurement)
    return 

def calculateRanking(measurements) -> str:

    # 1. Calculate increasing parts of the measurements
    # 2. Calculate average of those squences
    # 4. Return color based on average

    # 1.
    increasingSublists = [[measurements[0].value]]

    for i in range(1, len(measurements)):
        if measurements[i-1].value < measurements[i].value or abs(measurements[i-1].value - measurements[i].value) < 10:
            increasingSublists.append(measurements[i].value)
        else:
            increasingSublists.append([measurements[i].value])



    
    return