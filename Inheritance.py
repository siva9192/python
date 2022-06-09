#Parent class
class person:
 def __init__(self,fn,ln):
     self.firstname = fn
     self.lastname  = ln

 def fullname(self):
    print("full name:"+self.firstname,self.lastname)
x=person('siva','kumar')
x.fullname()

#Child class
class student(person):
    def __init__(self, fn, ln,phonenumber):
       super().__init__(fn, ln)
       self.phonenumber=phonenumber
    def welcome(self):
        print(self.fullname(),self.phonenumber)
# # or
#     def __init__(self, fn, ln):
#        person().__init__(fn, ln)
x=student('sada','siva',9866525117)
x.welcome()
