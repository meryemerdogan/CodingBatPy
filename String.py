############################################
############### string-1 ###################
############################################
def hello_name(name):
  return "Hello "+ name + "!"

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  tagStart = "<" + tag + ">"
  tagEnd = "</" + tag + ">"
  
  return tagStart + word + tagEnd

def make_out_word(out, word):
  return out[:2] + word + out[-2:]

def extra_end(str):
  return str[-2:] + str[-2:] + str[-2:]

def first_two(str):
  if len(str) < 3:
    return str
  return str[:2]

def first_half(str):
  half = len(str)/2
  return str[:half]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  if len(a) > len(b):
    return b + a +b
  return a + b + a

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  return str[2:] + str[:2]

############################################
############### string-2 ###################
############################################

def double_char(str):
  str2 = ""
  for i in range(len(str)):
    str2 += (str[i] + str[i])
  return str2

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      count += 1
  return count
    
def cat_dog(str):
  cCount = 0
  dCount = 0
  
  for i in range(len(str)-2):
    if str[i:i+3] == "cat":
      cCount += 1
    if str[i:i+3] == "dog":
      dCount += 1
  return dCount == cCount

def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == "co" and str[i+3] == "e":
      count+=1
      
  return count

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  return a.endswith(b) or  b.endswith(a)

def xyz_there(str):
  a = str.count(".xyz")
  b = str.count("xyz")
  return b-a > 0

