# # Function with Functions
# def name(hello='john'):
#     print('the hello function has been excutec')
#
#     def greet():
#         return 'this is inside the greet function'
#
#     def welcome():
#         return 'This is inside the function'
#
#     if hello=='john':
#         return greet()
#     else:
#         return welcome()

    # print(greet())
    # print(welcome())
    # print('Now WE are on name function ')
# x=name()
# print(x)



# # Functions as arguments
# def hello():
#     return 'hi bilal'
# def other(func):
#     print('hello there')
#     print(func)
# print(other(hello()))
#
#
# def name():
#     return 'great man'
# def answer(hello):
#     print('you are entering func to func')
#     print(hello)
# print(answer(name()))
#
#
# def new_decorator(func):
#     def wrap():
#         print('code here before excuting the func')
#         func()
#         print('code will execute after the func')
#     return wrap()
#
# def func_decorator():
#     print('code decorators')
# func_decorator=new_decorator(func_decorator)
# print(func_decorator)



# def employee(func):
#     def grade1():
#         print('grade 1 employee is pass')
#         func()
#         print('grade 2 employee comes at a right time')
#     return grade1()
# # def new_decorator():
# #     print('you are making new decorator!')
# # new_dedcorator=employee(new_decorator)
# # print(new_dedcorator)
# @employee
# def newdecorator():
#     print('great you have made the manual decorator')
#
# print(employee(newdecorator))
#
#

#
# def name(emp='bilal'):
#     print('hello'+emp)
#
#     def greet():
#         print('you are in greet')
#     def wrap():
#         print('you are in wrap')
#     wrap()
#     greet()
#     print('success')
# print(name())
#
#
# def func(other):
#     print('other function are also include')
#     print(other)
# def hello():
#     return 'bilal'
# print(func(hello()))
#
#
#


#
# def newdecorator(func):
#     def emp():
#         print('hello')
#         func()
#         print('world')
#     return emp()
# @newdecorator
# def newdecorators():
#     print('i am making the deocarator')
# print(newdecorators())



# decorators example
# def newdecorator(original_function):
#     def wrapfuction(*args,**kwargs):
#         print('wrap function calls')
#         return original_function(*args,**kwargs)
#     return wrapfuction()
#
# @newdecorator
# def display(name,age):
#     print('a greet display')
# print(display('bb',21))
#











# # Functions as arguments
# def hello():
#     return 'hi bilal'
# def other(func):
#     print('hello there')
#     print(func)
# print(other(hello()))
#

# decorators and generators

# def gencubes(n):
#     for i in range(n):
#         yield i**3
# for x in gencubes(10):
#     print(x)

#
# def fibonacci(n):
#     a=1
#     b=1
#     for c in range(n):
#         yield a
#         t=a
#         a=b
#         b=t+a
# for aa in fibonacci(10):
#     print(aa)
#


# def fibon(n):
#     a=1
#     b=1
#     output=[]
#     for al in range(n):
#         output.append(a)
#         a,b=b,b+a
#     return output
# print(fibon(10))



def simple_gen():
    for x in range(3):
        yield x
g=simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))




