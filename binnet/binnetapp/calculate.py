from .models import Ranking 
from datetime import timedelta

def filterWeekDay(measurements) -> list[float]:
    # Split measurements into weekdays
    ans = {i: [] for i in range(1, 8)}

    for measurement in measurements:
        ans[measurement.measureDate.weekday()].append(measurement)
    
    return ans


def calculateFillrate(measurements) -> float:

    # Calculates fillrate of a single list
    # Returns fillrate as cm/hour
    
    maxMeasurement = measurements[-1]
    minMeasurement = measurements[0]

    valueDelta = abs(maxMeasurement.value - minMeasurement.value)
    timeDelta = timedelta(days=maxMeasurement.measureDate.day - minMeasurement.measureDate.day, hours=maxMeasurement.measureTime.hour - minMeasurement.measureTime.hour)
    hourDelta = timeDelta.total_seconds() // 3600
    print([m.value for m in measurements])
    print(valueDelta, hourDelta)
    return (valueDelta) / (hourDelta)


def calculateIncreasing(measurements) -> list[list[float]]:

    # Calculates increasing parts of the measurements
    # E.g. Output: [[5, 12], [5, 58, 59], [57], [12, 34, 67]]

    increasingSublists = [[measurements[0]]]

    for i in range(1, len(measurements)):

        isIncreasing = measurements[i-1].value < measurements[i].value
        isDiff = abs(measurements[i-1].value - measurements[i].value) < 10

        if isIncreasing or isDiff:
            increasingSublists[-1].append(measurements[i])
        else:
            increasingSublists.append([measurements[i]])
    
    # Go through each part and calculate fillrate
    fillrate = []
    for part in increasingSublists:
        if len(part) > 1:
            fillrate.append(calculateFillrate(part))
        else:
            fillrate.append(0.0)

    return increasingSublists, fillrate


def calculateRanking(measurements) -> dict[int, Ranking.Color]:
    # Input: List of measurements
    # Output: Color of the ranking for each weekday

    # Split measurements into weekdays
    measurements = filterWeekDay(measurements)

    for key, value in measurements.items():
        if len(value) != 0:
            
            measurements[key], fillrate = calculateIncreasing(value)
            
            # Calculate average fillrate of every fillrate
            avgFillrate = sum(fillrate) / len(fillrate)
            
            # DETERMINE RANKING
            RED_THRESHOLD = 20
            ORANGE_THRESHOLD = 15
            GREEN_THRESHOLD = 5

            if avgFillrate >= RED_THRESHOLD:
                measurements[key] = (avgFillrate, Ranking.Color.RED)
            
            elif avgFillrate >= ORANGE_THRESHOLD:
                measurements[key] = (avgFillrate, Ranking.Color.ORANGE)
            
            elif avgFillrate >= GREEN_THRESHOLD:
                measurements[key] = (avgFillrate, Ranking.Color.GREEN)
            
            else:
                measurements[key] = (avgFillrate, Ranking.Color.GREEN)
            
    return measurements