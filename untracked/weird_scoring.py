import math
def exam(v):
  examCount = 0
  oneCount = v.count(1)
  zeroCount = v.count(0)

  if oneCount == 0 :
    return examCount

  mustTakeExamCount = math.ceil((oneCount - zeroCount) / 2)

  for exam in v:
    if mustTakeExamCount != 0:
      if exam == 1:
        mustTakeExamCount -=1
      else:
        mustTakeExamCount +=1
      examCount += 1

  return examCount

print(exam([1,1,1,0,1]))