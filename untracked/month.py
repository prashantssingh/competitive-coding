import calendar

def ada(year):
  daysList = calendar.monthcalendar(year, 10)
  count = 0
  i = 0
  while i < len(daysList):
    if count == 2: break
    if daysList[i][1]:
      count += 1
    i += 1
  print (daysList)
  return (daysList[i - 1][1])

print(ada(2016))