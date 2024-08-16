
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
