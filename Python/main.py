








-------------------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3],[2,3,4]))

------------------------
def m(a,b):
  t = a
  a = b
  b = t
  return a,b

m(10,20)
-----------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "yes"
  else:
    return "no"

m("baab","baab")

------------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a, b = 0, 1
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
--------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(6)
-----------------------------
def m(a,b):
  d = {}
  for i in a:
    d[i]=True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
-----------------------------
def m(s):
  c = 0
  d = {}
  for i in s:
    d[i]=s.count(i)
    c = c + 1
  return d

m("mncwjceowcnenocow")
------------------------
def m(s):
  return s[::-1]

m("dmndckjwncn")
---------------------------------
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)
----------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3],[2,3,4]))

------------------------------
a = lambda x : x**2

a(10)
-----------------------------------
a = [1,2,3]
b = [3,4,5]

c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)
-----------------------------
a = [1,2,3]
b = ['a','b','c']

c = dict(zip(a,b))
c
---------------------------
def m(a,b):
  t = a
  a = b
  b = t
  return a,b

m(10,20)
-------------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a , b = 0, 1
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
---------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
-----------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(6)
---------------------------------
def m(s):
  c = 0
  d = {}
  for i in s:
    d[i]=s.count(i)
    c = c + 1
  return d

m("lkascskncwcmpwqcmcj")
-----------------------------
def m(s):
  return s[::-1]

m("jnconwomcciwowe")
------------------------------
def m(a,b):
  d = {}
  for i in a:
    d[i]=True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
----------------------------------
def m(n):
  if n==0 or n==1:
    return 1
  else:
    return n*m(n-1)

m(6)

---------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+ l[j] ==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
------------------------------------
a = [1,2,3]
b = [3,4,5]

c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)
-------------------------
a = [1,2]
b = ['a','b']

c = dict(zip(a,b))
print(c)

c.update({'c':4})
c
----------------------
a = lambda x : x[::-1]

a("qskjcbkwncnw")
--------------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3],[2,3,4]))
-----------------------------
def m(a,b):
  t = a
  a = b
  b = t
  return a,b

m(10,20)
-------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a, b = 0, 1
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
----------------------------
def m(s):
  c = 0
  d = {}
  for i in s:
    d[i]=s.count(i)
    c = c + 1
  return d

m("kjbcwj2exownqnc")
------------------------
def m(s):
  return s[::-1]

m("wdkjcbkjwnc")
-----------------------------
def m(a,b):
  d = {}
  for i in a:
    d[i]=True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
----------------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3],[2,3,4]))
--------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a, b = 0, 1
    for i in range(2,n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4],6)
------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(6)
-------------------------------
def m(s):
  c = 0
  d = {}
  for i in s:
    d[i]=s.count(i)
    c = c + 1
  return d

m("jdnconononcowiqo")
------------------------
def m(s):
  return s[::-1]

m("jksncnwncw")
---------------------------
def m(a):
  return a**2

list(map(m,[1,2,3]))
-----------------------
def m(a,b):
  t = a
  a = b
  b = t
  return a,b

m(10,20)
-------------------------
a = lambda x: x**2

a(10)
-----------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
---------------------------
def m(a,b):
  d = {}
  for i in a:
    d[i]=True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
--------------------------
c.update({4:'d'})
c
-----------------------------
a = [1,2,3]
b = ['a','b','c']

c = dict(zip(a,b))
c
-------------------------------
a = [1,2,3]
b = [2, 3,4]

c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)
----------------------
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
-------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(3)
----------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i]=s.count(i)
    c = c + 1
  return d

m("qkncjnwomew")
-------------------------
def m(s):
  return s[::-1]

m("lkancwnocw")
-------------------------------
a = lambda x : x[::-1]

a("wjkdncjwnojcn")
-------------------------
def m(a,b):
  d = {}
  for i in a:
    d[i]=True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
-----------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
---------------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3],[2,3,4]))
----------------------------------------
def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)


def per(n,r):
  if n>r:
    return m(n)/m(n-r)

def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))
---------------------------------------
def m(x):
  l = [0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a = 0
    b = 1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
-------------------------------
def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)

m(4)
------------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i]=s.count(i)
    c = c + 1
  return d

m("kjcwncnnonqxw")
------------------------------
def m(s):
  return s[::-1]

