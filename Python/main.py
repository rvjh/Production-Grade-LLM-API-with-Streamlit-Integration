
----------------------------------------
def m(s):
  if len(s)<3:
    return s
  else:
    if s[-3:] == "ing":
      return s+"ly"
    else:
      return s + "ing"

m("ab")
-------------------------------------------
def m(a,b):
  m = b[:2] + a[2:]
  n = a[:2] + b[2:]
  o = m + " " + n
  return o

m("abc","xyz")
----------------------------------------------
def n(s):
  a = s[0]
  l = s.replace(a,"$")
  m = a + l[1:]
  return m

  
n("restart")
------------------------------------------------
def m(s):
  if len(s)<2:
    return s
  else:
    return s[:2]+s[-2:]

m("rohan")

-----------------------------------------------------
def m(s):
  d = {}
  c=0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d 

m("rohandas")
--------------------------------------------------------------------------
def m(s):
  return len(s)

m("rohan")
-----------------------------------------------------------------------------
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}  # Track the 
        seen = set()  # Keep track of characters already in the result
        result = []  # Stack to build the result
        
        for i, char in enumerate(s):
            if char not in seen:
                # Ensure the result is in lexicographical order
                while result and char < result[-1] and i < last_occurrence[result[-1]]:
                    seen.remove(result.pop())
                seen.add(char)
                result.append(char)
        
        return "".join(result)

        
        
        
-----------------------------------------
## Counting Special Characters

def m(s):
  a = re.sub("[\w]+","",s)
  return len(a)

m("!@#$%^&*()")
------------------------------------------
import re
def m(s):
  a = re.sub("[^0-9]","",s)
  b = re.sub("[^a-zA-Z]","",s)
  c = re.findall("[ \n]",s)

  return len(a), len(b), len(c)

m("I love programming")
--------------------------------------
s1 = "abc"
s2 = "abc"
s1 = list(s1)
s2 = list(s2)

if s1 == s2:
  print(True) 
else:
  print(False) 
-----------------------------------------
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
l = []
for i in lst1:
  for j in lst2:
    l.append(i+j)

l
------------------------------------------
lst = ["P", "Y", "T", "H", "O", "N"]

