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



def employee(func):
    def grade1():
        print('grade 1 employee is pass')
        func()
        print('grade 2 employee comes at a right time')
    return grade1()
# def new_decorator():
#     print('you are making new decorator!')
# new_dedcorator=employee(new_decorator)
# print(new_dedcorator)
@employee
def newdecorator():
    print('great you have made the manual decorator')

print(employee(newdecorator))




