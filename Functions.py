#Functions
"""
1.Format
2.Upper
3.Lower
4.Index
5.Replace
6.Split
7.Strip
"""
# 1.Format
# it is used to concat diffrent type of data
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
