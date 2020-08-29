# # def count_unique(s):
# #     '''
# #     Count the number of unique characters in s.
# #     >>> count_unique("aaab")
# #     2
# #     >>> count_unique("abcdef")
# #     6
# #     '''
# #     # seen_c = [] # O(1)
# #     # for c in s: # O(n)
# #     #     if c not in seen_c: #O(n)
# #     #         seen_c.append(c)
# #     #
# #     # return len(seen_c) # O(n^2)
# #     # sets are immutable
# #     # seen_c = set()
# #     # for c in s:
# #     #     if c not in seen_c:
# #     #         seen_c.add(c)
# #     # print(seen_c)
# #     # return len(seen_c)
# #
# #     # return len(set(s)) # amazing set comprehension
# #     return len({c for c in s})
# #
# # print(count_unique('aaab'))
#
# # # Built-in Functions
# #
# # # range and enumerate
# #
# # # def fizz_buzz(numbers):
# # #     for i,num in enumerate(numbers):
# # #
# # #         if num % 3 ==0:
# # #             numbers[i] = "fizz"
# # #         if num % 5 ==0:
# # #             numbers[i] = "buzz"
# # #         if num % 3 == 0 and num % 5 == 0:
# # #             numbers[i] = "fizzbuzz"
# # #
# # #
# # # numbers = [45,22,14,65,97,72]
# # # fizz_buzz(numbers)
# # # print(numbers)
# #
# # # List comprehensions and useful builtin functions applicable to List
# # lst = [1, 2, -5, 4]
# # # print(lst)
# # # def square(x):
# # #     return x*x
# # #
# # # # lst = list(map(square,lst))
# # # # print("After changes:", lst)
# # #
# # # result = []
# # #
# # # for num in lst:
# # #     result.append(square(num))
# # #
# # # print(result)
# #
# #
# #
# # # def is_odd(num):
# # #     return num % 2 == 1
# # #
# # # lstt = [num for num in lst if is_odd(num)]
# # # print(lstt)
# #
# # ## Debugging
# #
# # def max(lst):
# #     breakpoint()
# #     max_num  = 0
# #
# # age = 10
# # name = 'bob'
# #
# # print(f'My name is {name} and I am {age} year old')
# #
# # # Sorting
# # animals = ["cat", "dog", "rhino"]
# # sorted(animals, reverse=True)
# #
# #
# #
# # animals = [
# # {'type':'cat', 'name':'Stephanie', 'age':8},
# # {'type':'dog', 'name':'Bob', 'age':3},
# # {'type':'rhino', 'name':'chands', 'age':38}
# #
# # ]
# #
# #
# # print(list(sorted(animals, key = lambda animal: animal['age'], reverse=True)))
#
# # Linked list
#
#
#
# #
# #
# # class Node:
# #     def __init__(self, dataval=None):
# #         self.dataval = dataval
# #         self.nextval = None
# #
# # class SLinkedList:
# #     def __init__(self):
# #         self.headval = None
# #
# #     def listprint(self):
# #         printval = self.headval
# #         while printval is not None:
# #             print(printval.dataval)
# #             printval = printval.nextval
# #
# #     def AtBegining(self, newdata):
# #         NewNode = Node(newdata)
# #         NewNode.nextval = self.headval
# #         self.headval = NewNode
# #
# #     def AtEnd(self, newdata):
# #         NewNode = Node(newdata)
# #         if self.headval is None:
# #             self.headval = NewNode
# #             return
# #         laste = self.headval
# #         while(laste.nextval):
# #             laste = laste.nextval
# #         laste.nextval = NewNode
# #
# #     def InBetween(self, middle_node, newdata):
# #         if middle_node is None:
# #             print("The mentioned node is absent")
# #             return
# #
# #         NewNode = Node(newdata)
# #         NewNode.nextval = middle_node.nextval
# #         middle_node.nextval = NewNode
# #
# #     def RemoveNode(self, RemoveKey):
# #         '''
# #         Removing node from linked List
# #         '''
# #         HeadVal = self.headval
# #
# #         if HeadVal is not None:
# #             if HeadVal.dataval == RemoveKey:
# #                 self.headval = HeadVal.nextval
# #                 HeadVal = None
# #
# #
# #         while HeadVal is not None:
# #             if HeadVal.dataval == RemoveKey:
# #                 break
# #             prev = HeadVal
# #             HeadVal = HeadVal.nextval
# #
# #         if HeadVal == None:
# #             return "Nothing to remove dawg"
# #
# #         prev.nextval = HeadVal.nextval
# #         print('successful dawg')
# #         HeadVal =None
# #
# #
# #
# #
# # list1 = SLinkedList()
# # list1.headval = Node("Mon")
# # e2 = Node("Tue")
# # e3 = Node("Wed")
# #
# #
# # # Link first Node to second Node
# # list1.headval.nextval = e2
# #
# # # Link sedond node to third Node
# # e2.nextval = e3
# # # print(e2.dataval)
# # # print(e2.nextval)
# # list1.AtBegining("Sun")
# # list1.AtEnd("Thus")
# # list1.InBetween(list1.headval.nextval, "Fri")
# # list1.listprint()
# # list1.RemoveNode("Fri")
# # list1.listprint()
#
# # Insertion
# import collections
#
# class Queue:
#     def __init__(self):
#         self.queue = list()
#
#     def addtoq(self, dataval):
#         if dataval not in self.queue:
#             self.queue.insert(0,dataval)
#             return True
#         return False
#
#     def size(self):
#         return len(self.queue)
#
#     def removefromq(self):
#         if len(self.queue)>0:
#             return self.queue.pop()
#         return "No elements in Queue"
#
#
#
# # TheQueue = Queue()
# # TheQueue.addtoq("Mon")
# # TheQueue.addtoq("Tue")
# # TheQueue.addtoq("Wed")
# # print(TheQueue.size())
# # print(TheQueue.removefromq())
# # print(TheQueue.removefromq())
# lst = ['mon', 'tues', 'wed']
# DoubleEnded = collections.deque(lst)
# DoubleEnded.append("Thus")
# print ("Appended at right - ")
# print (DoubleEnded)
#
# DoubleEnded.appendleft("Sun")
# print ("Appended at right at left is - ")
# print (DoubleEnded)
#
# DoubleEnded.pop()
#
# print ("Deleting from right - ")
# print (DoubleEnded)
#
# DoubleEnded.popleft()
#
# print ("Deleting from left - ")
# print (DoubleEnded)
#
#
# # Traversing a Linked list

