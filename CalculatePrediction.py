
def getBounds(val) -> tuple[int, int]:

    # minDist: Lowest measurement value -> highest point in garbage bin
    # maxDist: Highest measurement value -> lowest point in garbage bin
    minDist = 1e5
    maxDist = -1

    for num in val:
        minDist = min(num, minDist)
        maxDist = max(num, maxDist)

    return minDist, maxDist
    

def calculateFillRate(val) -> float:
    
    # Calculate fill rate
    minDist, maxDist = getBounds(val)
    fillRate = (maxDist - minDist) / maxDist

    return round(fillRate, 2)


def solveIncreasingValues() -> list[list[int]]:

    values = [5, 12, 5, 58, 59, 57, 12, 34, 67]
    weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    solution = []
    temp = []

    minDist, maxDist = getBounds(values)
    
    
    # Search for increasing values
    oldVal = values[0]
    for num in values:

        # If increasing or close to previous value
        if num > oldVal or abs(num - oldVal) < 5:
            temp.append(num)
        elif num < oldVal:
            solution.append((temp, calculateFillRate(temp)))
            temp = [num]
        oldVal = num

    solution.append((temp, calculateFillRate(temp)))

    return solution



def main():
    args = solveIncreasingValues()
    print(args)

if __name__ == "__main__":
    main()