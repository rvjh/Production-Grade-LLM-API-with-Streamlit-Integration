














---------------------------------------------------------------------
a = [1,2,3,4,5]
b = ['a','b','c','d','e']
c = dict(zip(a,b))

for i,j in c.items():
  print(f"{i} --> {j}")
----------------------------------------------------------
def f(x):
  l = [0,1]
  if x==1:
    return l[0]
  elif x==2:
    return l
  else:
    a=0
    b = 1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

f(10)
------------------------------------------------------
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))


def per(n,r):
  if n>r:
    return m(n)/m(n-r)

print(com(6,2))
print(per(6,2))
---------------------------------------------------------------
def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)

m(6)
------------------------------------------------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j

m([1,2,3,4,5,6,7,8],13)
------------------------------------------------------------------------
def m(a,b):
  if (len(a)>len(b) or len(a)<len(b)) and (a[::-1] == b[::-1]):
    return "Anagram"
  else:
    return "Not Anagram"

m("listen","silent")
---------------------------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c+ 1
  return d


m("jwnhfhwfoihofhoi2ou87279")
----------------------------------------------------------------------
def m(s):
  return s[::-1]

m("kjwejcooejwcj2u3")
--------------------------------------------------------
my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = set(my_list)

print(type(my_set))
------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[::-4]

print(my_slice) #['Ruby', 20]
-----------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[::3]

print(my_slice) #[10, 30, 'Ruby']
---------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[:-2]

print(my_slice) #[10, 10.5, 20, 30, 'Python']
------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[-4:]

print(my_slice) #[30, 'Python', 'Java', 'Ruby']
--------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[:-4]

print(my_slice) #[10, 10.5, 20]
-----------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[2:]

print(my_slice) #[30, 'Python', 'Java', 'Ruby']
----------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[-4:-1]

print(my_slice)
------------------------------------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(6)
----------------------------------------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a=l[0]
    b=l[1]
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
--------------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[3:6]

print(my_slice)
--------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

element = my_list[-2]

print(element)
------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

element = my_list[2]

print(element)
------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

add = (my_list + [30.01, 30.02, 30.03])*2

print(add)
----------------------------------------------------------
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

my_list.clear()

print(my_list)
--------------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

add = sum(my_list)

print(add)
------------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

large = max(my_list)

print(large)
---------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

small = min(my_list)

print(small)
--------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = sorted(my_list, reverse=True)

print(asc)
------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = sorted(my_list)

print(asc)
-----------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

howmany = my_list.count(20)

print(howmany)
---------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.extend([100, 101, 102])

print(my_list)
-------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.insert(4,77)

print(my_list)
----------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

index = my_list.index(10.5)

print(index)
------------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.remove(30)

print(my_list)
-----------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list. append('C++')

print(my_list)
-------------------------------------------------------
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.pop(5)

print(my_list)
-------------------------------------------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a=0
    b=1
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
---------------------------------------
def m(a,b):
  if len(a) == len(b) and a[::-1] == b[::-1]:
    return "Anagram"
  else:
    return "Not Anagram"

m("listen","silent")


------------------------------------
def m(l, x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j

m([1,2,3,4,5,6,7,8],13)
-----------------------------------
s = "dhcwcvwvh"
s.replace("d","D")
--------------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(6,2))
print(com(6,2))
-----------------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(5)
------------------------------------------
def m(s):
  c = 0
  d = {}
  for i in s:
    d[i] = s.count(i)
    c =  c + 1
  return d

m("jhwchwecjwoid287ur0h3h2")
---------------------------------------------
def m(s):
  return s[::-1] 

m("kjhbcwejonoxiewijjoieu08372") 
----------------------------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(6,2))
print(com(6,2))
------------------------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(6)
-------------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(6)
------------------------------------------------------
s = "rohkjwehfwjk"
s[::2]
---------------------------------------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a = 0
    b = 1
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
--------------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j

m([1,2,3,4,5,6,7,8],13)
---------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jhwehflewnc3inxiocmo3imocn3onn")
----------------------------------
def m(s):
  return s[::-1]

m("iwejfhweoiwmci")
-----------------------------------
l = ['a','b','c']
m = [1,2,4]
d = dict(zip(l,m))
d
------------------------------
a = lambda x:x**2

