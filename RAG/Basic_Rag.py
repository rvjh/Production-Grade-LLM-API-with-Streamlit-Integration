


a = lambda x,y: x*y
a(20,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      l.append(a+b)
      a, b = b, a+b
  return l

m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))

print(com(5,2))


def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in range(len(l)):
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3,4],6)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("nclwnllcql")

def m(s):
  return s[::-1]
m("cacnlwl")

response = {
    "open_ai": {
        "gpt3.5": {"total_token": 30, "cost": 4},
        "gpt4o": {"total_token": 10, "cost": 2}
    },
    "amthropic": {
        "gamma2.9": {"total_token": 15, "cost": 2}
    }
}


def m(r):
  d = {}
  for provider, model in r.items():
    for i,j in model.items():
      total = ["total_token"]*j["cost"]
      key = f"{provider}/{i}"
      d[key] = total
  return d

m(response)

select student_id 
from exams
where subject in ('Chemistry','Physics') 
group by student_id
having count(distinct subject)=2 and count(distinct marks)=1

with cte as(
select student_id,
max(case when subject = 'Chemistry' then marks end) chem_marks,
max(case when subject = 'Physics' then marks end) phy_marks
from exams
group by student_id)
select * from cte where chem_marks = phy_marks;

WITH RECURSIVE cte AS (
    SELECT DISTINCT store, 1 AS q_no
    FROM stores
    UNION ALL
    SELECT store, q_no + 1
    FROM cte
    WHERE q_no < 4
),
q AS (
    SELECT store, CONCAT('Q', q_no) AS q_no
    FROM cte
)
SELECT q.store,
       q.q_no missing_quarter
FROM q
LEFT JOIN stores s
       ON q.store = s.store
      AND q.q_no = s.quarter
where s.quarter is null
ORDER BY q.store, q.q_no;

select * from stores;

-- find missing quater

-- using affregation
SELECT store,
CONCAT('Q', 10 - SUM(CAST(RIGHT(quarter, 1) AS UNSIGNED))) AS missing_quarter
FROM stores
GROUP BY store;

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,4],[4,2]
])

b = np.array([
    [1,2],[3,4]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))
print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)


from functools import reduce
reduce(a,[1,2,3,4])

a = lambda x,y : x*y
a(10,3)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      l.append(a+b)
      a, b = b, a+b
  return l

m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))
print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)


def m(l,x):
  d={}
  for i in range(len(l)):
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3,4],6)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("ackaoicnan")

def m(s):
  return s[::-1]
m("nclaksncxlnal")

-- 3/more consecutive empty seats

select * from bms;

-- using lead lag
WITH cte AS (
    SELECT seat_no,
           LAG(is_empty, 1) OVER (ORDER BY seat_no) AS prev_seat_1,
           LAG(is_empty, 2) OVER (ORDER BY seat_no) AS prev_seat_2,
           LEAD(is_empty, 1) OVER (ORDER BY seat_no) AS next_seat_1,
           LEAD(is_empty, 2) OVER (ORDER BY seat_no) AS next_seat_2,
           is_empty
    FROM bms
), cte2 as(
SELECT *,
       CASE 
           WHEN is_empty = 'Y' AND prev_seat_1 = 'Y' AND prev_seat_2 = 'Y'
             OR is_empty = 'Y' AND prev_seat_1 = 'Y' AND next_seat_1 = 'Y'
             OR is_empty = 'Y' AND next_seat_1 = 'Y' AND next_seat_2 = 'Y'
           THEN seat_no
       END AS emp_seat_no
FROM cte)
select * from cte2 
where emp_seat_no is not null;

-- using adv agg
select * from(
SELECT *,
sum(case when is_empty='Y' then 1 else 0 end) OVER (ORDER BY seat_no rows between 2 preceding and current row) AS prev_2,
sum(case when is_empty='Y' then 1 else 0 end) OVER (ORDER BY seat_no rows between 1 preceding and 1 following) AS prev_next_1,
sum(case when is_empty='Y' then 1 else 0 end) OVER (ORDER BY seat_no rows between current row and 2 following) AS next_2
FROM bms) A
where prev_2=3 or prev_next_1=3 or next_2=3

