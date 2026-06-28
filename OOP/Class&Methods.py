#Manual entry.

# class Employee:
#     pass     #pass is used with blank class, when they are not used for temp. period

# emp_1 = Employee() # Obj. Creation;
# emp_2 = Employee()

# emp_1.name = "SR"  #instance attributes are specify to obj.
# emp_1.age = 22    # name and age are using as a instance attribute

# emp_2.name = "Hari"
# emp_2.age = 23

#print(emp_1) #print the memory location of that obj.

# print(emp_1.name)
# print(emp_1.age)
# print(emp_2.name)
# print(emp_2.age)

# Dynamicallly Entry

class Employee:
    def __init__(self, first, last): #constructor, self is instace of class.
        self.first =first
        self.last = last
     
    def fullName(self): #method in python
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("SR", "Pradhan")
emp_2 = Employee("Seemant", "Adhikari")

print(emp_1.first)
print(emp_1.last)

print(emp_2.first)
print(emp_2.last)

#print('{} {}'.format(emp_1.first, emp_1.last)) # to print name and age 

print(emp_1.fullName()) #or 
#print(Employee.fullName(emp_1)) #both are same 








