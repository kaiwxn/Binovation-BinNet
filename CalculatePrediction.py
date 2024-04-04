
def calculateIncreasing(measurements):

    
    increasingSublists = [[measurements[0]]]

    for i in range(1, len(measurements)):

        isIncreasing = measurements[i-1] < measurements[i]
        isDiff = abs(measurements[i-1] - measurements[i]) < 10

        if isIncreasing or isDiff:
            increasingSublists[-1].append(measurements[i])
        else:
            increasingSublists.append([measurements[i]])

    # Go through each part and calculate fillrate
    fillrate = []
    for part in increasingSublists:
        fillrate.append(calculateFillrate(part))

    return increasingSublists, fillrate


def calculateFillrate(measurements) -> float:

    # Calculates fillrate of a single list
    maxMeasurement = measurements[-1]
    minMeasurement = measurements[0]

    return (maxMeasurement - minMeasurement) / 1

def filterWeekDay(measurements) -> list[float]:
    # Split measurements into weekdays
    ans = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }

    for measurement in measurements:
        ans[measurement[1]].append(measurement[0])
    
    return ans

def main():
    example = [(5, 1), (24, 1), (1, 1), (12, 1), (5, 2), (58, 2), (59, 2), (57, 3), (12, 4), (34, 4), (67, 4)]

    args = filterWeekDay(example)

    # Calculate increasing parts of the measurements
    # Format: {1: [[5, 24], [1, 12]], 2: [[5, 58, 59]], 3: [[57]], 4: [[12, 34, 67]], 5: [], 6: [], 7: []}
    for key, value in args.items():
        if len(value) > 0:
            args[key], fillrate = calculateIncreasing(value)

            # Calculate average fillrate of every fillrate
            # len() SHOULD BE difference of time 
            avgFillrate = sum(fillrate) / len(fillrate)
            
            # NOW: DETERMINE RANKING
            RED_THRESHOLD = 15
            ORANGE_THRESHOLD = 10
            GREEN_THRESHOLD = 5

            if avgFillrate >= RED_THRESHOLD:
                args[key] = (avgFillrate, "Ranking.Color.RED")
            
            elif avgFillrate >= ORANGE_THRESHOLD:
                args[key] = (avgFillrate, "Ranking.Color.ORANGE")
            
            elif avgFillrate >= GREEN_THRESHOLD:
                args[key] = (avgFillrate, "Ranking.Color.GREEN")
            
            else:
                args[key] = (avgFillrate, "Ranking.Color.GREEN")
    
    print(args)
    print("\n")
    


if __name__ == "__main__":
    main()