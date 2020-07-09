#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 14:56
# @Author  : wenlei

'''
会议室安排
'''

class Program():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

def bestArrange(programs, cur):
    programs.sort()
    res = 0
    for i in range(len(programs)):
        if cur <= programs[i].start:
           res += 1
           cur = programs[i].end
    return res

if __name__ == '__main__':
    p1 = Program(9, 10)
    p2 = Program(9.5, 11)
    p3 = Program(10, 12)
    p4 = Program(11, 13)
    p5 = Program(11.6, 16)
    p6 = Program(8, 18)
    programs = [p1, p2, p3, p4, p5, p6]
    print(bestArrange(programs, 8))