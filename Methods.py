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
16.Remove   --removes specifed element
17.Extand
18.Index    --only returns the first occurrence of the value.
19.Insert   --inserts the specified value at the specified position.

Tuple Methods
20.Count
21.Index

Set Methods
22.Add()	                      Adds an element to the set
23.Clear()	                    Removes all the elements from the set
24.Copy()	                      Returns a copy of the set
25.Difference()	                Returns a set containing the difference between two or more sets
26.Difference_update()	        Removes the items in this set that are also included in another, specified set
27.discard()	                    Remove the specified item
28.Intersection()	              Returns a set, that is the intersection of two other sets
29.Intersection_update()        Removes the items in this set that are not present in other, specified set(s)
30.Isdisjoint()	                Returns whether two sets have a intersection or not
31.Issubset()	                  Returns whether another set contains this set or not
32.Issuperset()	                Returns whether this set contains another set or not
33.Pop()	                      Removes an element from the set
34.Remove()	                    Removes the specified element
35.Symmetric_difference()	      Returns a set with the symmetric differences of two sets
36.Symmetric_difference_update()inserts the symmetric differences from this set and another
37.Union()	                    Return a set containing the union of sets
38.Update()	                    Update the set with the union of this set and others

Dictionary Methods
39.clear()	                    Removes all the elements from the dictionary
40.copy()	                      Returns a copy of the dictionary
41.fromkeys()	                  Returns a dictionary with the specified keys and value
42.get()	                      Returns the value of the specified key
43.items()	                    Returns a list containing a tuple for each key value pair
44.keys()	                      Returns a list containing the dictionary's keys
45.pop()	                      Removes the element with the specified key
46.popitem()	                  Removes the last inserted key-value pair
47.setdefault()	                Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
48.update()	                    Updates the dictionary with the specified key-value pairs
49.values()	                    Returns a list of all the values in the dictionary
"""
# 1.Format
# it is used to concat diffrent type of data
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

##Tuple Methods
#20.count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(5))

#21.index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.index(5))

#Set Methods
#22.add
Names = {'Rio','Manika','Denver'}
Names.add('nairobi')
print(Names)

#23.clear
Names = {'Rio','Manika','Denver'}
Names.clear()
print(Names)

#24.copy
Names = {'Rio','Manika','Denver'}
x = Names.copy()
print(x)

#25.difference
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
z= x.difference(Names)
print(z)

#26.difference_update
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
x.difference_update(Names)
print(x)

#27.discard
Names = {'Rio','Manika','Denver'}
Names.discard('Rio')
print(Names)

#28.intersection
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
z= x.intersection(Names)
print(z)

#29.intersection_update
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
x.intersection_update(Names)
print(x)

#30.isdisjoint
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
z= x.isdisjoint(Names)
print(z)

#31.issubset
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
z= x.issubset(Names)
print(z)

#32.issuperset
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
z= x.issuperset(Names)
print(z)

#33.pop
Names = {'Rio','Manika','Denver'}
Names.pop()
print(Names)

#34.remove
Names = {'Rio','Manika','Denver'}
Names.remove('Rio')
print(Names)

#35.symmetric_difference
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
z= x.symmetric_difference(Names)
print(z)

#36.symmetric_difference_update
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
Names.symmetric_difference_update(x)
print(Names)

#37.union
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
z= x.union(Names)
print(z)

#38.update
Names = {'Rio','Manika','Denver'}
x = {'Rio','Manika','Denver','nairobi'}
Names.update(x)
print(Names)

##Dictionary Methods
#39.clear()	  
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
Names.clear()
print(Names)

#40.copy()
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
x = Names.copy()
print(x)
	          
#41.fromkeys()
Names =("Rio","denver","Nairobi")
x = 0
Names = dict.fromkeys(Names,x)
print(Names)
#42.get()	
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
print(Names.get("name"))
           
#43.items()	
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
print(Names.items())
         
#44.keys()	
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
print(Names.keys())
          
#45.pop()	
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
print(Names.pop("Age"))
           
#46.popitem()	
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
print(Names.popitem())
       
#47.setdefault()
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
x = Names.setdefault("name","Denver")
print(x)
	    
#48.update()	
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
Names.update({"name":"Denver"})
Names.update({"phone":9866})
print(Names)
#49.values()	        
Names={
  "name"  :"Rio",
  "Age"   : 39,
  "Gender":"Male"

}
print(Names.values())