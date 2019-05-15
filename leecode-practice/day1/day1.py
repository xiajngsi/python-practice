def getSumIndexArr(nums, sum):
  result = []
  for i, num in enumerate(nums):
    if i not in result: 
      complement = sum - num
      for currIndex, value in enumerate(nums):
        if value == complement:
          result.append(i)
          result.append(currIndex)
  print(result)

getSumIndexArr([1, 3, 9, 2, 8, 7, 4], 10)