#
# # Generators
# g = (i for i in range(6))
# print(next(g))




# student_grades = {
#
# "Jack": [65,65,76.4,63],
# "Jill": [22.34,34,54,43]
#
# }



#
# from collections import defaultdict, Counter, deque, namedtuple
#
# def top_three(string):
#     counter = defaultdict(int) # defaults to 0
#     for c in string:
#         counter[c] += 1
#     top_3 = sorted(counter, key = lambda k: counter[k], reverse=True)[:3]
#     return [(letter, counter[letter]) for letter in top_3]
#
#
# # print(top_three("aabbccd"))
# # print(Counter("aabbccd").most_common(3))
#
# Car = namedtuple("Car", ["color", "make", "model", "mileage"])
#
# print(Car("silver","German Make","2020","10000"))

# import string
# # print(string.whitespace)
# # print(ord('A'), ord('a'))
# whitespace_set = set(string.whitespace)
# # print(whitespace_set)
#
#
# # print(''.join(letter for letter in 'HELLO WORLD' if letter not in whitespace_set))
#
# import itertools as it
# from functools import reduce, lru_cache
# import time


# print("--- %s seconds ---" % (time.time() - start_time))

#
# print(reduce(lambda x,y: x+y, [1,2,3,4]))
# #
# # all_ones = it.repeat(1)
# # print(next(all_ones), next(all_ones), next(all_ones), next(all_ones))
#
# # print(list(map(pow, range(10), it.repeat(2))))
#
# friends = ['ajckl', 'jill', 'joe']
# print(list(it.combinations(friends,r = 1)))

# # @lru_cache(1)
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# start_time = time.time()
# print(fib(5))
# print("--- %s seconds ---" % (time.time() - start_time))


# Back to Inheritance and Composition
# arrays




# a  = [1,2,3,4,5]
#
# # print(a[::-1])
# # print(' '.join(map(str, a[::-1])))
#
# n = 5
# d = 3
#
# print((a[d:] + a[0:d]))

# -------------------------------
# import math
# import os
# import random
# import re
# import sys
#
#
#
# if __name__ == '__main__':
#     nd = input().split()
#
#     n = int(nd[0]) # 5
#
#     d = int(nd[1]) # 3
#
#
#     a = list(map(int, input().rstrip().split()))
#
#     for value in (a[d:] + a[0:d]):
#         print(value, end=' ')