m("jncnwonmiowec")
-------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
--------------------------------
def m(a,b):
  d = {}
  for i in a:
    d[i]=True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
-------------------------------------
a = [1,2,3]
b = [3,4,5]

c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)
----------------------------
a = np.zeros((2,3))
a
---------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3],[2,3,4]))
------------------------------
a = lambda x: x**2

a(10)
---------------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif l==1:
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
---------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
---------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)
  
f(6)
----------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jwdncijnwincowneno")
----------------------------------
def m(s):
  return s[::-1]

m("kcojwncoiem")
-------------------------------------
a = [1,2,3]
b = [3,4,5]

dict(zip(a,b))
----------------------------------------
a = [1,2,3]
b = [3,4,5]

c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)
------------------------------------
a = lambda x: x**2

list(map(a,[1,2,3]))
-------------------------------------
def m(a,b):
  return a*b

list(map(m,[1,2],[3,4]))
---------------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
---------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(4)
------------------------------
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
-------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("skncwnocmmxeniw")
----------------------------
def m(s):
  return s[::-1]

m("klkncjdwnnc")
-----------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
------------------------------
def m(a,b):
  d = {}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
m([1,2,3],[3,4,5])
-----------------------------------
a = lambda x : x[::-1]

a("wijhcwhoc")
-------------------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3],[2,3,4]))
-------------------------------------------
a = [1,2,3]
b = [3,4,5,6]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)
----------------------------
a = [1,2,3]
b = ['a','b','c']
c = dict(zip(a,b))
c
---------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(4)
-----------------------------
def f(n):
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

f(10)
-----------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i]=s.count(i)
    c=c+1
  return d

m("dkljnvcwonocwemcimwoj")

-----------------------------------
def m(s):
  return s[::-1]

m("dncjnwowqclqnc")
------------------------------------
a = [1,2,3,4]
b = [2,4,5,6,7]

c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)
-----------------------------
a = [1,2,3,4,5]
b = ['a','b','c','d','e']

d = dict(zip(a,b))
d
---------------------------------
def m(a,b):
  return a*b

list(map(m,[1,2,3,4,5],[2,4,6,8,10]))
---------------------------------
a =  lambda x: x**2

a(10)
------------------------------------
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
------------------------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
--------------------------------------
def m(l, x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4],7)
-----------------------------------
def m(l2, l3):
  f = {}
  for i in l2:
    f[i] = True
  for j in l3:
    if j in f:
      return j
  return None

m([1,2,3],[3,4,5])
--------------------------------------
def d(n):
  if n==0 or n==1:
    return 1
  else:
    return n*d(n-1)

d(10)
---------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jknclwxniwxmmxqnxce")
-----------------------------
def m(s):
  return s[::-1]

m("dmndlwencecm")
-------------------------
s = "kljcnkwjkconc jwnconwo"
s[::2]
-------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
----------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "True"
  else:
    return "False"

m("racecar","racecar")
-----------------------------
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
----------------------------
def m(a):
  if a==0 or a==1:
    return 1
  else:
    return a*m(a-1)

m(3)
----------------------------
list(map(a,[1,2,3]))
-----------------------------
a = lambda x:x**2

a(10)
-------------------------------
def m(l1, l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
--------------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jknclwxniwxmmxqnxce")
-----------------------------------
def m(s):
  return s[::-1]

m("wenconepmpwe")
-----------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
---------------------------------------
l1 = [1,2,3,4,5]
l2 = [4,5,6,7]

c = set(l1).union(set(l2))
d = set(l1).intersection(set(l2))
e = c - d

print(c)
print(d)
print(e)
-------------------------------------------------
def f(n):
  l=[0,1]
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

f(10)
----------------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(10,5))
print(com(10,5))
--------------------------------
a = lambda a:a**2

list(map(a,[1,2,3]))
------------------------------------
a = lambda x,y : x+y

a(1,2)
---------------------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "True"
  else:
    return "False"

m("racecar","racecar")
-----------------------------
def m(a):
  return a**2

list(map(m,[1,2,3,4,5]))
----------------------------
a = [1,2,3,4]
b = ['a','b','c','d']

d = dict(zip(a,b))
print(d)

