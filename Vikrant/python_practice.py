def count_unique(s):
    '''
    Count the number of unique characters in s.
    >>> count_unique("aaab")
    2
    >>> count_unique("abcdef")
    6
    '''
    # seen_c = [] # O(1)
    # for c in s: # O(n)
    #     if c not in seen_c: #O(n)
    #         seen_c.append(c)
    #
    # return len(seen_c) # O(n^2)
    # sets are immutable
    # seen_c = set()
    # for c in s:
    #     if c not in seen_c:
    #         seen_c.add(c)
    # print(seen_c)
    # return len(seen_c)

    return len(set(s)) # amazing set comprehension

print(count_unique('abcdef'))

# # Built-in Functions
#
# # range and enumerate
#
# # def fizz_buzz(numbers):
# #     for i,num in enumerate(numbers):
# #
# #         if num % 3 ==0:
# #             numbers[i] = "fizz"
# #         if num % 5 ==0:
# #             numbers[i] = "buzz"
# #         if num % 3 == 0 and num % 5 == 0:
# #             numbers[i] = "fizzbuzz"
# #
# #
# # numbers = [45,22,14,65,97,72]
# # fizz_buzz(numbers)
# # print(numbers)
#
# # List comprehensions and useful builtin functions applicable to List
# lst = [1, 2, -5, 4]
# # print(lst)
# # def square(x):
# #     return x*x
# #
# # # lst = list(map(square,lst))
# # # print("After changes:", lst)
# #
# # result = []
# #
# # for num in lst:
# #     result.append(square(num))
# #
# # print(result)
#
#
#
# # def is_odd(num):
# #     return num % 2 == 1
# #
# # lstt = [num for num in lst if is_odd(num)]
# # print(lstt)
#
# ## Debugging
#
# def max(lst):
#     breakpoint()
#     max_num  = 0
#
# age = 10
# name = 'bob'
#
# print(f'My name is {name} and I am {age} year old')
#
# # Sorting
# animals = ["cat", "dog", "rhino"]
# sorted(animals, reverse=True)
#
#
#
# animals = [
# {'type':'cat', 'name':'Stephanie', 'age':8},
# {'type':'dog', 'name':'Bob', 'age':3},
# {'type':'rhino', 'name':'chands', 'age':38}
#
# ]
#
#
# print(list(sorted(animals, key = lambda animal: animal['age'], reverse=True)))