#
# a = ["abv", "fff", "rre"]
# # print(set(a))
#
# from collections import defaultdict
# fq= defaultdict(int)
# for w in a:
#     fq[w] += 1
#
# print(dict(fq))



#
#
# import collections
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List : ",my_list)
# ctr = collections.Counter(my_list)
#
# print(dict(ctr))



# s ='UDDDUDUU'
# print(list(s))



# Binary Search



# a = [1,2,3,4,5,67,99,104,111,146,197]
# val = 99
#
# def binarySearch(arr, val):
#     low = 0
#     high = len(a)-1
#
#     while low<=high:
#         mid = (low+high)//2
#         if val == arr[mid]:
#             return True
#         if val < arr[mid]:
#             high = mid
#         else:
#             low = mid
#     return False
#
# print(binarySearch(a,val))



# class Array:
#     def __init__(self, leng, capacity):
#         self.leng = leng
#         self.capacity = capacity


# queries = [[1,0,5]]#,[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
# for q in queries:
#     print(queries[(q[1]^0)%1])

# arr = [0,0,0,0,0]
# p,q,k,i,j = arr
# print(p)

# import numpy as np
# empty_list = [[0,0,0,0,0],
#        [100,100,0,0,0],
#        [100,200,100,100,100],
#        [100,200,200,200,100]]
# print(np.max(empty_list))

# for i in range(1,3):
#     empty_list[0][i-1] = empty_list[0][i-1] + 100
#     # print(empty_list)
# arr.append(*empty_list)
#
# print(arr)



# from collections import defaultdict
# from itertools import accumulate
# a = defaultdict(int)
# print(a)
#
# a[1] += 100
# a[3] -= 100
# print(a)
# a[2] += 100
# a[6] -= 100
# print(a)
# a[3] += 100
# a[5] -= 100
# print(a)
#
# print(max(accumulate(a[i] for i in sorted(a))))




# Best ever array manipulation


# def arrayManipulation(n, queries):
#     a = defaultdict(int)
#     for ele in queries:
#         p,q,k = ele
#         a[p] += k
#         a[q+1] -= k # normalize for accumulate operation
#     return max(accumulate(a[i] for i in sorted(a)))







# A tree whose nodes have atmost 2 elements is called a binary tree.
# left and right child




# @classmethod vs @staticmethod

# class MyClass:
#     def method(self):
#         return 'instance method called', self
#
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#
#     @staticmethod
#     def staticmethod():
#         return 'static method called'
#
# class Pizza:
#     def __init__(self, ingredients, radius):
#         self.ingredients = ingredients
#         self.radius = radius
#
#     def __repr__(self):
#         return f'Pizza({self.ingredients})'
#
#     def area(self):
#         return self.__circle_area(self.radius)
#
#     @staticmethod
#     def __circle_area(r):
#         return r**2*math.pi
#
#
#     @classmethod
#     def margherita(cls):
#         return cls(['cheese','tomatoes'])
#
#     @classmethod
#     def prosciutto(cls):
#         return cls(['cheese','tomatoes','ham','mushrooms'])



# print(Pizza.margherita())
# print(Pizza.prosciutto())

# obj = MyClass()
# print(obj.method())

# print('='*50)
# # print(obj.classmethod())
# # print(obj.staticmethod())
#
#
#
# print(MyClass.classmethod())
# print(MyClass.staticmethod())
# print(MyClass.method())
#
#
#
#




# Recursion Basics Towers of Hanoi - minimum 2^n - 1 steps

# so for 3 disks minimum 7 steps
#
# def Hanoi(disk, source, dest, aux):
#     if disk == 1:
#         print("Move disk 1 from source", source, "to destination", destination)
#         return
#     Hanoi(disk-1, source, auxiliary, destination)
#     print("Move disk", n, "from source", soure, "to destination", destination)
#     Hanoi(disk-1, auxiliary, destination, source)
#
#
#
#
# # Driver code
# disk = 4
# Hanoi(disk,'A','B','C')
# A, C, B are the name of rods

# Contributed By Dilip Jain




# Binary Tree in Python
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert node
    def insert(self, data):

        if self.data:
            if data < self.data:

                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data


        # Print tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

        # Inorder Traversal
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res+ self.inorderTraversal(root.right)
        return res


root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)



print(root.PrintTree(),sep='=')
print(root.inorderTraversal(root),sep='=')