b = list(map(a,[1,2,3,4,5]))
b

-----------------------------------
def m(n):
  l = [0,1]
  if n==1:
    return 0
  elif n==2:
    return l
  else:
    a=0
    b=1
    for i in range(2,n):
      c = a + b
      a = b
      b = c
      l.append(c)
  return l

m(10)
------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c=c+1
  return d

m("rohsqkqqqoqyc")
---------------------------------
def m(n):
  if n==0 or n==1:
    return 1
  else:
    return n*m(n-1)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)

def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(6,2))
print(com(6,2))
---------------------------
def m(n):
  if n==0 or n==1:
    return 1
  else:
    return n*m(n-1)

m(6)
-------------------------------
def m(s):
  return s[::-1]

m("iwufhrvenom")
-------------------------------------
def fibo(n):
  l = [0,1]
  if n==0:
    return 0
  elif n==1:
    return l
  else:
    a = 0
    b=1
    for i in range(2,n):
      c = a + b
      a = b
      b = c
      l.append(c)
  return l

fibo(10)
---------------------------------------
def f(x):
  if x==0 or x==1:
    return 1
  else:
    return x*f(x-1)

f(4)
-----------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i):
      if l[j] + l[i] ==x:
        return i,j

m([1,2,3,4,5],6)
------------------------------------
a = lambda x, y : x*y

list(map(a,[1,2,3,4,5],[6,7,8,9,10]))
-------------------------------
a = lambda x : x[::-1]
a("slhjvoao quwdp")
-------------------------------
def m(s):
  return s[::-1]

m("slhjvoao quwdp")
----------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("rohsqkqqqoqyc")
------------------------------------
num1 = 5
num2 = 2

num3 = num1 // num2

print(num3 == 5 % 3) #result is True
----------------------------------------
num1 = 10
num2 = 3

num3 = num1 ** num2

print(num3 == 250 * 4) #result is True
----------------------------------------
num1 = 25
num2 = 8

num3 = num1 % num2

print(num3 == 1) #result is True
--------------------------------------------
num1 = 13.67

num2 = int(num1)

print(type(num2))
-----------------------------------------------------
num1 = 25

num2 = float(25)

print(type(num2))
------------------------------------------------------------
def f(x):
  if x == 0 or x==1:
    return 1
  else:
    return x*f(x-1)


def per(n,r):
  if r>n:
    return 0
  else:
    return f(n)/f(n-r)

def com(n,r):
  if r>n:
    return 0
  else:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
-------------------------------------------
def m(a):
  if a == 0 or a==1:
    return 1
  return a*m(a-1)

m(6)
--------------------------------------
def m(x):
  d = {}
  for i in range(1,x+1):
    d[i] = i**2
  return d

a = m(15)
for i,j in a.items():
  if j%2==0:
    print(f"i: {i},j: {j}")
