# class employee():
#     pass
#
# emp_1=employee()
# emp_2=employee()
#
# emp_1.firstname='bilal'
# emp_1.lastname='ahmad'
# emp_1.email='bilalshakeel590@gmail.com'
#
# emp_2.firstname='sami'
# emp_2.lastname='ahmad'
# emp_2.email='samishakeel590@gmail.com'
#
#
# print(emp_1.email)
# print(emp_2.email)
#

# def __init(self)-->is init method (e.g initialize( if you are coming from other language it is called constructor)
# when we create methods in class it recieve first instances(arguments) automatically

# class employee():
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.salary=salary
#
# name1=name('sami' ,'ahmad','1200$')
# print(name1.first)
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
#
#

#
# class names():
#     species='mammals'
#
#     def __init__(self,breed,name):
# Instance variable are unique that we used with self object instant
#         self.breed=breed
#         self.name=name
# abc=names('dog','german')
# cdf=names('dog','ireland')
# print(names.species)
# print(names.__init__())


class employee():
    ceo='samiahmad'
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'gmail.com'

    def fullname(self):
<<<<<<< Updated upstream
        return '{}{}'.format(self.first,self.last)
emp1=employee('bilal','ahmad',5000)
print(employee.ceo)
print(emp1.email)
print(employee.fullname(emp1))




=======
        return '{} {}'.format(emp_1.first, emp_1.last)
emp_1=employee('bilal','ahmad',5000)
emp_2=employee('sami','ahmad',3000)

print(emp_1.email)
print(emp_2.email)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
print(emp_1.fullname())
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes


