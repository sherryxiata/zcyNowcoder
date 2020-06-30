#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 19:39
# @Author  : wenlei

'''
将单向链表调整成左小中等右大的形式
'''

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：荷兰国旗
def smallerEqualBigger1(head, num):
    if not head:
        return head
    arr = []
    while head:
        arr.append(head)
        head = head.next
    partition(arr, num)
    for i in range(len(arr) - 1):
        arr[i].next = arr[i + 1]
    arr[-1].next = None
    return arr[0]

def partition(arr, num):
    index = 0
    less = -1
    more = len(arr)
    while index < more:
        if arr[index].val < num:
            less += 1
            swap(arr, less, index)
            index += 1
        elif arr[index].val == num:
            index += 1
        else:
            more -= 1
            swap(arr, more, index)

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

# 解法2
def smallerEqualBigger2(head, num):
    sH, sT, eH, eT, bH, bT = None, None, None, None, None, None
    while head:
        next = head.next
        head.next = None
        if head.val < num:
            if not sH:
                sH = head
            else:
                sT.next = head
            sT = head
        elif head.val == num:
            if not eH:
                eH = head
            else:
                eT.next = head
            eT = head
        else:
            if not bH:
                bH = head
            else:
                bT.next = head
            bT = head
        head = next
    if sT:
        sT.next = eH
        eT = eT if eT else sT
    if eT:
        eT.next = bH

    return sH if sH else eH if eH else bH

def printLinkedList(head):
    res = []
    while head != None:
        res.append(head.val)
        head = head.next
    print(res)

if __name__ == '__main__':
    head1 = Node(7)
    head1.next = Node(9)
    head1.next.next = Node(1)
    head1.next.next.next = Node(8)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(2)
    head1.next.next.next.next.next.next = Node(5)
    printLinkedList(head1)
    # head1 = smallerEqualBigger1(head1, 5)
    head1 = smallerEqualBigger2(head1, 5)
    printLinkedList(head1)