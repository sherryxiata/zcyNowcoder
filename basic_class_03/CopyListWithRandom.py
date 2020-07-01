# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 9:12
# @Author  : wenlei

'''
复制含有随机节点的链表
'''

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

# 解法1：哈希表
def copyListWithRandom1(head):
    hashMap = {}
    cur = head
    while cur:
        hashMap[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        hashMap.get(cur).next = hashMap.get(cur.next)
        hashMap.get(cur).random = hashMap.get(cur.random)
        cur = cur.next
    return hashMap.get(head)

# 解法2：复制、分离
def copyListWithRandom2(head):
    if not head:
        return None
    cur = head
    while cur:
        next = cur.next
        cur.next = Node(cur.val)
        cur.next.next = next
        cur = next
    cur = head
    while cur:
        next = cur.next.next
        curCopy = cur.next
        curCopy.random = cur.random.next if cur.random else None
        cur = next
    cur = head
    res = cur.next
    while cur:
        next = cur.next.next
        curCopy = cur.next
        cur.next = next
        curCopy.next = next.next if next else None
        cur = next
    return res

def printListWithRandom(head):
    cur = head
    print('\norder:', end = '')
    while cur:
        print(cur.val, end = '', sep = ',')
        cur = cur.next
    cur = head
    print('\nrandom:', end = '')
    while cur:
        print(cur.val, end = '', sep = ',') if cur.random else print('-', end = '', sep = ',')
        cur = cur.next

if __name__ == '__main__':
    head = None
    printListWithRandom(head)
    res1 = copyListWithRandom1(head)
    printListWithRandom(res1)
    res2 = copyListWithRandom2(head)
    printListWithRandom(res2)
    printListWithRandom(head)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.random = head.next.next.next.next.next # 1 -> 6
    head.next.random = head.next.next.next.next.next # 2 -> 6
    head.next.next.random = head.next.next.next.next # 3 -> 5
    head.next.next.next.random = head.next.next # 4 -> 3
    head.next.next.next.next.random = None # 5 -> null
    head.next.next.next.next.next.random = head.next.next.next # 6 -> 4

    printListWithRandom(head)
    res1 = copyListWithRandom1(head)
    printListWithRandom(res1)
    res2 = copyListWithRandom2(head)
    printListWithRandom(res2)
    printListWithRandom(head)