d.update({5:'e'})
d
-----------------------------
def m(l1, l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,2,3],[3,4,5])
------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(4)
--------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("wljcohwejimx2ijxqjpix")  
--------------------------------
def m(s):
  return s[::-1]

m("jcwocwoocnenc")
-----------------------------------
l1 = [1,2,3,4,5]
l2 = [2,4,6,8]

a = set(l1).union(set(l2))
b = set(l1).intersection(set(l2))
c = a - b

print(a)
print(b)
print(c)
------------------------
def m(l1,l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,3,5],[2,4,5])
---------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
----------------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "True"
  else:
    return "False"

m("racecar","racecar")
--------------------------------
def f(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a = 0
    b = 1
    for i in range(2,n):
      c =  a + b
      l.append(c)
      a = b
      b = c
  return l

f(10)
------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
----------------------
def m(a):
  return a**2

list(map(m,[1,2,3,4,5]))
-------------------------
def f(x):
  if x==0 or x==1:
    return 1
  else:
    return x*f(x-1)

f(5)
----------------------------
from functools import reduce

a = reduce(lambda x,y : x+y,[1,2,3,4,5])
a
----------------------------
a = lambda x: x[::2]

a("ksacnjkwnj")
---------------------------
a = [1,2,3,4]
b = ['a','b','c','d']

d = dict(zip(a,b))
print(d)
-------------------------------
d = {1:'a',2:'b'}

d.update({3:'c'})

print(d)
-------------------------------
def m(s):
  return s[::-1]

m("jwbcjbowencon")
-----------------------------
def m(a):
  return a**2

list(map(m,[1,2,3,4,5]))
----------------------------
a = lambda x: x[::-1]

a("whflwhoc")
----------------------------
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
------------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
----------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "True"
  else:
    return "False"

m("racecar","racecar")
-----------------------------------------
def m(l1,l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,3,5],[2,4,5])
-------------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(10,5))
print(com(10,5))
--------------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(4)
-----------------------------------------
def m(s):
  d={}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("kjwbck3ic3nxim")
-----------------------------------
def m(s):
  return s[::-1]

m("jkenveo")
---------------------------------------------------
def swap(my_list, index1, index2):
  temp = my_list[index1]
  my_list[index1] = my_list[index2]
  my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
  swap_index = pivot_index
  for i in range(pivot_index+1, end_index+1):
    if my_list[i]<my_list[pivot_index]:
      swap_index += 1
      swap(my_list, swap_index, i)
  swap(my_list, pivot_index, swap_index)
  return swap_index

def quick_sort_helper(my_list, left, right):
  if left < right:
    pivot_index = pivot(my_list, left, right)
    quick_sort_helper(my_list, left, pivot_index-1)
    quick_sort_helper(my_list, pivot_index+1, right)
  return my_list

def quick_sort(my_list):
  return quick_sort_helper(my_list, 0, len(my_list)-1)  

my_list = [4,6,1,7,3,2,5]
print(pivot(my_list, 0, 6))
print(my_list)
print(quick_sort(my_list))



-----------------------------------------
def swap(my_list, index1, index2):
  temp = my_list[index1]
  my_list[index1] = my_list[index2]
  my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
  swap_index = pivot_index
  for i in range(pivot_index+1, end_index+1):
    if my_list[i]<my_list[pivot_index]:
      swap_index += 1
      swap(my_list, swap_index, i)
  swap(my_list, pivot_index, swap_index)
  return swap_index

my_list = [4,6,1,7,3,2,5]
print(pivot(my_list, 0, 6))
print(my_list)


--------------------------------------------------
def merge(l1,l2):
  combined = []
  i,j = 0,0
  while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
      combined.append(l1[i])
      i = i + 1
    else:
      combined.append(l2[j])
      j = j + 1
  while i<len(l1):
    combined.append(l1[i])
    i = i + 1
  while j < len(l2):
    combined.append(l2[j])
    j = j + 1
  return combined


def merge_sort(l):
  if len(l) == 1:
    return l
  else:
    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    return merge(merge_sort(left),merge_sort(right))

oiginal_list = [3,1,5,7,2,4,6,8]
print(f"Original list : {oiginal_list}")
print("Sorted list : ",merge_sort(oiginal_list))
-------------------------------
def merge(l1,l2):
  combined = []
  i,j = 0,0
  while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
      combined.append(l1[i])
      i = i + 1
    else:
      combined.append(l2[j])
      j = j + 1
  while i<len(l1):
    combined.append(l1[i])
    i = i + 1
  while j < len(l2):
    combined.append(l2[j])
    j = j + 1
  return combined