-- using normal logic

with cte as(
select * 
, row_number() over(order by seat_no) rn
, seat_no - row_number() over(order by seat_no) d
from bms
where is_empty = 'Y')
, cte2 as(
select d, count(1) from cte
group by d having count(1)>=3)
select * from cte where d in( select d from cte2)


import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[9,3]
])

b = np.array([
    [1,2],[3,4]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))
print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce
reduce(a,[1,2,3,4])

a = lambda x,y: x*y
a(20,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      l.append(a+b)
      a, b = b, a+b
  return l

m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))

print(com(5,2))

def m(x: int)-> int:
  """factorials on a given number"""

  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)

m(10)

def m(l,x):
  d={}
  for i in range(len(l)):
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3,4],6)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("alhcan;n")

def m(s):
  return s[::-1]
m("zlknclahca")

select * from activity;

-- total active users per day

select event_date, count(distinct user_id) no_of_active_users
from activity
group by event_date;

-- total active users each week

select week(event_date)+1 week_number, count(distinct user_id) week_no
from activity
group by week(event_date)+1;

-- users who purchase on the same day and installed the app

select  event_date, count(new_user) no_of_users from(
select user_id, event_date,
case when count(distinct event_name) = 2 then user_id else null end new_user
from activity 
group by user_id, event_date) A
group by event_date;


-- percentage of paid users in India, USA others tag as others

WITH cte AS (
SELECT *,
CASE WHEN country = 'India' OR country = 'USA' THEN country ELSE 'Others' END AS country_group
FROM activity
WHERE event_name = 'app-purchase'),
total AS (
SELECT COUNT(DISTINCT user_id) AS usr_cnt FROM cte)
SELECT c.country_group, COUNT(*) AS per_users, t.usr_cnt, COUNT(*)/t.usr_cnt *100 per_users
FROM cte c
CROSS JOIN total t
GROUP BY c.country_group, t.usr_cnt;

-- users who installed app on a given date, app purchased on very next day
-- day wise count

with prev_events as(
select * ,
lag(event_name,1) over(partition by user_id order by event_date) prev_event_name,
lag(event_date,1) over(partition by user_id order by event_date) prev_event_date
from activity)
select *
from prev_events
where event_name = 'app-purchase' 
and prev_event_name = 'app-installed' 
and datediff(event_date, prev_event_date)=1;





import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,4],[4,2]
])

b = np.array([
    [1,2],[3,4]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))
print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce
reduce(a,[1,2,3,4])

a = lambda x,y : x*y
a(10,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      l.append(a+b)
      a, b = b, a+b
  return l
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))
print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in range(len(l)):
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i 
  return None
m([1,2,3,4],6)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("dclskdnw")

def m(s):
  return s[::-1]
m("addcbdwbc")

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,4],[4,2]
])

b = np.array([
    [1,2],[3,4]
])

mat_mul(a,b)



a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))
print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce
reduce(a,[1,2,3,4])

a = lambda x,y : x*y
a(10,3)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      l.append(a+b)
      a, b = b, (a+b)
  return l

m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in range(len(l)):
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3,4],6)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("abclqabl")

def m(s):
  return s[::-1]
m("asnclabc")

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,4],[4,2]
])

b = np.array([
    [1,2],[3,4]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))
print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3])

a = lambda x,y : x*y
a(10,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))
print(per(5,2))
print(com(5,2))

def m(z):
  if z==0 or z==1:
    return 1
  else:
    return z*m(z-1)
m(10)


def m(l,x):
  d={}
  for i in range(len(l)):
    diff = x -l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i
m([1,2,3],4)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None
m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("ajbcabclb")

def m(s):
  return s[::-1]
m("alcklk")

select * from billings;
select * from hoursworked;

-- total charges as per billing rate


select * from billings;
select * from hoursworked;

