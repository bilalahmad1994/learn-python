# import functools
# def even_check(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# d=even_check(43)
# print(d)
#
# list=range(10)
# print(list)
# print(filter(even_check(13),list))
#
# c=filter(lambda num:num%2==0,list)
# print(c)
#
# print(complex(2,4))
#
# def aa(name='bilal'):
#     return 'hello'+name
# print(aa())
#
# s='hello how are you'
# print(globals()['s'])
#
# greet=aa()
# print(greet)
# del greet
# print(greet)
#
#




# counter
# from collections import Counter
# l=[1,1,1,3,3,2,5,5,6,7]
# print(Counter(l))


# s='how many times they are up for running up'
# words=s.split()
# print(Counter(words))



from collections import namedtuple
d=namedtuple('dog','name age breed bark')
sam=d(name='aa',age=12,breed='lab',bark='shefield')
print(sam.bark)


import timeit
print('0-1-2-3-......-99')
c=timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(c)
d=timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(d)



# import datetime
# t=datetime.time(4,25)
# print(t)
# print(datetime.time.min)
# print(datetime.time.max)
# print(datetime.date.today())
# d1=datetime.date(2016,1,11)
# print(d1)
# d2=d1.replace(1993)
# print(d2)
