from .models import Ranking 

def splitWeekDay(measurements: list[float]) -> dict[int, list]:
    # Splits measurements into weekdays
    ans = {i: [] for i in range(1, 8)}

    for measurement in measurements:
        ans[measurement.measureDate.weekday()].append(measurement)
    
    return ans



def splitDecreasing(measurements: list[float]) -> list[list[float]]:

    # Splits decreasing parts of the measurements
    # E.g. Output: [[24, 12, 4, 1], [56, 47, 43, 4], [4]]

    decreasingSublists = [[measurements[0]]]

    for i in range(1, len(measurements)):

        # If value is decreasing or difference is less than 10cm
        isDecreasing = measurements[i-1].value > measurements[i].value
        isDiff = abs(measurements[i-1].value - measurements[i].value) < 10

        if isDecreasing or isDiff:
            decreasingSublists[-1].append(measurements[i])
        else:
            decreasingSublists.append([measurements[i]])
    
    # Go through each part and calculate sum of differences
    sumDiff = 0.0
    for part in decreasingSublists:
        sumDiff += part[0] - part[-1]

    return decreasingSublists, sumDiff, len(decreasingSublists)


def calculateRanking(measurements: list[float]) -> dict[int, Ranking.Color]:
    # Input: List of measurements for each weekdaz
    # Output: Color of the ranking for each weekday

    # Split measurements into weekdays
    measurements = splitWeekDay(measurements)

    for day, values in measurements.items():

        if values != []:
            countMeasurements = len(values)

            # [DecreasingSublists, sumDiff]
            measurements[day], sumDiff, countSublists = splitDecreasing(values)

            # Number of Differences in one day = Number of measurements - Number of sublists
            # Because each sublist has len(sublist) - 1 differences
            countDelta = countMeasurements - countSublists

            # Calculate average fillrate of one weekday
            fillrate = round(sumDiff / countDelta, 3)
            
            # DETERMINE RANKING (In cm/hour)
            # Thresholds for ranking are based on experimental results
            RED_THRESHOLD = 20
            ORANGE_THRESHOLD = 15
            GREEN_THRESHOLD = 5

            if fillrate >= RED_THRESHOLD:
                measurements[day] = (fillrate, Ranking.Color.RED)
            
            elif fillrate >= ORANGE_THRESHOLD:
                measurements[day] = (fillrate, Ranking.Color.ORANGE)
            
            elif fillrate >= GREEN_THRESHOLD:
                measurements[day] = (fillrate, Ranking.Color.GREEN)
            
            else:
                measurements[day] = (fillrate, Ranking.Color.GREEN)
            
    return measurements