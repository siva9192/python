#Functions
"""
String Methods
1.Format
2.Upper
3.Lower
4.Index
5.Replace
6.Split
7.Strip

Boolen methods
8.Bool

List Methods:
9.Append    --addes element at last
10.Pop
11.Clear    --removes all elements
12.Copy
13.Count
14.Reverse
15.Sort
17.Remove   --removes specifed element
18.Extand
19.Index    --only returns the first occurrence of the value.
20.Insert   --inserts the specified value at the specified position.
"""
# 1.Format
# it is used to concat diffrent type of data
from readline import insert_text
from tkinter.font import names
from unicodedata import name


Name= 'Siva'
Phone= 9866525117

print("I'm {} and my Number is {}".format(Name,Phone)) 
#OR
print("I'm {0} and my Number is {1}".format(Name,Phone))

# 2.Upper
Name ='Python'
print(Name.upper())

# 3.Lower
Name ='PYTHON'
print(Name.lower())

# 4.Index
Name = 'Python'
print(Name.index('P',0))

# 5.Replace
Name = 'Python'
print(Name.replace('y','Y'))

# 6.Split
Name = ('a,b,c') 
print(Name.split(','))

# 7.Strip

Name = '   Python   '
print(Name.strip())
Name = 'Python'
print(Name.lstrip('P'))
print(Name.rstrip('in'))

# 8.Bool
"""
Bool() returns true  when it is NOT IN( '',0,[],(),{} )
"""
#True case
print(bool("python"))
print(bool(2))
print(bool([1,2,3]))
print(bool((1,2,3)))
print(bool({1,2,3}))

#False case
print(bool())
print(bool(0))
print(bool([]))
print(bool(()))
print(bool({}))


##List Methods
# 9.append
Names=['Tokyo','Berlin','Rio']
Names.append('Denver')
print(Names)

# 10.pop
Names=['Tokyo','Berlin','Rio','Denver']
Names.pop()
print(Names)
#specified position 
Names.pop(2)
print(Names)

# 11.clear
Names=['Tokyo','Berlin','Rio','Denver']
Names.clear()
print(Names)

# 12.copy
Names=['Tokyo','Berlin','Rio','Denver']
Names.copy()

# 13.Count

Names=['Tokyo','Berlin','Rio','Denver']
Names.count('Rio')

Numbers = [1,2,3,4,5,6,7,7,8,9]
Numbers.count(7)

# 14.reverse

Names=['Tokyo','Berlin','Rio','Denver']
Names.reverse()
print(Names)

# 15.sort
# syntax list.sort(reverse=True|False, key=myFunc)
Names=['Tokyo','Berlin','Rio','Denver']
Names.sort()
Names.copy()  #ascending 

Names=['Tokyo','Berlin','Rio','Denver']
Names.sort(reverse=True)
Names.copy()  #descending 

def myFunc(a):
  return len(a)
Names=['Tokyo','Berlin','Rio','Denver']

Names.sort(key=myFunc)
Names.copy()  #ascending

def myFunc(a):
  return len(a)
Names=['Tokyo','Berlin','Rio','Denver']

Names.sort(key=myFunc, reverse=True)
Names.copy()  #descending

#16.remove
Names=['Tokyo','Berlin','Rio','Denver']
Names.remove('Rio')
Names.copy() 

#17.extand
Names=['Tokyo','Berlin','Rio','Denver']
Names.extend(Numbers)
Names.copy()

#18.index
Names=['Tokyo','Berlin','Rio','Denver',1,1]
Names.index(1)

# 19.insert
Names=['Tokyo','Berlin','Rio','Denver']
Names.insert(2,Numbers)
Names.copy()