def myfun():
    print("I'm function")
myfun()

def name(firstname,lastname):
    print('Firstname:'+firstname)
    print('Lastname:'+lastname)
    print('Myname is:'+firstname+' '+lastname)

name('Siva','Kumar')

# Arbitrary Arguments returns result as tuple
def movies(*movies):
    print(movies)
movies('RRR','KGF','I')

# Keyword Arguments   arguments with the key = value syntax.
def child(child1,child2,child3):
    print('the youngist child is:'+child3)
child(child1='Rupesh',child2='siva',child3='Bharat')

# Arbitrary Keyword Arguments, **kwargs  returns  dictionary

def child(**kid):
    print('the youngist child is:'+kid['child3'])
child(child1='Rupesh',child2='siva',child3='Bharat')

#return
def number(x):
    return 5*x
number(3)
# pass
def num():
    pass
num()

# Recursion
def rec(x):
    if(x==1):
        return 1
    else:
        return x+rec(x-1)
rec(3)

# lambda function is a small anonymous function.
x = lambda a : a + 10
print(x(5))


x = lambda a,b,c: a+b+c
print(x(2,1,3))