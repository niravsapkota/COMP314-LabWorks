def getStrings(n):
    return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]


def bruteKnapsack(weights, profits, capacity):
    assert len(weights) == len(profits)
    n = len(profits)
    bitStrings = getStrings(n)

    list = []
    for s in bitStrings:
        p = sum([int(s[i])*profits[i] for i in range(n)])
        w = sum([int(s[i])*weights[i] for i in range(n)])

        if (w <= capacity):
            list.append((w, p))

    maxProfit = max(list, key=lambda tup: tup[1])
    return (maxProfit[1])


def bruteFracKnapsack(weights, profits, capacity):
    assert len(weights) == len(profits)
    n = len(profits)
    bitStrings = getStrings(n)
    maxProfit = 0

    for s in bitStrings:
        a = []
        for i, x in enumerate(s):
            if x == '0':
                a.append(i)

        p = sum([int(s[i])*profits[i] for i in range(n)])
        w = sum([int(s[i])*weights[i] for i in range(n)])

        fraction = 0

        if w < capacity:
            for i in a:
                if capacity-w < weights[i]:
                    remain = capacity - w
                else:
                    remain = weights[i]

                frac = (profits[i]/weights[i])*remain
                if frac > fraction:
                    fraction = frac
        p += fraction

        if w <= capacity and p >= maxProfit:
            maxProfit = p

    return maxProfit


def greedyKnapsack(weights, profits, capacity):
    assert len(weights) == len(profits)
    n = len(profits)
    ratios = [(profits[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)

    result = 0
    for ratio, i in ratios:
        if capacity == 0:
            return result
        amount = min(weights[i], capacity)
        result += amount * ratio
        capacity -= amount

    return result


# Dynamic Programming using the Bottom-Up Approach
def dynamicKnapsack(weights, profits, capacity):
    assert len(weights) == len(profits)
    n = len(profits)

    # Initialize a 2D array of size n+1 and capacity+1
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Calculating the maximum profit for every possible values of capacity and items
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(profits[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][capacity]