with cte as(
SELECT *,
LEAD(DATE_ADD(bill_date, INTERVAL -1 DAY), 1, '9999-12-31') 
OVER (PARTITION BY emp_name ORDER BY bill_date ASC) AS bill_date_end
FROM billings)
select cte.emp_name, sum(cte.bill_rate * hoursworked.bill_hrs) total_bill
from cte inner join hoursworked on cte.emp_name = hoursworked.emp_name
where hoursworked.work_date between cte.bill_date and cte.bill_date_end
group by cte.emp_name;

with cte as(
select * 
, count(1) over(partition by username) total_activity
, rank() over(partition by username order by startdate) rnk
from useractivity)
select * from cte
where total_activity =1 or rnk=2

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,4],[4,2]
])

b = np.array([
    [1,2],[3,4]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3])

a = lambda x,y : x*y
a(101,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c =a +b
      l.append(c)
      a = b
      b = c
  return l
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))
print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in range(len(l)):
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i
m([1,2,3],4)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None
m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("lkHDOI BCN")

def m(s):
  return s[::-1]
m("jhfkff")

SELECT 
    MONTH(last_month.order_date) AS month_date,
    COUNT(DISTINCT last_month.cust_id) AS total_cust_churn
FROM transactions AS last_month
LEFT JOIN transactions AS this_month
    ON this_month.cust_id = last_month.cust_id
   AND TIMESTAMPDIFF(MONTH, last_month.order_date, this_month.order_date) = 1
WHERE this_month.cust_id IS NULL
GROUP BY MONTH(last_month.order_date);

select * from transactions;

select month(this_month.order_date) month_date, count(distinct last_month.cust_id) total_cust
from transactions this_month left join transactions last_month
on this_month.cust_id = last_month.cust_id and (month(last_month.order_date)- month(this_month.order_date)) = 1 
group by month(this_month.order_date);


import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[3,4]
])

b = np.array([
    [1,2],[3,4]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3,4])

a = lambda x,y : x*y
a(1,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i
m([1,2,3,4],6)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("sklaclann")

def m(s):
  return s[::-1]
m("alhlahl")

SELECT -- u.*, e.*, datediff(e.access_date, u.join_date) no_of_days
count(distinct u.user_id) no_of_users,
count(distinct case when datediff(e.access_date, u.join_date) <= 30 then u.user_id end) prime_members,
count(distinct case when datediff(e.access_date, u.join_date) <= 30 then u.user_id end) /count(distinct u.user_id)*100 per_convert
FROM users_2 u
LEFT JOIN events_2 e 
    ON u.user_id = e.user_id 
   AND e.type = 'P'
WHERE u.user_id IN (
    SELECT user_id 
    FROM events_2 
    WHERE type = 'Music')

select * from orders_2;
select * from products_2;

SELECT 
    concat(p1.name,p2.name)  product,
    COUNT(1) AS freq
FROM orders_2 o1
INNER JOIN orders_2 o2 
    ON o1.order_id = o2.order_id
INNER JOIN products_2 p1 
    ON o1.product_id = p1.id
INNER JOIN products_2 p2 
    ON o2.product_id = p2.id
WHERE o1.product_id > o2.product_id
GROUP BY p1.name, p2.name;

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[1]
  row_b = b.shape[0]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[3,6]
])

b = np.array([
    [3,2],[9,6]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3,4])

a = lambda x,y : x*y
a(10,2)

def m(x):
  l=[0,1]
  if x==1:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3,9],11)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[3,4])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("ajvqljhl")

def m(s):
  return s[::-1]
m("ckhciwii")

-- total sales by year

select * from sales_1;

WITH RECURSIVE cte AS (
    SELECT MIN(period_start) AS dates, MAX(period_end) AS max_date
    FROM sales_1
    UNION ALL
    SELECT DATE_ADD(dates, INTERVAL 1 DAY) AS dates, max_date
    FROM cte
    WHERE dates < max_date)
SELECT product_id, year(dates) report_year, sum(average_daily_sales) total_sales
FROM cte INNER JOIN sales_1 on dates between period_start and period_end
group by product_id, year(dates)
order by product_id, year(dates);



-- recursive cte

with recursive cte as(
select 1 as num
union all
select num +1 
from cte where num<6)
select * from cte

select * from spending;

