#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 14:48
# @Author  : wenlei

'''
给定一个单链表，使得链表中奇数位于偶数之前。
O(N) O(1) 但不能保证稳定性
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenSort(head):
    newHead = Node(-1)
    newHead.next = head
    l, cur = newHead, head
    while cur:
        if cur.val % 2 != 0:
            l.next.val, cur.val = cur.val, l.next.val
            l = l.next
        cur = cur.next
    return newHead.next

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(1)
    res = oddEvenSort(head)
    while res:
        print(res.val)
        res = res.next