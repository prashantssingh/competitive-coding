def maximumTotalWeight(tasks, weights, p):
  weightToTaskProportionDict = dict()
  tasksDoubled = [2*task for task in tasks]
  for i in range(0, len(tasks)):
    key = weights[i]/(tasksDoubled[i])
    weightToTaskProportionDict[key] = [tasksDoubled[i], weights[i]]
  print(weightToTaskProportionDict)
  proportionList = sorted(weightToTaskProportionDict.keys(), reverse=True)
  weightToReturn = 0
  for proportion in proportionList:
    item = weightToTaskProportionDict[proportion]
    print("task:",item[0],", weight:", item[1], ", p:", p)
    if item[0] < p:
      weightToReturn += item[1]
      p -= item[0]

  return weightToReturn

# print(maximumTotalWeight([1,4,6,3],[1,2,2,3],8))
# print(maximumTotalWeight([1,2,2,3],[1,4,6,3],8))
# print(maximumTotalWeight([3,2,2],[3,2,2],9))
print(maximumTotalWeight([1,4,2,5,3],[2,6,4,7,1],13))