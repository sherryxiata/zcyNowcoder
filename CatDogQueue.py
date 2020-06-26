# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 11:11
# @Author  : wenlei

'''
猫狗队列问题
'''

class Queue():
    def __init__(self):
        self.arr = []

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return (self.arr.pop(0))

    def peek(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return (self.arr[0])

    def isEmpty(self):
        if not self.arr or len(self.arr) < 1:
            return True

    def size(self):
        return len(self.arr)

# 题目设定的类定义
class Pet():
    def __init__(self, type):
        self.type = type

    def getPetType(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super().__init__('Dog')

class Cat(Pet):
    def __init__(self):
        super().__init__('Cat')

# 自定义一个enter类
class PetEnter():
    def __init__(self):
        self.pet = Pet()
        self.count = 0

    def getPet(self):
        return self.pet

    def getCount(self):
        return self.count

    def getEnterPetType(self):
        return self.pet.getPetType()

# 猫狗队列
class CatDogQueue():
    def __init__(self):

        self.catQueue = PetEnter(Cat)


if __name__ == '__main__':
    dog1 = Dog()
    print(dog1.getPetType())