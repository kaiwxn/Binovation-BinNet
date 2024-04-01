from .models import Ranking 

import datetime

def filterWeekDay(measurements) -> list[float]:
    # Split measurements into weekdays
    ans = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }

    for measurement in measurements:
        ans[measurement.measureDate.getWeekday()].append(measurement)
    
    return ans


def calculateFillrate(measurements) -> float:

    # Calculates fillrate of a single list
    maxMeasurement = measurements[-1].value
    minMeasurement = measurements[0].value

    return (maxMeasurement - minMeasurement) / (maxMeasurement.measureTime - minMeasurement.measureTime)


def calculateIncreasing(measurements):

    # Calculates increasing parts of the measurements
    # E.g. Output: [[5, 12], [5, 58, 59], [57], [12, 34, 67]]

    increasingSublists = [[measurements[0].value]]

    for i in range(1, len(measurements)):

        isIncreasing = measurements[i-1].value < measurements[i].value
        isDiff = abs(measurements[i-1].value - measurements[i].value) < 10

        if isIncreasing or isDiff:
            increasingSublists[-1].append(measurements[i].value)
        else:
            increasingSublists.append([measurements[i].value])
    
    return increasingSublists


def calculateRanking(measurements) -> Ranking.Color:
    # Input: List of measurements
    # Output: Color of the ranking for each weekday

    # Get only today's measurements
    measurements = filterWeekDay(measurements)
    
    increasingParts = calculateIncreasing(measurements)
    
    # Go through each part and calculate fillrate
    fillrate = []
    for part in increasingParts:
        fillrate.append(calculateFillrate(part))

    # Calculate average fillrate
    avgFillrate = sum(fillrate) / len(fillrate)

    RED_THRESHOLD = 15
    ORANGE_THRESHOLD = 10
    GREEN_THRESHOLD = 5

    if avgFillrate >= RED_THRESHOLD:
        return Ranking.Color.RED
    
    elif avgFillrate >= ORANGE_THRESHOLD:
        return Ranking.Color.ORANGE
    
    elif avgFillrate >= GREEN_THRESHOLD:
        return Ranking.Color.GREEN
    
    else:
        return Ranking.Color.GREEN