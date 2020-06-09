def maxValue(n, rounds):
    low, high, max_investment = rounds[0]
    print(low, high, max_investment)
    for left, right, contribution in rounds[1:]:
        if contribution > max_investment:
            if low < left:
                pass

print(maxValue(5, [[1,2,10],[2,4,5],[3,5,12]]))