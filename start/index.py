# name = input('please enter your name: ')
# print(name)
# age = 33
# if age > 18:
#   print('adult')
# else:
#   print('teenager')

# age = 22+ 12
# print(age)


# names = ['Michael', 'Bob']
# for name in names:
#   print(name)

# d = {'Michael': 95, 'Bob': 75}
# print(d.Michael)

# from abstest import my_abs
# print(my_abs(-10))


# L = list(range(100))
# print(L[:], L[: 10], L[1:9], L[-2:-1], L[::25])

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#   print(key, d[key])

# for x, y in [(1, 1), (2,4), (3,9)]:
#   print(x, y)

# lt = list(range(1, 10))

# ran = range(1, 10)

# print(lt, ran)

# L = []
# for x in range(1, 11):
#   L.append(x * x)

# print(L)
# print([x * x for x in range(0, 10) if x > 5])

# print([x * m for x in range(0, 5) for m in range(0,5)])
# import os
# print([d for d in os.listdir('.')])


# d = {'a': 1, 'b': 2, 'c': 3}
# for key, value in d.items():
#   print(key, d[key], value)

# L = ['Hello', 'Word']
# print([s.lower() for s in L])

# L = [x * x for x in range(10)]

# g = (x*x for x in range(10))
# # print(L, next(g), next(g))
# for n in g:
#    print(n)

# def fib(max):
#   n, a, b = 0,0,1
#   while n < max:
#     print(b)
#     a, b = b, a+b
#     n = n + 1
#   return 'done'
# print(fib(10))

# def fib(max):
#   n, a, b = 0,0,1
#   while n < max:
#     yield b
#     a, b = b, a+b
#     n = n + 1
#   return 'done'
# print(fib(10))
# for value in fib(10):
#   print(value)

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
# for value in odd():
#   print(value)

# def fib(max):
#   n, a, b = 0,0,1
#   while n < max:
#     yield b
#     a, b = b, a+b
#     n = n + 1
#   return 'done'

# g = fib(6)
# while True:
#   try: 
#     x = next(g)
#     print('g:', x)
#   except StopIteration as e:
#     print('except', e.value)
#     break


# def f(x):
#   return x * x
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

# from functools import reduce
# def f(x, y):
#   return x * 10 + y

# r = reduce(f, [1, 3, 5, 7, 9])
# print(r)

# f = lambda x: x * x
# print(f(5))

# def now():
#   print('balabala')
# f = now
# print(now.__name__, f.__name__)

# def log(func):
#   def wrapper(*args, **kw):
#     print('call %s:' % func.__name__)
#     return func(*args, **kw)
#   return wrapper

# @log
# def now():
#   print('balabala')
# print(now(), log(now)())

# from module import module.test
# module.test()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 'a test module'
# __author__ = 'candice'
# import sys
# def sysTest():
#   args = sys.argv
#   if len(args) == 1:
#     print('hello, world')
#   elif len(args) ==2:
#     print('hello', args[1])
#   else:
#     print('too many')

# if __name__ == '__main__':
#   sysTest()


# std1 = {'name': 'Michael', 'score': 98}
# std2 = {'name': 'Bob', 'score': 18}

# def print_score(std):
#   print(std['name'], std['score'])
# print_score(std1)

# class
# 面向对象编程的一个重要特点就是数据封装
# class Student(object):
#   def __init__(self, name, score):
#     self.name = name
#     self.score = score
#   def print_score(self):
#       print(self.name, self.score)

# bart = Student('Bart Simpson', 59)
# bart.print_score()

# class Student(object):
#   def __init__(self, name, score):
#     self._name = name
#     self.__score = score
#   def print_score(self):
#     print(self._name, self.__score)

# bart = Student('Bart', 18)
# bart._name = 'candice'
# bart.__score = 20
# bart.print_score()
# print(bart._name, bart.__score)


# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()


#数据封装、继承、多态只是面向对象程序设计中最基础的3个概念


#面向对象的高级编程
# class Student(object):
#   pass
# s = Student()
# def set_age(self, age): # 定义一个函数作为实例方法
#   self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age, s)# 给实例绑定一个方法
# s.set_age(5)
# print(s.age)

#给一个实例绑定的方法，对其它的实例不起作用
# s2 = Student() # 创建新的实例
# s2.set_age(25)
# print(s.age)

#给class绑定方法
# Student.set_age = set_age
# s2 = Student() # 创建新的实例
# s2.set_age(25)
# print(s2.age)


#__slots__ 限制实例添加的属性，仅对当前类的实例起作用，对子类不起作用
# class Student():
#   __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

# s = Student() # 创建新的实例
# s.name = 'Michael' # 绑定属性'name'
# s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score' 报错

# class GraduateStudent(Student):
#   pass
# s = GraduateStudent() # 创建新的实例
# s.name = 'Michael' # 绑定属性'name'
# s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score' 不报错

#@property装饰器是负责把一个方法变成属性调用的，property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
# class Student(object):
#   @property
#   def birthday(self):
#     return self._birthday

#   @birthday.setter
#   def birthday(self, value):
#     self._birthday = value

# s = Student()
# s.birthday = '1992'
# print(s.birthday)

#通过多重继承，一个子类就可以同时获得多个父类的所有功能。如果需要“混入”额外的功能用多重继承，这种设计通常称之为MixIn
#MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

#调试
s = '0'
n = int(s)
print(10 / n)