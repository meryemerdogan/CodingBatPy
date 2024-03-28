############################################
############### lists-1 ###################
############################################

def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  if len(nums) > 0:
    return nums[0] == nums[len(nums)-1]
  return False
  
def make_pi():
  pi = [3,1,4]
  return pi

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
  
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
  temp = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = temp
  return nums

def reverse3(nums):
  temp = nums[0]
  nums[0] = nums[2]
  nums[2] = temp
  return nums

def max_end3(nums):
  if nums[0] > nums[2]:
    nums[1] =  nums[0]
    nums[2] =  nums[0]
  else:
     nums[1] =  nums[2]
     nums[0] =  nums[2]
  return nums

def sum2(nums):
  if len(nums) == 0: 
    return 0
  elif len(nums) == 1: 
    return nums[0]
  else:
    return nums[0] + nums[1]

def middle_way(a, b):
  array = [a[1], b[1]]
  return array

def make_ends(nums):
  array = [ nums[0],  nums[-1]]
  return array

def has23(nums):
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3

############################################
############### lists-2 ###################
############################################

def count_evens(nums):
  count = 0
  for i in nums:
    if i%2 == 0:
      count += 1
  return count

def big_diff(nums):
  minimum = nums[0]
  maximum = nums[0]
  for i in nums:
    minimum =  min( minimum, i)
    maximum =  max( maximum, i)
  diff = maximum -minimum
  return diff

def centered_average(nums):
  s = nums[0]
  b = nums[0]
  total = 0
  
  for i in nums:
    s = min (s, i)
    b = max(b, i)
    total += i
  return (total - b - s) / (len(nums)-2)

def sum13(nums):
  total = 0
  i = 0
  while i < len(nums):
    if nums[i] == 13:
      i += 2
    else:
      total += nums[i]
      i += 1
  return total

def sum67(nums):
  add = True
  t = 0
  for i in nums:
    if i == 6:
      add = False
    elif not add and i == 7:
      add = True
    elif add:
      t += i
  return t

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False