merge([1,3,5,7],[2,4,6,8])

-------------------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j
  return None

m([1,2,3,4,5,6,7],13)
---------------------------------------
def m(n):
  l = [0,1]
  if n == 0:
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
-------------------------------
list(map(f,[1,2,3,4,5,6]))

---------------------------------
a = lambda x: x[::-1]

a("whflwhoc")
----------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(5)
--------------------------------------
def m(l1,l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,3,5],[2,4,5])
-------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("kjbckjwbibbcwebcibecbw")
------------------------------
def m(s):
  return s[::-1]

m("whjbeco")
-----------------------------
def m(a):
  return a**2

list(map(m,[1,2,3,4,5]))
--------------------------------
a = lambda x: x**2

a(10)
---------------------------------
def m(l, x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return [i,j]
  return None

m([1,2,3,4,5], 7)
--------------------------------
def m(l1,l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,3,5],[2,4,5])
---------------------------------
def m(n):
  if n==0 or n==1:
    return 1
  else:
    return n*m(n-1)

m(4)
---------------------------------
def m(n):
  l = [0,1]
  if n==0:
    return l[0]
  elif n==1:
    return l
  else:
    a = 0
    b = 1
    for i in range(2, n):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
---------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jnwcje2hcoh2nxjxwmx")
--------------------------------
def m(s):
  return s[::-1]

m("jwnclw")
----------------------------------------------
## graph

class Graph:
  def __init__(self):
    self.adj_list = {}

  def print_graph(self):
    for vertex in self.adj_list:
      print(vertex, ':', self.adj_list[vertex])

  def add_vertex(self, vertex):
    if vertex not in self.adj_list.keys():
      self.adj_list[vertex] = []
      return True
    return False

  def add_edge(self,v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
      self.adj_list[v1].append(v2)
      self.adj_list[v2].append(v1)
      return True
    return False

  def remove_edge(self,v1,v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
      try:
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)
      except ValueError:
        pass
      return True
    return False

  def remove_vertex(self,vertex):
    if vertex in self.adj_list.keys():
      for other_vertex in self.adj_list[vertex]:
        self.adj_list[other_vertex].remove(vertex)
      del self.adj_list[vertex]
      return True
    return False

g1 = Graph()
g1.add_vertex('A')
g1.add_vertex('B')
g1.add_vertex('C')
g1.add_vertex('D')
g1.add_vertex('E')
g1.add_vertex('F')
g1.print_graph()
g1.add_edge('A','B')
g1.add_edge('A','C')
g1.add_edge('B','D')
g1.add_edge('C','E')
g1.add_edge('D','E')
g1.add_edge('D','F')
g1.print_graph()
g1.remove_edge('D','F')
g1.print_graph()
g1.remove_vertex('D')
g1.print_graph()
------------------------------------------
l1 = [1,2,3]
l2 = ['a','b','c']

dict(zip(l1,l2))
-----------------------------------------------------
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

-------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(5,2))
print(com(5,2))
---------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(4)
-------------------------------------
def m(l1, l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,3,5],[2,4,5])
------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jnwcje2hcoh2nxjxwmx")

-----------------------------------------
def m(s):
  return s[::-1]

m("whflwhoc")
-----------------------------------------
def m(l1,l2):
  d = {}
  for i in l1:
    d[i] = True
  for j in l2:
    if j in d:
      return j
  return None

m([1,3,5],[2,4,5])
-----------------------------------------------
## item in common
# [1,3,5]
# [2,4,5]

def item_in_commom(l1, l2):
  my_dict = {}
  for i in l1:
    my_dict[i] = True
  for j in l2:
    if j in my_dict:
      return j
  return None

item_in_commom([1,3,5], [2,4,5])
---------------------------------------------------------
## class hashtable

