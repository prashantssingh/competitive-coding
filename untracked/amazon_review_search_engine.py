def search(numRevies, repo, queryStr):
  searchResult = list()
  for i, _ in enumerate(queryStr, start = 2):
    search = queryStr[:i]
    currRes = list()
    for each in repo:
      if search in each:
        currRes.append(each)

    if len(currRes) > len(searchResult):
      searchResult = currRes
  
  return searchResult

print(search(5, ["money", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))