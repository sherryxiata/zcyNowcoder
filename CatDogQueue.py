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
        super().__init__('dog')

class Cat(Pet):
    def __init__(self):
        super().__init__('cat')

# 自定义一个enter类
class PetEnter():
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def getPet(self):
        return self.pet

    def getCount(self):
        return self.count

# 猫狗队列
class CatDogQueue():
    def __init__(self):
        self.catQ = Queue()
        self.dogQ = Queue()
        self.count = 0

    def add(self, pet):
        if pet.getPetType() == 'dog':
            self.dogQ.push(PetEnter(pet, self.count))
            self.count += 1
        elif pet.getPetType() == 'cat':
            self.catQ.push(PetEnter(pet, self.count))
            self.count += 1
        else:
            raise Exception('no dog or cat')

    def pollAll(self):
        if not self.catQ.isEmpty() and not self.dogQ.isEmpty():
            if self.catQ.peek().getCount() < self.dogQ.peek().getCount():
                return self.catQ.pop().getPet()
            else:
                return self.dogQ.pop().getPet()
        elif self.catQ.isEmpty():
            return self.dogQ.pop().getPet()
        elif self.dogQ.isEmpty():
            return self.catQ.pop().getPet()
        else:
            raise Exception('error, no dog or cat')

    def pollDog(self):
        if not self.dogQ.isEmpty():
            return self.dogQ.pop().getPet()
        else:
            raise Exception('no dog')

    def pollCat(self):
        if not self.catQ.isEmpty():
            return self.catQ.pop().getPet()
        else:
            raise Exception('no dog')

    def isEmpty(self):
        return self.catQ.isEmpty() and self.dogQ.isEmpty()

    def isDogEmpty(self):
       return self.dogQ.isEmpty()

    def isCatEmpty(self):
      return self.catQ.isEmpty()

if __name__ == '__main__':
    test = CatDogQueue()

    dog1 = Dog()
    cat1 = Cat()
    dog2 = Dog()
    cat2 = Cat()
    dog3 = Dog()
    cat3 = Cat()

    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    test.add(dog3)
    test.add(cat3)

    while not test.isEmpty():
        print(test.pollAll().getPetType())

    while not test.isCatEmpty():
        print(test.pollCat().getPetType())