class HashTable:
  def __init__(self, size=7):
    self.data_map = [None]*size

  def _hash(self,key):
    my_hash = 0
    for letter in key:
      my_hash = (my_hash + ord(letter)*23)%len(self.data_map)
    return my_hash

  def print_table(self):
    for i, val in enumerate(self.data_map):
      print(f"{i} -> {val}")

  def set_item(self, key, value):
    index = self._hash(key)
    if self.data_map[index] == None:
      self.data_map[index] = []
    self.data_map[index].append([key, value])
  
  def get_item(self, key):
    index = self._hash(key)
    if self.data_map[index] is not None:
      for i in range(len(self.data_map[index])):
        if self.data_map[index][i][0] == key:
          return self.data_map[index][i][1]
    return None
  
  def keys(self):
    all_keys = []
    for i in range(len(self.data_map)):
      if self.data_map[i] is not None:
        for j in range(len(self.data_map[i])):
          all_keys.append(self.data_map[i][j][0])
    return all_keys


h1 = HashTable()
h1.set_item('bolts',1400)
h1.set_item('washers',50)
h1.set_item('lumber',70)
h1.print_table()
h1.get_item('bolts')
h1.keys()

---------------------------------------------
## class hashtable

class HashTable:
  def __init__(self, size=7):
    self.data_map = [None]*size

  def _hash(self,key):
    my_hash = 0
    for letter in key:
      my_hash = (my_hash + ord(letter)*23)%len(self.data_map)
    return my_hash

  def print_table(self):
    for i, val in enumerate(self.data_map):
      print(f"{i} -> {val}")

h1 = HashTable()
h1.print_table()
----------------------------------------------------------------------
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id','age'])
    return df
-----------------------------------------------------
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_animals = animals[animals['weight'] > 100]
    sorted_animals = filtered_animals.sort_values(by='weight', ascending=False)
    names = sorted_animals[['name']]
    return names
    
---------------------------------------------------------
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df = report.melt(
        id_vars = ['product'],
        value_vars = ['quarter_1','quarter_2','quarter_3','quarter_4'],
        var_name = 'quarter',
        value_name = 'sales'
    )
    return df
    
--------------------------------------------------
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
# Reset the index if you want to have 'month' as a regular column
    ans = weather.pivot(index='month', columns='city',values='temperature')
    return ans
------------------------------------------------
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True)
    
------------------------------------------------
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products
    
---------------------------------------
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
    
--------------------------------------------------------
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    dict={
        'id':'student_id',
        'first':'first_name',
        'last':'last_name',
        'age':'age_in_years'}
    return students.rename(columns=dict)
    
-----------------------------------------
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    return employees
    
--------------------------------------------
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna()
    return students
-----------------------------------------
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset='email', keep='first')
    return customers
    
-------------------------------------------
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees
------------------------------
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    a = students[students['student_id'] == 101][['name','age']]
    return a
    
-----------------------------
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    
---------------------------
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id','age'])
    return df
-------------------------------------------
## Queue

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self,value):
    new_node = Node(value)
    self.first = new_node
    self.last = new_node
    self.length = 1

  def print_queue(self):
    temp = self.first
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def en_queue(self,value):
    if self.length == 0:
      return None
    else:
      new_node = Node(value)
      self.last.next = new_node
      self.last = new_node
      self.length += 1
      return True

  def de_queue(self):
    if self.length == 0:
      return None
    else:
      temp = self.first
      self.first = self.first.next
      temp.next = None
      self.length -= 1
      if self.length == 0:
        self.last = None
      return temp.value


q1 = Queue(1)
q1.en_queue(2)
q1.en_queue(3)
q1.en_queue(4)
q1.en_queue(5)
q1.en_queue(6)
q1.en_queue(7)
q1.en_queue(8)
q1.en_queue(9)
q1.en_queue(10)

q1.print_queue()

-------------------------------
# Stack implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push_stack(self, value):
      if self.height == 0:
        return None
      else:
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop_stack(self):
      if self.height == 0:
        return None
      else:
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value


# Create a stack and push values
s1 = Stack(1)
s1.push_stack(2)
s1.push_stack(3)
s1.push_stack(4)
s1.push_stack(5)
s1.push_stack(6)
s1.push_stack(7)
s1.push_stack(8)
s1.push_stack(9)
s1.push_stack(10)

# Print all the items in the stack
s1.print_stack()

s1.pop_stack()
s1.pop_stack()

s1.print_stack()
--------------------------------------
x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

if x.count(115) >= 1 or x.index(115) == 0:
    print("True!")
else:
    print("False!")
