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
