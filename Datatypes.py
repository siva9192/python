# Datatypes
"""
1.Numeric 
    * int
    * Float
    * Complex 
2.Boolean
3.Set
4.Dictionary
5.SequenceType
    * String
    * List
    * Tuple

"""
#Numeric
A= 20
print(type(A))  #int
A=22.3
print(type(A))  #float
A=2+3j
print(type(A))  #complex

#Boolean
True - False
A= True
print(type(A)) #bool
A= False
print(type(A)) #bool

#Set
A= {1,2,3}
print(type(A)) #set

#Dictionary
A= {1:'a',2:'b',3:'c'}
print(type(A)) #dict

# SequenceType

A="Python"
print(type(A)) #str

A=[1,2,3]
print(type(A)) #list

A=(1,"python",3.2) #tuple
print(type(A))
