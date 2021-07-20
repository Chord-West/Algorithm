'''
배열은 정해진 공간에 데이터를 순차적으로 적재한다.
반면, 링크드 리스트는 노드가 다음 노드(데이터)의 주소값을 가지고 있다.
따라서 배열이 공간의 크기를 미리 할당 해줘야 한다는 단점을 해결할 수 있다.
단, 저장 측면에서는 비효율적이다.

구조
노드(Node): 데이터를 저장하는 단위 (데이터와 포인터로 구성)
포인터(Pointer): 각각의 노드 안에서 다음 노드의 주소(위치)를 가짐
'''

# Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # 포인터

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(data)
    def descend(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self,data):
        if self.head == None:
            return False

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            return
        else:
            node = self.head

            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next


# Test Code
linked_list = LinkedList()

for a in range(1, 10):
    linked_list.insert(a)

linked_list.descend()

linked_list.delete(1)
linked_list.delete(7)
linked_list.delete(9)

print()
linked_list.descend()