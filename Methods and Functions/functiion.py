# def myfunction(arg1, arg2):
#     print(arg1+arg2)
# myfunction(1,2)
#
# def helloworld(name):
#     print('my name is '+name )
# helloworld('bilal')


# def student(num1,num2):
#     return num1+num2
# x=student(2,5)
# print(student(4,4))
# print(x)


def prime_number(num):
    for n in range(2,num):
        # n is 2 and num is argument in which you have already give the argument for n that is 9
        if num%n==0:
            print('prime number')
        else:
            print('not prime number')
prime_number(4)




# s= 'Bilal ahmad'
# def globloc(s):
#     d={"upper":0,"lower":0}
#     for c in s:
#         if c.isupper():
#             d["upper"]+=1
#         elif c.islower():
#             d["lower"]+=1
#         else:
#             pass
#     print("on going name",s)
#     print("upper",d["upper"])
#     print("lower",d["lower"])
# globloc(s)
#




def primenumber(num):
    for n in range(1,num):
        if num%n==0:
            print("prime number")
        else:
            print('not prime number')
prime_number(2)