s = ''.join(lst)
s
-------------------------------
l = [1,2,3,4,5,6,7,8]
mid = int(len(l)//2)
l[mid]
------------------------------------
numberList = [15, 85, 35, 89, 125]

min(numberList)
-----------------------------
numberList = [15, 85, 35, 89, 125]

max(numberList)
----------------------------
def m(a):
  l = [0,1]
  if a==0:
    return l[0]
  elif a==1:
    return l
  else:
    m = 0
    n = 1
    for i in range(2,a):
      c = m+n
      m = n
      n = c
      l.append(c)
  return l
  
m(5)
------------------------------------------
def m(s):
  d = dict()
  for i  in s:
    d[i] = s.count(i)
  return d

m("gagan bhatia")
----------------------------------------------
def m(s):
  l = ['a', 'e', 'i', 'o', 'u']
  d = dict()
  for i in s:
    if i not in l:
      d[i] = s.count(i)
  return d

m("programming")
-------------------------------------------
def m(s):
  d = dict()
  for i in s:
    d[i] = s.count(i)
  return d

m("gagan")
-------------------------------------------------
def m(s):
  d = dict()
  for i in "aeiouAEIOU":
    if i in s:
      d[i] = s.count(i)

  return d

m("Gagan")

-------------------------------------------------------
def ab(s):
  return s[::-1]

ab("Gagan")
----------------------------------------------------------
def f(a):
  l = [0,1]
  if a==0:
    return l[0]
  elif a==1:
    return l
  else:
    m = 0
    n = 1
    for i in range(2,a):
      c = m+n
      m = n
      n = c
      l.append(c)
    return l


f(5)
      
------------------------------------------------------------
def f(a):
  if (a==0) or (a==1):
    return 1
  else:
    return f(a-1)+f(a-2)

f(5)
-----------------------------------------------------------------
def s(l, m):
  k = 0
  for i in l:
    if i == m:
      k = k+1
  return k

s("rohandas","d")
------------------------------------------------------------------
def s(l, m):
  k = 0
  for i in l:
    if i == m:
      k = k+1
  return k

s("rohandas","d")
---------------------------------------------------------------------
from itertools import combinations_with_replacement

string = input("Enter the string: ")
r = int(input("Enter the size of combinations: "))

# Generate and print the combinations
combinations = combinations_with_replacement(sorted(string), r)
for combo in combinations:
    print(''.join(combo))


-----------------------------------------------------------------------
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = product(a, b)
print(" ".join(f"({x}, {y})" for x, y in result))


------------------------------------------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for _ in range(n):
    try:
        a, b = map(int, input().split())
        if b == 0:
            print("Error Code: integer division or modulo by zero")
        else:
            print(a//b)
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(input()))
        
    

-------------------------------------------------------------------------

def print_formatted(number):
    # your code goes here
    
    for i in range(1, number+1):
        decimal = i
        octal = format(i,'o')
        hexa = format(i,'X')
        binary = format(i,'b')
        
        print(f"{decimal}  {octal}  {hexa}  {binary}")
        
        
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
---------------------------------------------------------
import numpy

numpy.set_printoptions(legacy='1.13')

my_arr = list(map(float, input().split()))

print(numpy.floor(my_arr))

print(numpy.ceil(my_arr))

print(numpy.rint(my_arr))

# print(my_arr)
----------------------------------------------
import numpy

# Input the dimensions n and m
n, m = map(int, input().split())

# Input array A
A = numpy.array([list(map(int, input().split())) for _ in range(n)])

# Input array B
B = numpy.array([list(map(int, input().split())) for _ in range(n)])

# Perform the operations
print(A + B)       # Addition
print(A - B)       # Subtraction
print(A * B)       # Multiplication
print(A // B)      # Integer Division
print(A % B)       # Modulus
print(A ** B)      # Power
----------------------------------------------------

import numpy
numpy.set_printoptions(legacy='1.13')

a, b = map(int, input().split())

if a != b : 
    pass
else:
    c = numpy.identity((a))
    print(c)






---------------------------------------------------
import numpy

n, m, p = map(int, input().split())

a = numpy.zeros((n,m,p), dtype = int)
b = numpy.ones((n,m,p), dtype = int)

# c = numpy.concatenate((a, b))

print(a)
print(b)

# print(numpy.ones((n,m)), dtype = numpy.int)



-----------------------------------------------------
import numpy as np

n, m, p = map(int, input().split())

# Create empty lists to store the input arrays
arr1 = []
arr2 = []

# Read the first array
for _ in range(n):
    row = list(map(int, input().split()))
    arr1.append(row)

# Read the second array
for _ in range(p):
    row = list(map(int, input().split()))
    arr2.append(row)

# Convert lists to NumPy arrays
arr1 = np.array(arr1)
arr2 = np.array(arr2)

# Concatenate the arrays
concatenated_arr = np.concatenate((arr1, arr2), axis=0)

# Print the concatenated array
print(concatenated_arr)
---------------------------------------------------------
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # Split the string into k-sized chunks
        chunk = string[i:i + k]
        unique_chunk = ""
        for char in chunk:
            if char not in unique_chunk:
                unique_chunk += char
        print(unique_chunk)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


#-----------------------------------------------------------
## C

import math
class Cir():
  def __init__(self,r):
    self.r = r
  
  def per(self):
    return 2*(math.pi)*(self.r)

  def area(self):
    return (math.pi)*(self.r**2)

#------------------------------------------------------------

from datetime import date
class P():
  def __init__(self, name, country, dob):
    self.name = name
    self.county = country
    self.dob = dob

  def age(self):
    a = date.today().year - self.dob
    return a


p = P("Akash","ind",1965)
p.age()

#-------------------------------------------------------------

class D():
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def add(self):
    return self.a + self.b
  def sub(self):
    return self.a - self.b
  def mul(self):
    return self.a * self.b
  def div(self):
    return self.a / self.b

d = D(4,6)
print(d.add())
print(d.sub())
print(d.mul())
print(d.div())

--------------------------------------------

import numpy


n, m = map(int, input().split())

# Create an empty list to store the input array
arr = []

# Read the input array
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# Convert the list to a NumPy array
arr = numpy.array(arr)

# Transpose the array
transpose_arr = arr.T

# Flatten the array
flatten_arr = arr.flatten()

# Print the transpose array
print(transpose_arr)

# Print the flatten array
print(flatten_arr)

-------------------------------------