---------------------------------------
a = lambda x:x**2
a(20)
list(map(a,[1,2,3,4,5]))
---------------------------------------
def ts(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j

ts([10,20,10,40,50,60,70],50)
------------------------------------------
def m(l):
  d = {}
  for i in l:
    d[i] = len(i)
  a = max(d.values())
  for i,j in d.items():
    if j == a:
      return i,j

m(["rohan","das","suchitra"])
-------------------------------------
def m(s):
  return s.replace('a','#')

m("rohan")
-----------------------------------------
def m(s):
  c = 0
  d = {}
  for i in s:
    d[i] = s.count(i)
    c += 1
  return d

m("whfowehfwfhpwejhpwpq")

-------------------------------------
def m(a,b):
  if len(a) != len(b):
    return False
  else:
    if a == b[::-1]:
      return True

m("abba","abba")
------------------------------------
def a(s):
  return s[::-1]

a("rohandas")
-------------------------------------------
def f(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n == 1:
    return l
  else:
    a = 0
    b = 1
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

f(10)
------------------------------------------
def f(n):
  if n == 0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(3)
--------------------------------------
def m(s,k):
  for i in s:
    c = s.count(k)
  return c

m("rohandas",'a')
-------------------------
a = lambda x:x**3

a(10)
--------------------------------
def m(x):
  if x == 0 or x ==1:
    return 1
  else:
    return x*m(x-1)

def per(n,r):
  if n<r :
    return 0
  else:
    return m(n)/m(n-r)

def com(n,r):
  if n<r:
    return 0
  else:
    return m(n)/(m(r)*m(n-r))

print("Permutation : ",per(5,3))
print("Combination : ",com(5,3))
------------------------------
def m(a):
  if a==0 or a==1:
    return 1
  else:
    return a*m(a-1)

m(10)
-------------------------------
def m(a,b):
  if len(a) != len(b):
    return False
  else:
    if a == b[::-1]:
      return True
    else:
      return False

m("aba","abc")
--------------------------------
def m(s):
  return s[::-1]

m("rohandas")
----------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("kbvjeeowvoewvr")
----------------------------------
a = [1,2,3]
b = [2,3,4]

c = a + b
c.sort()
c
----------------------------------
def m(a,x):
  l, r = 0, len(a)-1
  while l<r:
    s = a[l] + a[r]
    if s > x:
      r-=1
    elif s<x :
      l += 1
    else:
      return [l, r]

m([1,2,3,4,5],9)

-------------------------------------
def twosum(l,x):
  hasmap = {}   # value : index
  for i, n in enumerate(l):
    diff = x - n
    if diff in hasmap:
      return [hasmap[diff],i]
    hasmap[n] = i
  return 

twosum([1,2,3,4,5],9)
----------------------------------------
def twoSum(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j

twoSum([1,2,3,4,5],9)
---------------------------------------------
def anagram(s,t):
  if len(s) != len(t):
    return False
  else:
    l = list(s)
    m = list(t)
    l.sort()
    m.sort()
    p = 0
    match = True
    while p < len(l) and match:
      if l[p] == m[p]:
        p = p + 1
      else:
        match = False
    return False 

anagram("rohan","nahor")

-----------------------------------------
def palindrome(s,t):
  if len(s) != len(t):
    return False
  else:
    if s == t[::-1]:
      return True
    else:
      return False

palindrome("rohan","nahor")
-----------------------------------------------
## permutation & combination

def f(n):
  if n == 0 or n==1:
    return 1
  else:
    return n*f(n-1)

def p(n,r):
  if n<r:
    return 0
  else:
    return f(n)/f(n-r)

def c(n,r):
  if n<r:
    return 0
  else:
    return f(n)/(f(r)*f(n-r))


print("Permutation : ",p(5,3))
print("Combination : ",c(5,3))
---------------------------------------------
def f(n):
  if n == 0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(5)
-----------------------------------------------------------------
def m(n):
  a = [] ## for returning the list as a input array
  n.sort()   ## sorting the array

  for i, b in enumerate(n):    ## index and value
    if i > 0 and b == n[i-1]:                  ## not first index and a not repeated
      continue
    ## two pointers
    l, r = i+1, len(n)-1
    while l<r:
      threeSum = b + n[l] + n[r]
      if threeSum > 0:
        r -= 1
      elif threeSum <0:
        l += 1
      else:
        a.append([b,n[l],n[r]])
        l += 1
        while l<r and n[l] == n[l-1]:
          l += 1
  return a


m([-1,0,1,2,-1,-4])

--------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("rohandas")
---------------------------------------------------------------------
## 3 sum i.e a + b + c =0 in a array of n integers incluing -ve

def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      for k in range(j+1, len(l)):
        if l[i] + l[j] + l[k] == x:
          return i,j,k

m([-1,0,1,2,-1,-4],0)
------------------------------------------
## two sum

def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j

m([1,2,3,4,5],9)
------------------------------------------
SELECT 
  emp.employee_id AS employee_id,
  emp.name AS employee_name
FROM employee AS mgr
INNER JOIN employee AS emp
  ON mgr.employee_id = emp.manager_id
WHERE emp.salary > mgr.salary;
-------------------------------------------
def m(s):
  return list(filter(lambda x: x.startswith(("A","E","I","O","U")), s))


m(["Aiui","iuwfg","Qreu"])
---------------------------------------------
def m(l):
  return list(filter(lambda x:x<10, l))

m([10,2,5,23,4,3,6])
------------------------------------------------
def m(s):
  return list(filter(lambda x: x.isupper(), s))

m("ROhANdAs")
-----------------------------------------------------
def m(l):
  return list(filter(lambda x: x%2==0,l))


m([1,3,4,5,6,7,8,9])
-----------------------------------------------------------------
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Convert the string into a list of characters
        l = [i for i in s]
        
        # Use a set to remove duplicate characters
        m = set(l)
        
        # Sort the set to get the characters in lexicographical order
        a = sorted(m)
        
        # Join the sorted characters into a single string
        return "".join(a)

-------------------------------------------------------------
WITH ranked_measurements AS (
  SELECT 
    CAST(measurement_time AS DATE) AS measurement_day, 
    measurement_value, 
    ROW_NUMBER() OVER (
      PARTITION BY CAST(measurement_time AS DATE) 
      ORDER BY measurement_time) AS measurement_num 
  FROM measurements
) 

SELECT 
  measurement_day, 
  SUM(measurement_value) FILTER (WHERE measurement_num % 2 != 0) AS odd_sum, 
  SUM(measurement_value) FILTER (WHERE measurement_num % 2 = 0) AS even_sum 
FROM ranked_measurements
GROUP BY measurement_day;
------------------------------------------------------
WITH latest_transactions_cte AS (
  SELECT 
    transaction_date, 
    user_id, 
    product_id, 
    RANK() OVER (
      PARTITION BY user_id 
      ORDER BY transaction_date DESC) AS transaction_rank 
  FROM user_transactions) 
  
SELECT 
  transaction_date, 
  user_id,
  COUNT(product_id) AS purchase_count
FROM latest_transactions_cte
WHERE transaction_rank = 1 
GROUP BY transaction_date, user_id
ORDER BY transaction_date;
----------------------------------------------------------
WITH top_10_cte AS (
  SELECT 
    artists.artist_name,
    DENSE_RANK() OVER (
      ORDER BY COUNT(songs.song_id) DESC) AS artist_rank
  FROM artists
  INNER JOIN songs
    ON artists.artist_id = songs.artist_id
  INNER JOIN global_song_rank AS ranking
    ON songs.song_id = ranking.song_id
  WHERE ranking.rank <= 10
  GROUP BY artists.artist_name
)

SELECT artist_name, artist_rank
FROM top_10_cte
WHERE artist_rank <= 5;
-------------------------------
def m(a,b):
  return list(map(lambda x,y: x+y, a,b)), list(map(lambda x,y: x-y, a,b))

m([1,2,3,4,5],[2,1,2,3,5])
----------------------------------
def m(l):
  return list(map(lambda x: x**2, l))

m([1,2,3,4,5])
----------------------------------
def m(l):
  return list(map(lambda x: x+3, l))

m([1,2,3,4,5])
--------------------------------------
def m(l):
  return list(map(lambda x:x**3, l))

m([1,2,3,4,5])
------------------------------------------
def m(l):
  return list(map(lambda x: True if len(x)==6 else False, l))

m(["rohana","rohandaaas","gagan"])
-------------------------------------------
def m(l):
  a = 0
  b = 0
  for i in l:
    if i%2==0:
      a = a + 1
    else:
      b = b+ 1
  return a,b

m([1,2,3,4,5,6,7,8,9])
-------------------------------------------
def m(n):
  l = [0,1]
  if n == 1:
    return l[0]
  elif n == 2:
    return l
  else:
    a = 0
    b = 1
    for i in range(2,n):
      c = a + b
      a = b
      b = c
      l.append(c)
  return l

m(10)
------------------------------------
def m(s):
  print(lambda s : True if s.startswith("A") else False)

m("Abinash")
---------------------------------------
def m(l):
  return list(map(lambda x : x ** 2, l)), list(map(lambda x:x**3, l))

m([1,2,3,4])
-------------------------------------------
WITH order_counts AS (
  SELECT COUNT(order_id) AS total_orders 
  FROM orders
)

SELECT
  CASE
    WHEN order_id % 2 != 0 AND order_id != total_orders THEN order_id + 1
    WHEN order_id % 2 != 0 AND order_id = total_orders THEN order_id
    ELSE order_id - 1
  END AS corrected_order_id,
  item
FROM orders
CROSS JOIN order_counts
ORDER BY corrected_order_id;
-------------------------------------------------------------
WITH supercloud_cust AS(
SELECT 
  customers.customer_id, 
  COUNT(DISTINCT products.product_category) AS product_count
FROM customer_contracts AS customers
INNER JOIN products 
  ON customers.product_id = products.product_id
GROUP BY customers.customer_id
)

SELECT customer_id
FROM supercloud_cust
WHERE product_count = (
  SELECT COUNT(DISTINCT product_category) FROM products
);
----------------------------------------------
SELECT
  artist_name,
  concert_revenue,
  genre,
  number_of_members,
  concert_revenue / number_of_members AS revenue_per_member,
  RANK() OVER (
    PARTITION BY genre
    ORDER BY concert_revenue / number_of_members DESC) AS ranked_concerts
FROM concerts;
--------------------------------------------------
select user_id,
MAX(post_date:: DATE) - MIN(post_date:: DATE) AS days_between
FROM posts
WHERE DATE_PART('year', post_date::DATE) = 2021
GROUP BY user_id
HAVING COUNT(post_id) > 1;
----------------------------------------------------
select 
emails.user_id
FROM emails JOIN texts
ON emails.email_id = texts.email_id
WHERE texts.action_date = emails.signup_date + INTERVAl '1 day'
AND texts.signup_action = 'Confirmed'
---------------------------------------------------------
SELECT
user_id,
(MAX(post_date :: DATE) -  MIN(post_date :: DATE)) as days_between
FROM posts
WHERE DATE_PART('year', post_date:: DATE) = 2021
GROUP BY user_id
HAVING COUNT(post_id) > 1;
-----------------------------------
SELECT page_id
FROM pages
WHERE page_id NOT IN (
SELECT page_id 
FROM page_likes
WHERE page_id IS NOT NULL
)
--------------------------------------
select 
users.city, COUNT(trades.order_id) AS total_orders
FROM trades join users
ON trades.user_id = users.user_id
WHERE trades.status = 'Completed'
GROUP BY users.city
ORDER BY total_orders DESC
LIMIT 3;
-----------------------------------
SELECT * FROM 
trades JOIN users
ON users.user_id = trades.user_id;
----------------------------------
SELECT
SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views,
SUM(CASE WHEN device_type IN ('tablet', 'phone') THEN 1 ELSE 0 END) AS mobile_views
FROM viewership;
------------------------------------
def m(x):
  x.sort(key = lambda x:x[1])
  print(x)

m([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
----------------------------------
def m(x):
  return sorted(x)

a = lambda x: m(x)

a([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
----------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("rohandas")
------------------------------
def m(x):
  print("Double", x*2)
  print("Triple", x*3)

a = lambda x:m(x)

a(10)
---------------------------------
def m(x,y):
  return x*y

a = lambda x,y:m(x,y)

a(10,5)
----------------------------------
def m(x):
  return x+15

a = lambda x:m(x)

a(10)
---------------------------------
def m(l):
  return list(set(l))

m([1,2,3,3,3,3,4,5])
-------------------------------------
def m(s):
  u = 0
  l = 0
  for i in s:
    if i.isupper():
      u = u +1
    elif i.islower():
      l = l +1
  return u,l

m("The quick Brow Fox")
--------------------------------------
def m(n):
  if (n == 0) or (n==1):
    return 1
  else:
    return n*m(n-1)

m(5)
========================================
def m(s):
  return s[::-1]

m("rohandas")
-----------------------------------------
def m(l):
  return sum(l)

m([1,1,1,1,1])
-----------------------------------------
def m(a,b,c):
  return max(a,b,c)

m(10,20,30)
---------------------------------------------
SELECT
  actor,
  character,
  platform,
  avg_likes,
  CASE 
    WHEN avg_likes >= 15000 THEN 'Super Likes'
    WHEN avg_likes BETWEEN 5000 AND 14999 THEN 'Good Likes'
    ELSE 'Low Likes'
  END AS likes_category
FROM marvel_avengers
ORDER BY avg_likes DESC;
-----------------------------------------------
SELECT part, assembly_step FROM parts_assembly
WHERE finish_date is NULL;
--------------------------------------------------
SELECT  drug, CEIL(total_sales/ units_sold) as unit_cost
FROM pharmacy_sales
WHERE manufacturer = 'Merck'
ORDER BY unit_cost
----------------------------------------------------
SELECT ticker, COUNT(ticker) FROM stock_prices
WHERE ((close - open)/open > 0.1) OR ((close - open)/open < -0.1)
GROUP BY ticker
ORDER BY count DESC;
----------------------------------------------------
SELECT card_name, (MAX(issued_amount) - MIN(issued_amount)) as difference
FROM monthly_cards_issued
GROUP BY card_name
ORDER BY difference DESC;
------------------------------------------------
SELECT drug,(total_sales - cogs)  as total_profit  FROM pharmacy_sales
ORDER BY total_profit DESC LIMIT 3;
-----------------------------------------------
SELECT category, COUNT(DISTINCT product) FROM product_spend
GROUP BY category ;
---------------------------------------------------
SELECT candidate_id FROM candidates
GROUP BY candidate_id
HAVING COUNT(candidate_id) > 2;
-------------------------------------------------------
SELECT ticker, MIN(open) as min FROM stock_prices
GROUP BY ticker
HAVING MIN(open) > 100;
-------------------------------------------------------
SELECT skill, COUNT(candidate_id) as count FROM candidates
GROUP BY skill
ORDER BY count DESC
-----------------------------------------------------
SELECT ticker, MIN(open) as min FROM stock_prices
GROUP BY ticker
ORDER BY min DESC
---------------------------------------------
SELECT MAX(open) FROM stock_prices
WHERE ticker = 'NFLX' ;
-----------------------------------------------
SELECT MIN(open) FROM stock_prices
WHERE ticker = 'MSFT' ;
------------------------------------------------
SELECT AVG(open) FROM stock_prices
WHERE ticker =  'GOOG';
------------------------------------------------------------
SELECT COUNT(*), SUM(total_sales) FROM pharmacy_sales
WHERE manufacturer = 'Pfizer';
--------------------------------------------
SELECT COUNT(*) FROM pharmacy_sales;
--------------------------------------------
def missing_int(input: list[int])-> int:
    input.sort()
    for i in range(len(input)):
      if i != input[i]:
        return i
    return len(input)
-----------------------------------------
def intersection(a, b):
  l = []
  for i in a:
    if i in b:
      l.append(i)
  return l
------------------------------------------
def fizz_buzz_sum(target):
  sum = 0
  for i in range(target):
    if (i % 3 == 0) or (i % 5 == 0):
      sum += i
  return sum
---------------------------------------------
from math import pi
class C:
  def __init__(self, x):
    self.x = x

  def per(self):
    return 2*pi*(self.x)

  def ar(self):
    return pi*(self.x**2)

c = C(5)
print(c.per())
print(c.ar())
-------------------------------------------------------------
from datetime import date

class P:
    def __init__(self, n, c, dob_year):
        self.n = n
        self.c = c
        self.dob = date(dob_year, 1, 1)  # Assuming January 1st as the date of birth

    def ag(self):
        ag = date.today().year - self.dob.year
        return self.n, self.c, ag

# Example usage
p = P("Rohan", "Male", 1999)
print(p.ag())

-----------------------------------------
class C:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def add(self):
    return self.x + self.y
  def sub(self):
    return self.x - self.y
  def mul(self):
    return self.x * self.y
  def div(self):
    return self.x / self.y

c = C(10,51)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j

m([10,2,5,24,6],11)
--------------------------------------
SELECT * FROM customers
WHERE
age BETWEEN 18 and 22
AND state IN ('Victoria', 'Tasmania', 'Queensland')
AND gender != 'n/a'
AND (customer_name LIKE 'A%' OR customer_name LIKE 'B%');
-----------------------------------------
SELECT * FROM customers 
WHERE
customer_name LIKE '_ee%'
LIMIT 20;

-------------------------------------------
SELECT * FROM customers 
WHERE
customer_name LIKE 'F%'
AND
customer_name LIKE '%ck'
LIMIT 20;
---------------------------------------------
SELECT manufacturer,drug, units_sold
FROM pharmacy_sales
WHERE
manufacturer IN ('Roche', 'Bayer', 'AstraZeneca')
AND
units_sold NOT BETWEEN 55000 AND 550000;
----------------------------------------------
SELECT manufacturer, drug, units_sold
FROM pharmacy_sales
WHERE (manufacturer = 'Biogen' OR manufacturer = 'AbbVie' OR manufacturer = 'Eli Lilly')
AND units_sold BETWEEN 100000 AND 105000;

--------------------------------------------
SELECT 
    *
FROM 
    reviews
WHERE
    stars >= 4
    AND review_id < 6000
    AND review_id > 2000
    AND user_id != 142;
-------------------------------------------------
select user_id, stars
from reviews
where reviews.stars = 3;

---------------------------------------------------
select EXTRACT(month from submit_date) as mth, product_id, ROUND(AVG(stars),2) as avg_stars
from reviews
GROUP BY EXTRACT(MONTH FROM submit_date), product_id
ORDER BY EXTRACT(MONTH FROM submit_date) ASC
--------------------------------
def factorial(n):
  if n==0 or n == 1:
    return 1
  else:
    return n*factorial(n-1)
----------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1,len(l)):
      if l[i] + l[j] == x:
        return i, j

m([2,7,11,15],13)
------------------------------------
def m(s):
  d = {}
  c=0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("Rohan das")
-------------------------------------
def m(d):
  return max(d, key=d.get)

m(d)
---------------------------------------
m = ['a', 'b', 'c', 'd', 'e', 'f']
n = [1, 2, 3, 4, 5]

d = dict(zip(m,n))
d
list(d.items())

list(d.keys())

list(d.values())
-----------------------------------
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d = {}
for i in (d1, d2):
  d.update(i)

d
-------------------------------------
def m(x):
  d={}
  for i in range(1,x+1):
    d[i] = i**2
  return d

m(5)
-----------------------------------------------
def m(x,d):
  if x in d:
    return True
  else:
    return False

m(4,{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})
---------------------------------------------
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

d = {}

for i in (dic1, dic2, dic3):
  d.update(i)

d
---------------------------------------------------------
d = {1:10,2:20}
d.update({3:30})
d
-----------------------------------------------------------------------------
select city, country, (population/NULLIF(area, 0)) as density 
from cities_population;
----------------------------------------------------------------------------------
select company, profits from forbes_global_2010_2014 order by profits desc limit 3;
-------------------------------------
import pandas as pd
forbes_global_2010_2014.head()

forbes_global_2010_2014.sort_values(by='profits', ascending=False).head(3)[['company','profits']]
-------------------------------
def m(l,t):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == t:
        return i,j

m([2,7,11,15],17)
--------------------------
a = [1,2,3]
b = ['a','b','c']

c = dict(zip(a,b))
c
----------------------------
def m(l):
  k = 1
  for i in l:
    k *= i
  return k

m([1,2,3,4,5])
------------------------------
def m(l):
  return sum(l)

m([1,2,3,4,5])
-------------------------------
def m():
  a = input("Enter : ")
  b = a.split(",")
  return ",".join(sorted(list(set(b))))

m()
------------------------------
def m():
  a = input("Enter : ")
  print(a.upper())
  print(a.lower())


m()
---------------------------------
## count of occuerences

def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c +1
  return d


m("rohandas")
-----------------------------------
def m(s):
  for i in range(len(s)):
    if i%2==0:
      print(s[i], end="")

m("rohan")
---------------------------------
def m(a, t):
  for i in range(len(a)):
    for j in range(i+1, len(a)):
      if (a[i] + a[j]) == t:
        return i,j

m([10,20,10,40,50,60,70],50)
---------------------------------
def m(s):
  return s[-1] + s[1:-1] + s[0]

m("rohan")
-----------------------------------
def m(a,b):
  return a[:b] + a[b+1:]

m("rohan", 3)

---------------------------------------
def m(l):
  d = {}
  for i in l:
    d[i] = len(i)
  a = max(d.values())
  for i,j in d.items():
    if j == a:
      return i,j

m(["rohan","rohandas","gagan"])
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
