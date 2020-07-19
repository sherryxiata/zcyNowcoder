#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 20:32
# @Author  : wenlei

'''
两链表相交的一系列问题
'''

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

def getInsertNode(head1, head2):
    if not head1 or not head2:
        return None
    # 判断是否有环，返回入环节点
    loop1 = getLoopNode1(head1)
    loop2 = getLoopNode1(head2)
    if not loop1 and not loop2:
        # 两个无环链表的相交问题
        return noLoop1(head1, head2)
    if loop1 and loop2:
        # 两个有环链表的相交问题
        return bothLoop1(head1, head2, loop1, loop2)
    # 一个有环，一个无环
    return None

# 解法1
def getLoopNode1(head):
    if not head or not head.next or not head.next.next:
        return None
    s = head.next # 慢指针
    f = head.next.next # 快指针
    while f != s:
        if not f.next or not f.next.next:
            return None
        f = f.next.next
        s = s.next
    f = head
    while f != s:
        f = f.next
        s = s.next
    return s

def noLoop1(head1, head2):
    cur1 = head1
    cur2 = head2
    n = 0
    while cur1.next:
        n += 1
        cur1 = cur1.next
    while cur2.next:
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        return None
    cur1 = head1 if n > 0 else head2
    cur2 = head2 if cur1 == head1 else head1
    n = abs(n)
    while n > 0:
        n -= 1
        cur1 = cur1.next
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

def bothLoop1(head1, head2, loop1, loop2):
    if loop1 == loop2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1 != loop1:
            n += 1
            cur1 = cur1.next
        while cur2 != loop2:
            n -= 1
            cur2 = cur2.next
        cur1 = head1 if n > 0 else head2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)
        while n > 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.next
        return None

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next  # 8->6
    print(getInsertNode(head1, head2).val) # 6

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next.next = head1.next.next.next # 7->4
    #
    # head2 = Node(0)
    # head2.next = Node(9)
    # head2.next.next = Node(8)
    # print(getInsertNode(head1, head2).val) # Nnone

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next # 8->2
    print(getInsertNode(head1, head2).val) # 2

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next # 8->6
    print(getInsertNode(head1, head2).val) # 4 / 6

