# warmup-1 
def not_string(str):
  if len(str) >=3 and str[0:3] == 'not': #str[:3] can also be written 
    return str
  else:
    return ('not '+str)

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if len(str) < 2:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]
  
def front3(str):
  if len(str) < 3:
    return str + str + str
  else:
    return str[:3] + str[:3] + str[:3] 

#warmup-2
def string_times(str, n):
  result = ""
  for i in range(n):
    result  += str
  return result

def front_times(str, n):
  result = ""
  
  if len(str) < 3:
    value = str 
  else:
    value = str[:3]
    
  for i in range(n):
    result += value
  return result

def string_bits(str):
  result = ""
  i = 0
  while i in range(len(str)):
    result += str[i]
    i = i + 2
  return result

def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = str[:len(str)-i] + result
  return result 

def last2(str):
  if len(str) < 2:
    return 0
  count = 0
  for i in range(len(str)-2):
    if str[-2:] == str[i:i+2]:
      count +=1
  return count

def array_count9(nums):
  count = 0
  for i in nums:
    if i == 9:
      count +=1
  return count

def array_front9(nums):
  for i in range(len(nums)):
    if(i < 4 and nums[i]==9):
      return True
  return False

def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

def string_match(a, b):
  length = len(a)
  
  if len(a) > len(b): #take the smaller string
    length = len(b)

  count = 0

  for i in range(length-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
      
  return count