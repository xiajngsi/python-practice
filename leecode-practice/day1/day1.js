function getSumIndexArr(nums, sum){
  const result = []
  nums.forEach((num, index) => {
    if(!result.includes(index)) {
      const complement = sum - num
      const compIndex = nums.indexOf(complement)
      if(compIndex !== -1) {
        result.push(index)
        result.push(compIndex)
      }
    }
  })
  console.log(result);
} 
  
getSumIndexArr([1, 3, 9, 2, 8, 7, 4], 10)