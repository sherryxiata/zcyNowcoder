#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 14:45
# @Author  : wenlei

'''
合并两个有序链表并去重
'''

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def merge(l1, l2):
    head = ListNode(-1)
    cur = head
    hash = set()
    while l1 and l2:
        if l1.val <= l2.val:
            if l1.val not in hash:
                cur.next = l1
                hash.add(l1.val)
                cur = cur.next
            l1 = l1.next
        else:
            if l2.val not in hash:
                cur.next = l2
                hash.add(l2.val)
                cur = cur.next
            l2 = l2.next
        print(hash)
    while l1:
        if l1.val not in hash:
            cur.next = l1
        l1 = l1.next
    while l2:
        if l2.val not in hash:
            cur.next = l2
        l2 = l2.next
    return head.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l = merge(l1, l2)
while l:
    print(l.val)
    l = l.next

