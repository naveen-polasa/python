# def add_nums(n1,n2):
#     sum = n1+n2
#     return sum


# a = add_nums(32,42)
# print(a)

# print("num")

# x=y=z = 'naveen'
# print(y)

# x='nave'
# y='en'
# z='polasa'

# print(x+y+z)

# a = str(31)
# print(type(a))

# def add(n1,n2):
#     sum =n1+n2
#     return sum

# print(add(132,532))

# import random

# print(random.randrange(1,21))

# a ='naveen polasa me'

# for x in a:
#     print(x)

# print(len(a))

# print('me' in a)

# print('yes' not in a)

# print(a[2:6])

# print(a.upper())

# print(a.lower())

# print(a.strip()) # removes spaces at start or end

# print(a.replace('me', 'you'))

# print(a.split(' '))

# a='naveen'
# b='polasa'

# print(a+ ' ' +b)

# a=9123
# b='naveen{}'

# print(b.format(a))

# a="naveen\"1213\"polasa"
# print(a)

# a=32
# b=3123
# if a>b:
#     print("yes")
# else:
#     print("no")

# print(bool('af'))

# print(231//231)
# print(2**2)
# list =['32','121','131','2983',23,1313]
# print(list)
# print(len(list))

# print(list[3])

# list.insert(2,'11')
# print(list)

# list.sort()
# print(list)
# list.append(32)
# print(list)

# for a in list:
#     print(a)

# tupple = (23,313,"42",32,'232')
# print(tupple)

# sett = {12,24,3,13,12,2141}
# print(sett)

# def func(n1,n4,n2):
#     return n1+n2+n4

# print(func(n2=23,n4=42,n1=122))

# a = lambda b : b * 2
# print(a(2))

# a=0
# while a < 9:
#     print(a)
#     a+=1

# print('23\nnaveen')

# name = int(input('enter name: '))
# name = name+1
# print('hello', name)

# import math

# pi = -3.14
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(429))

# x = 21
# y = 4242
# z = 23

# print(max(x,y,z))
# print(min(x,y,z))

# a='blockchain'
# print(a[0:5:2])

# lice = slice(2,6)
# print(a[lice])

# a = int(input('how old are you? : '))

# if a < 12:
#     print('kid')
# elif a >= 12 and a < 18:
#     print('kid++')
# else :
#     print('adult')

# row = int(input('enter rows: '))
# col = int(input('enter columns: '))
# symbol = input('enter symbol: ')

# for i in range(row):
#     for j in range(col):
#         print(symbol, end="")
#     print()

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert= ["cake", "ice cream "]
# food = [drinks, dinner, dessert]

# for i in food:
#     for j in i:
#         print(j, end=" ")
#     print()

# sett = {'hello','there','how', 'are', 'you'}

# sett.add('hsl')
# sett.remove('hsl')

# for x in sett:
#     print(x)

# caps = {'usa': 'washington','india':'delhi','china':'beijing','russia': 'moscow'}

# caps.update({'name':'naveen'})
# caps.update({'usa':'dc'})
# caps.pop('china')
# caps.clear()
# print(caps['india'])
# print(caps.get('germany'))
# print(caps.keys())
# print(caps.values())
# print(caps.items())

# for key, value in caps.items():
#     print(key,value)

#functions

# def hello(name):
#     print('hello', name)

# hello('Naveen')

# import random
# x = random.randint(1,5)
# print(x)

# class Car:

#     def __init__(self,make,model,year,color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color


#     def drive(self):
#         print('this car is driving')

#     def stop(self):
#         print('this car is stopped')

    

# car1 = Car('chevy','corvette', 2022, 'black')

# print(car1.color)

# car1.drive()

# class Animal():
    
#     def eat(self):
#         print('eating')
#     def run(self):
#         print('running')

# class Dog(Animal):
    
#     legs = 4

#     def bark(self):
#         print('barking')

# class CustomAnimal(Animal):

#     def __init__(self, legs, color, speed):
#         self.legs = legs
#         self.color = color
#         self.speed = speed

#     def getSpeed(self):
#         print(self.speed)

# d1 = Dog()
# d1.bark()
# d1.eat()
# d1.run()

# c1 = CustomAnimal(4, 'green', 50)

# c1.getSpeed()


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    pass
    # def go(self):
    #     print('drive the car')

class Bike(Vehicle):

    def go(self):
        print('drive the bike')


car = Car()

car.go()