-----------------------------------
x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]


if max(x[:2]) <= min(x[3:5]):
    print("True!")
else:
    print("False!")
--------------------------------------
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][2].endswith('h') or x[7][1].endswith('h'):
    print("True!")
else:
    print("False!")
    
    
---------------------------------
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print("True!")
else:
    print("False!")
-------------------------------
if len(x) >= 8 and type(x[6]) is float:
    print("True!")
else:
    print("False!")
---------------------------------
m = lambda x:x.upper()
m('hjdhwjkw')
---------------------------------
a = lambda x,y: x*y

a(4,5)
----------------------------------
def m(a):
  return a**2

list(map(m,[1,2,3]))
--------------------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "Anagram"
  else:
    return "Not Anagram"

m("rohan","nahor")
--------------------------------------
def f(n):
  l = [0,1]
  if n == 0:
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
--------------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(n-r)*f(r))

print(per(5,2))
print(com(5,2))
------------------------------------
def f(x):
  if x==0 or x==1:
    return 1
  else:
    return x*f(x-1)

f(4)
-------------------------------
def m(s):
  return s[::2]

m("kabckwck")
-----------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jnwcje2hcoh2nxjxwmx")
---------------------------------------------------------
def m(s):
  return s[::-1]

m("jnwcje2hcoh2nxjxwmx")
----------------------------------------------------------
## Doubly Linked List


