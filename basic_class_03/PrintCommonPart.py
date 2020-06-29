#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 20:13
# @Author  : wenlei

'''
打印两个有序链表的公共部分
'''

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

def printCommonPart(head1, head2):
    while head1 and head2:
        if head1.val < head2.val:
            head1 = head1.next
        elif head1.val > head2.val:
            head2 = head2.next
        else:
            print(head1.val)
            head1 = head1.next
            head2 = head2.next

if __name__ == '__main__':
    head1 = Node(2)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head1.next.next.next = Node(6)

    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(5)
    head2.next.next.next = Node(7)

    printCommonPart(head1, head2)