with cte as(
select spend_date, user_id, max(platform) platform, sum(amount) amount
from spending
group by user_id, spend_date having count(distinct platform) = 1
union all
select spend_date, user_id, "both" platform, sum(amount) amount
from spending
group by user_id, spend_date having count(distinct platform) = 2)
select spend_date, platform, sum(amount) total_amt, count(distinct user_id) no_of_users
from cte 
group by spend_date, platform;


with cte as(
select spend_date, user_id, max(platform) platform, sum(amount) amount
from spending
group by user_id, spend_date having count(distinct platform) = 1
union all
select spend_date, user_id, "both" platform, sum(amount) amount
from spending
group by user_id, spend_date having count(distinct platform) = 2
union all
select distinct spend_date, null as user_id, "both" platform, 0 amount
from spending
)
select spend_date, platform, sum(amount) total_amt, count(distinct user_id) no_of_users
from cte 
group by spend_date, platform;

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[1]
  row_b = b.shape[0]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[2,3]
])

b = np.array([
    [1,2],[2,3]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3,4])

a = lambda x,y : x*y
a(10,3)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)

m(10)

def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3],5)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("cabclab")

def m(s):
  return s[::-1]
m("kjabcB")

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[2,3]
])

b = np.array([
    [1,2],[2,3]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3,4])

a = lambda x,y: x*y
a(10,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)

def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i
m([1,2,3,4],6)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[2,3,4])


def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("asjkcbljab")

def m(s):
  return s[::-1]
m("dcbdb")

select * from tasks;

with cte as(
SELECT t.*,
DATE_ADD(t.date_value, INTERVAL -t.rn DAY) AS adjusted_date
FROM (
    SELECT tasks.*,
	ROW_NUMBER() OVER (PARTITION BY state ORDER BY date_value) AS rn
    FROM tasks
) AS t
ORDER BY t.date_value)
select start_date, end_date, state from(
select adjusted_date, state, min(date_value) start_date, max(date_value) end_date
from cte
group by adjusted_date, state) A
order by start_date



select * from orders_1;
select * from users_1;
select * from items_1;


with cte as(
select o.*, i.item_brand 
from orders_1 o
inner join items_1 i on o.item_id = i.item_id)
, cte2 as(
select *,
row_number() over(partition by users_1.user_id order by cte.order_date) rn
from cte 
right join users_1 on cte.seller_id = users_1.user_id)
, cte3 as(
select seller_id, item_brand, favorite_brand
from cte2 where rn=2 and item_brand = favorite_brand)
select users_1.user_id,
case when cte3.seller_id is null then 'No' else 'Yes' end item_fav_brand
from users_1 left join cte3 on users_1.user_id = cte3.seller_id;

select * from players;
select * from matches;

--  find winner in eahc grp who scored max no of points winin groupd 
-- in case tie lower player id wins 

with cte as(
select player, sum(total_score) score
from(
select first_player player,first_score total_score from matches
union all
select second_player player, second_score total_score from matches) A
group by player)
, cte2 as(
select players.player_id, players.group_id, cte.score
from players inner join cte on players.player_id = cte.player)
, cte3 as(
select * 
, rank() over(partition by group_id order by score desc, player_id asc) rn
from cte2)
select * from cte3 where rn=1;

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[3,2]
])

b = np.array([
    [1,2],[3,2]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3,4])

a = lambda x,y : x*y
a(10,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))
print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3,4],7)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return j 

m([1,2,3],[3,4,5])


def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("acnlbbad")

def m(s):
  return s[::-1]
m("dscwldnl")

select t.request_at,
count(case when t.status in ("cancelled_by_client","cancelled_by_driver") then 1 end) cancelled_trip_cnt,
count(1) total_trip,
count(case when t.status in ("cancelled_by_client","cancelled_by_driver") then 1 end) / count(1) cancelled_per
from trips_1 t
inner join users_3 u on t.client_id = u.users_id
inner join users_3 d on t.driver_id = d.users_id
where d.banned = 'No' and u.banned = 'No'
group by t.request_at

select * from person;
select * from friend;

-- person, id, no of friends, sum of marks of friends > 100


select * from person;
select * from friend;

