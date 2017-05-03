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


def fact(n):
    '''
    Returns factorial of n (n!).
    Note use of recursion
    '''
    # BASE CASE!
    if n == 0:
        return 1

    # Recursion!
    else:
        return n + fact(n-1)
print(fact(5))


def rec_sum(n):

    # Base Case
    if n == 0:
        return 0

    # Recursion
    else:
        return n + rec_sum(n-1)
print(rec_sum(3))


