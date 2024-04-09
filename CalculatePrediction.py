
def splitDecreasing(measurements) -> list[list[float]]:

    # Splits decreasing parts of the measurements
    # E.g. Output: [[24, 12, 4, 1], [56, 47, 43, 4], [4]]
    decreasingSublists = [[measurements[0]]]
    
    for i in range(1, len(measurements)):

        # If value is decreasing or difference is less than 10cm
        isDecreasing = measurements[i-1] > measurements[i]
        isDiff = abs(measurements[i-1] - measurements[i]) < 10

        if isDecreasing or isDiff:
            decreasingSublists[-1].append(measurements[i])
        else:
            decreasingSublists.append([measurements[i]])
    
    # Go through each part and calculate sum of differences
    sumDiff = 0
    for part in decreasingSublists:
        sumDiff += part[0] - part[-1]

    return decreasingSublists, sumDiff, len(decreasingSublists)

def filterWeekDay(measurements) -> list[float]:
    # Split measurements into weekdays
    ans = {i: [] for i in range(1, 8)}

    for measurement in measurements:
        ans[measurement[1]].append(measurement[0])
    
    return ans

def main():
    example = [(24, 1), (12, 1), (0, 1), (24, 1), (12, 1), (0, 1), (60, 2), (40, 2), (20, 2), (0, 2)]

    args = filterWeekDay(example)
    print(args)
    # Calculate increasing parts of the measurements
    # Format: dict[int, list]
    for key, value in args.items():
        
        if value != []:
            # [DecreasingSublists, sumDiff]
            countMeasurements = len(value)

            args[key], sumDiff, countSublists = splitDecreasing(value)


            # Number of Differences in one day = Number of measurements - Number of sublists
            # Because each sublist has len(sublist) - 1 differences
            countDelta = countMeasurements - countSublists

            # Calculate average fillrate of one weekday
            fillrate = round(sumDiff / countDelta, 3)

            # args[key] = fillrate
            print(f"{fillrate=}, {countDelta=}, {sumDiff=}, {len(example)=}, {len(value)=}")

    print(args)
    
    print("\n")
    


if __name__ == "__main__":
    main()