with cte as(
select f.personid, 	f.friendid, p.score friend_score
from person p
inner join friend f on p.personid = f.friendid)
, cte2 as(
select personid, count(*) no_of_frnds,
sum(friend_score) total_sc
from cte
group by personid)
select cte2.personid,person.name, cte2.no_of_frnds, cte2.total_sc
from cte2 inner join person on cte2.personid = person.personid
where total_sc > 100;

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[1]
  row_b = b.shape[0]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[2,3]
])

b = np.array([
    [2,2],[9,3]
])

mat_mul(a,b)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3])

a = lambda x,y: x*y
a(10,2)


def m(x):
  l = [0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))
print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)

m(12)

def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i
  return d

m([1,2,3,4],7)

def m(a,b):
  d = {}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[2,3,4])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("calcnCO")

def m(S):
  return S[::-1]
m("ajcljqglc")

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]

    return r

a = np.array([
    [1,2],[3,2]
])

b = np.array([
    [1,2],[3,2]
])

mat_mul(a,b)

a = [1,2,3]
b = [2,3,4]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))
print(c)
print(d)
print(e)

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

from functools import reduce

reduce(a,[1,2,3,4])

a = lambda x,y:x*y
a(10,2)

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)


def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))
print(per(5,2))
print(com(5,2))

def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i

m([1,2,3,4],7)

def m(a,b):
  d={}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None
m([1,2,3],[2,3])

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("adlbca")

def m(s):
  return s[::-1]
m("dschlsdl")
----- ----------------

select * from entries;


with cte as(
select name, floor, count(1) no_of_floor_visit, 
rank() over(partition by name order by count(1) desc) rn
from entries
group by name, floor)
, cte2 as(
select name, floor as most_visited_floor 
from cte where rn=1)
select e.name, count(*) total_visits,  c.most_visited_floor,
group_concat(e.resources) item_used
from entries e inner join cte2 c on e.name = c.name
group by e.name, c.most_visited_floor;

select * from orders3;

-- 20% products which are giving 80% of sales

-- select sum(sales) * 0.8 from orders3   -- 1501582.5083043575

with cte as(
select product_id, sum(sales) total_sales
from orders3
group by product_id
order by sum(sales) desc)
, cte2 as(
select * 
, sum(total_sales) over(order by total_sales desc rows between unbounded preceding and 0 preceding) running_sum
, 0.8 * sum(total_sales) over() 80_per_sell
from cte)
select * from cte2
where  running_sum  <= 80_per_sell

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[1]
  row_b = b.shape[0]
  if row_b != col_a:
    return "not possible"
  else:
    r = np.zeros((row_b, col_a))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,2],[2,3]
])

b = np.array([
    [1,2],[2,3]
])

mat_mul(a,b)

def m(s):
  return s[::-1]
m("adlkcnlak")


def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("sdlvnlkn")

def m(a,b):
  d = {}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[2,3])


def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i 
  
m([1,2,3,4],7)


def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)



a = lambda x,y: x*y
a(10,2)

from functools import reduce

reduce(a,[1,2,3,4])

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,3],[4,1]
])

b = np.array([
    [1,3],[4,1]
])

mat_mul(a,b)

from langchain_community.document_loaders import TextLoader, WebBaseLoader, PyPDFLoader
import bs4
from langchain.text_splitter import  RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

## Textloader
loader = TextLoader("RAG/speech.txt")
text_documents = loader.load()

print(text_documents)

## webloader

# web_loader = WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
#                            bs_kwargs=dict(parse_only=bs4.SoupStrainer(
#                                class_=("post-title","post-content","post-header")
#                            )))
#
# text_documents_web = web_loader.load()
# print(text_documents_web)

## load from PDF

pdf_loader = PyPDFLoader(file_path="RAG/Srijan Nirmal Kumar Galla_Data Analyst (1).pdf")
text_pdf_loader = pdf_loader.load()
print(text_pdf_loader)

## text splitting

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
documents = text_splitter.split_documents(text_pdf_loader)
print(documents)

## vector embeddings and vectr store

db = Chroma(documents[:], OllamaEmbeddings())

query = "Who are the authors of attention is all you need?"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)














































































































































































































