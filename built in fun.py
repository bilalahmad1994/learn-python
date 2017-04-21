import functools
def even_check(num):
    if num%2==0:
        return True
    else:
        return False
d=even_check(43)
print(d)

list=range(10)
print(list)
print(filter(even_check(13),list))

c=filter(lambda num:num%2==0,list)
print(c)

print(complex(2,4))

def aa(name='bilal'):
    return 'hello'+name
print(aa())

s='hello how are you'
print(globals()['s'])

greet=aa()
print(greet)
del greet
print(greet)