class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self,value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
  
  def print_doubly_ll(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self,value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length = self.length + 1
    return True

  def pop(self):
    if self.length == 0:
      return None
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      temp.prev = None
    self.length = self.length - 1
    return temp

  def prepend(self, value):
    if self.length == 0:
      return None
    new_node = Node(value)
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
    self.length = self.length + 1
    return True

  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      temp.next = None
    self.length = self.length -1
    return temp
  
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    if index < self.length/2:
      for _ in range(index):
        temp = temp.next
    else:
      temp = self.tail
      for _ in range(self.length - 1, index, -1):
        temp = temp.prev
    return temp

  def set_value(self, index, value):
    if index < 0 or index >= self.length:
      return None
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return None
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    before = self.get(index - 1)
    after = before.next
    new_node.prev = before
    new_node.next = after
    before.next = new_node
    after.prev = new_node
    self.length = self.length + 1
    return True

  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length -1:
      return self.pop()
    temp = self.get(index)
    temp.next.prev = temp.prev
    temp.prev.next = temp.next
    temp.next = None
    temp.prev = None
    self.length = self.length - 1
    return temp

    

l2 = DoublyLinkedList(1)
l2.append(2)
l2.append(3)
l2.append(4)
l2.append(5)
l2.print_doubly_ll()
l2.pop()
l2.print_doubly_ll()
l2.prepend(0)
l2.print_doubly_ll()
l2.pop_first()
l2.print_doubly_ll()
l2.get(2).value
l2.set_value(2,9)
l2.print_doubly_ll()
l2.insert(2,8)
l2.print_doubly_ll()
l2.remove(2)
l2.print_doubly_ll()
-------------------------------------
x = "The days of Python 2 are almost over. Python 3 is the king now."

if x[-3:].isdigit():
    print("True!")
else:
    print("False!")
----------------------------------------
x = "The days of Python 2 are almost over. Python 3 is the king now."

if x.index('f') < 10:
    print('True!')
else:
    print('False!')

-------------------------------------------
x = "The days of Python 2 are almost over. Python 3 is the king now."

if 'z' in x or x.count('y')>=2:
    print("True!")

--------------------------
x = "The days of Python 2 are almost over. Python 3 is the king now."

if x[0] == 'T':
    print("True!")
----------------------------
x = "The days of Python 2 are almost over. Python 3 is the king now."

if len(x) >= 50:
    print("True!")
-------------------------------
a = [1,2,3,4]
b = ['m','n','o','p']

dict(zip(a,b))
-----------------------------------
def m(a):
  return a**2

list(map(m, [10,20,30]))
-------------------------------------
a = lambda x: x.upper()

a("rohan")
-----------------------------------------
def m(x):
  l = [0,1]
  if x==0:
    return l[0]
  elif x==1:
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

m(10)
----------------------------------------------------
def f(x):
  if x==0 or x==1:
    return 1
  else:
    return x*f(x-1)

f(4)
----------------------------------------------
def m(l,x):
  if len(l)!=0:
    for i in range(len(l)):
      for j in range(i+1, len(l)):
        if l[i] + l[j] == x:
          return i,j

m([1,2,3,4,5],9)
-----------------------------------------------
def m(s):
  d={}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("rlwejflohan")
--------------------------------------------
def m(s):
  return s[::-1]


m("rohan")
----------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get_index(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp  # Return the node itself instead of just its value

    def set_value(self, index, value):
        temp = self.get_index(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get_index(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove_item(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get_index(index - 1)  # Use get_index to retrieve the previous node
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    def reverse_list(self):
      if self.length == 0:
        return None
      temp = self.head
      self.head = self.tail
      self.tail = temp
      after = temp.next
      before = None
      for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after
      return True



# Test the LinkedList
l1 = LinkedList(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append('rohan')
l1.append('das')
l1.prepend(0)
l1.print_list()
print("After pop:")
l1.pop()
l1.print_list()
print("After prepend:")
l1.prepend(9)
l1.print_list()
print("After pop_first:")
l1.pop_first()
l1.print_list()
print(f"Get index 3: {l1.get_index(3).value}")  # Use .value to get the value of the node
l1.set_value(3, 'uttam')
print("After set_value at index 3:")
l1.print_list()
l1.insert(3, 'suchitra')
print("After insert at index 3:")
l1.print_list()
l1.remove_item(5)
print("After remove_item at index 5:")
l1.print_list()
print("After reverse_list:")
l1.reverse_list()
l1.print_list()
---------------------------------
value = '0xa'

conv = int(value,16)

print(conv)
-----------------------------
value = '0b1010'

conv = int(value,2)

print(conv)
-------------------------------
value = 10

conv = hex(value)

print(conv)
------------------------------
value = 10

conv = bin(value)

print(conv)
-----------------------------------
value = (10, 20, 40, 10, 25, 30, 45)

conv = frozenset(value)

print(type(conv))
---------------------------------
value = [1, 2, 3, 10, 20, 30]

conv = tuple(value)

print(type(conv))
-----------------------------------
value = "Hello!"

conv = list(value)

print(type(conv))
--------------------------------
value = 10

conv = float(value)

print(type(conv))
----------------------------------
value = "10"

conv = int(value)

print(type(conv))
-----------------------------------
value = 10

conv = str(value)

print(type(conv))
----------------------------------------------------------
def f(x):
  l = [0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a=0
    b=1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

f(10)
------------------------------------
def m(a,b):
  return a+b

list(map(m,[1,2,3,4,5],[6,7,8,9,10]))
--------------------------------------

a = lambda x:x**2

a(10)
-----------------------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "Anagram"
  else:
    return "Not Anagram"

m("listen","silent")  
-----------------------------------
def per(n,r):
  if n>r:
    return f(n)/f(n-r)

def com(n,r):
  if n>r:
    return f(n)/(f(r)*f(n-r))

print(per(6,2))
print(com(6,2))
-------------------------------------
def f(x):
  if x==0 or x==1:
    return 1
  else:
    return x*f(x-1)
  
f(4)
----------------------------------
def f(x):
  if x==0 or x==1:
    return 1
  else:
    return x*f(x-1)
  
f(4)
--------------------------------------------
def m(l,x):
  if len(l)!= 0:
    for i in range(len(l)):
      for j in range(i+1, len(l)):
        if l[i] + l[j] == x:
          return i,j

m([1,2,3,4,5,6,7,8],14)
----------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jkwhfiohcnqocohconecn")
--------------------------------
def m(s):
  return s[::-1]

m("kjwckhcu2hw  jclc")
--------------------------------
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
      a=b
      b=c
  return l

m(10)
--------------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i]+l[j]==x:
        return i,j

m([1,2,3,4,5,6,7,8],13)
-------------------------------
def m(a,b):
  if len(a)==len(b) and a[::-1]==b[::-1]:
    return "Anagram"
  else:
    return "Not Anagram"

m("rohan","nahor")
--------------------------------------
def f(n):
  if n==0 or n==1:
    return 1
  else:
    return n*f(n-1)

f(4)
----------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("iuhweihu298u02cmnon2no")
------------------------
def m(s):
  return s[::-1]

m("we2hou8320")
------------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.popitem()

print(len(crypto))
-----------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

keys = crypto.keys()

print(list(keys))
-------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

key = min(crypto)

print(key)
-----------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

val = crypto.values()

print(list(val))
===================
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

add = sum(crypto)

print(add)
---------------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

result = crypto.items()

print(list(result))
-----------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.clear()

print(crypto)
--------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

check = 7 not in crypto

print(check)
-----------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.pop(3)

print(crypto)
----------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

del crypto[3]

print(crypto)
------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

number = len(crypto)

print(number)
-----------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.update({6: "Monero"})

print(crypto[6])
----------------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.update({4:'Cardano'})

print(crypto[4])
----------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

value = crypto.get(4)

print(value)
---------------------------------
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

value = crypto[4]

print(value)
-------------------------------------------
my_range = range(-10,-9)

print(list(my_range)) #[-10]
--------------------------------------------
my_range = range(-25, 139, 30)

print(list(my_range)) #[-25, 5, 35, 65, 95, 125]
------------------------------------------
my_range = range(-75, -25, 15)

print(list(my_range)) #[-75, -60, -45, -30]
--------------------------------------------
my_range = range(115, 125,5 )

print(list(my_range)) #[115, 120]
-------------------------------------------------
my_range = range(10,20,3)

print(list(my_range)) #[10, 13, 16, 19]
---------------------------------------------------
my_range = range(117, 129)

print(list(my_range)) #[117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]
----------------------------------------------------
my_range = range(10)

print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
---------------------------------------------------
my_range = range(10)

print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
------------------------------------------------------
def m(x):
  l = [0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a=0
    b=1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)
-----------------------------------------------------
def per(n,r):
  if n>r:
    return m(n)/m(n-r)

def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(6,2))
print(com(6,2))
--------------------------------------
def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)

m(6)
-------------------------------------------------------
def m(a,b):
  if len(a) == len(b) and a[::-1]==b[::-1]:
    return "Anagram"
  else:
    return "Not Anagram"

m("listen","silent")
------------------------------------------------------
def m(l,x):
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == x:
        return i,j


m([1,2,3,4,5,6],10)
---------------------------------------------------
def m(s):
  d = {}
  c = 0
  for i in s:
    d[i] = s.count(i)
    c = c + 1
  return d

m("jkcljewlfhfho32oyroy929")
--------------------------------------------------------
def m(s):
  return s[::-1]

m("wjhhohco3hof08u342")
------------------------------------------------------------
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[0:5]

print(my_slice)
-------------------------------------------------------
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[:-3]

print(my_slice)
------------------------------------------------------------------------
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[2:]

print(my_slice)
----------------------------------------------------------
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Estonia", "Romania", "Hungary", "Slovenia")

number = my_tup.count('Estonia')
---------------------------------------------------------
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

last = max(my_tup)

print(last) #should return Slovenia
------------------------------------------------------------
my_tup = ("Romania", "Poland", "Estonia")

(ro , po , es) = my_tup

print(ro + ", " + po + ", " + es) #returns 'Romania, Poland, Estonia'
--------------------------------------------
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

index = my_tup.index('Slovakia')

print(index)
-----------------------------------------------------
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

number = len(my_tup)

print(number)
----------------------------------------------------------------
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

diff = my_set2.difference(my_set1)

print(sorted(list(diff)))
----------------------------------------------------
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

join = my_set1.union(my_set2)

print(sorted(list(join)))
---------------------------------------------
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

common = my_set1.intersection(my_set2)

print(sorted(list(common)))
-------------------------------------------------
my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.remove(9)

print(my_set)
------------------------------------------------
my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.add(19)

print(my_set)
-------------------------------------------------------
my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

check = 10 in my_set

print(check)
-----------------------------------------------------------------
my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = frozenset(my_list)

print(type(my_set))
----------------------------------------------------------------------
def m(x):
  return x**2

list(map(m,[1,2,3,4,5]))
-----------------------------------------------------------------------
a = lambda x,y: x*y

a(10,3)
------------------------------------------------------------------------
a = [1,2,3,4,5]
b = ['a','b','c','d','e']
c = dict(zip(a,b))

for i,j in c.items():
  print(f"{i} --> {j}")

c.update({6:'f'})
c
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
