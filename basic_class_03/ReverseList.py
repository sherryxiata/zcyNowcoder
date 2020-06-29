# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 10:16
# @Author  : wenlei

'''
反转单向链表和双向链表
'''

# 单向链表的节点
class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

def printLinkedList(head):
    res = []
    while head != None:
        res.append(head.val)
        head = head.next
    print(res)

# 双向链表
class DoubleNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.last = None

def reverseDoubleList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next
    return pre

def printDoubleLinkedList(head):
    res1 = []
    end = None
    while head:
        res1.append(head.val)
        end = head
        head = head.next
    print(res1)

    res2 = []
    while end:
        res2.append(end.val)
        end = end.last
    print(res2)

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    printLinkedList(head1)
    head1 = reverseList(head1)
    printLinkedList(head1)

    head2 = DoubleNode(1)
    head2.next = DoubleNode(2)
    head2.next.last = head2
    head2.next.next = DoubleNode(3)
    head2.next.next.last = head2.next
    head2.next.next.next = DoubleNode(4)
    head2.next.next.next.last = head2.next.next
    printDoubleLinkedList(head2)
    head2 = reverseDoubleList(head2)
    printDoubleLinkedList(head2)