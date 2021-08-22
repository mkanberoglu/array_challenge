def ArrayChallenge(arr):
  mem = sorted(arr)
  maxi = mem[-1]
  mem.remove(maxi)
  summ = sum(mem)
  diff = summ - maxi 

  if summ == maxi:
    return 'true'
  
  if any(diff == x for x in mem):
    return 'true'
  
  if summ > maxi:
    for i in range(len(mem)):
      if diff - mem[i] > diff:
        summ = summ - mem[i]
        if summ == maxi:
          return 'true'
    return 'false'
    
  elif summ < maxi: 
    for i in range(len(mem)):     
      if mem[i] < 0:
        summ = summ - mem[i]
        if summ == maxi:
          return 'true'
    return 'false'



# keep this function call here 
print(ArrayChallenge(input()))