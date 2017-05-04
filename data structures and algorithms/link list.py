# class Node(object):
#
#     def __init__(self,value):
#
#         self.value = value
#         self.nextnode = None
# a = Node(1)
# b = Node(2)
# c = Node(3)
# print(a.value)
# a.nextnode=c
# print(a.nextnode.value)
#
#
#






#
# class node:
#     def __init__(self,vallue):
#         self.value=vallue
#         self.nextnode=None
# a=node(1)
# b=node(2)
# c=node(4)
# print(a.value)
# a.nextnode=c
# print(a.nextnode.value)


#
# class doublelist:
#     def __init__(self,values):
#         self.values=values
#         self.previousvalue=None
#         self.nextvalue=None
# l=doublelist(1)
# m=doublelist(2)
# n=doublelist(3)
# print(n.values)
# n.previousvalue=m
# l.nextvalue=m
# print(n.previousvalue.values)
# print(l.nextvalue.values)
#
#
#
#
# class node():
#     def __init__(self,value):
#         self.value = value
#         self.nextnode = None
# def reverse(head):
#     current=head
#     previous=None
#     next=None
#     while current:
#         nextnode=current.nextnode
#         current.nextnode=previous
#         previous=current
#         current=nextnode
#     return previous
#
#
# a = node(1)
# b = node(2)
# c = node(3)
# d = node(4)
# # Set up order a,b,c,d with values 1,2,3,4
# a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# print(a.nextnode.value)
# print(b.nextnode.value)
# print(c.nextnode.value)
# print(reverse(a))
# print(d.nextnode.value)
# print(c.nextnode.value)
# print(b.nextnode.value)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.nextnode = None
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# d.nextnode = e
# target_node = Node(2,a)
# print(target_node)


# def fact(n):
#     '''
#     Returns factorial of n (n!).
#     Note use of recursion
#     '''
#     # BASE CASE!
#     if n == 0:
#         return 1
#
#     # Recursion!
#     else:
#         return n + fact(n-1)
# print(fact(5))

#
# def rec_sum(n):
#
#     # Base Case
#     if n == 0:
#         return 0
#
#     # Recursion
#     else:
#         return n + rec_sum(n-1)
# print(rec_sum(3))

# def func(n):
#     if n==0:
#         return 1
#     else:
#         return n*func(n-1)
# print(func(6))


#
# def reverse(s):
#
#     # Base Case
#     if len(s) <= 1:
#         return s
#     # Recursion
#     return reverse(s[1:])+ s[0]
# print(reverse('hello world'))


#
# def reverse(s):
#     # Recursion
#     return (s[::-1])
# print(reverse('hello world'))
#
#
#
# def word_split(phrase,list_of_words, output = None):
#     '''
#     Note: This is a very "python-y" solution.
#     '''
#
#     # Checks to see if any output has been initiated.
#     # If you default output=[], it would be overwritten for every recursion!
#     if output is None:
#         output = []
#
#     # For every word in list
#     for word in list_of_words:
#
#         # If the current phrase begins with the word, we have a split point!
#         if phrase.startswith(word):
#
#             # Add the word to the output
#             output.append(word)
#
#             # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
#             # Remember to pass along the output and list of words
#             return word_split(phrase[len(word):],list_of_words,output)
#
#     # Finally return output if no phrase.startswith(word) returns True
#     return output
# print(word_split('bilal','balil'))



# # Create cache for known results
# factorial_memo = {}
#
# def factorial(k):
#
#     if k < 2:
#         return 1
#
#     if not k in factorial_memo:
#         factorial_memo[k] = k * factorial(k-1)
#
#     return factorial_memo[k]
# print(factorial(4))





# def reverse(s):
#     if len(s)<=1:
#         return s
#     else:
#         return reverse(s[1:])+s[0]
# print(reverse('bilal'))
#


# def fib_rec(n):
#
#     # Base Case
#     if n == 0 or n == 1:
#         return n
#
#     # Recursion
#     else:
#         return fib_rec(n-1) + fib_rec(n-2)
# print(fib_rec(10))



# def fib_iter(n):
#
#     # Set starting point
#     a = 0
#     b = 1
#
#     # Follow algorithm
#     for i in range(n):
#
#         a, b = b, a + b
#
#     return a
# print(fib_iter(23))
#






def fib_iter(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
print(fib_iter(20))
























































































