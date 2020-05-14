class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count <= (pos-1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.data == item:
                break
            else:
                pre = cur
                cur = cur.next
        pre.next = cur.next





if __name__=="__main__":

    l1 = SingleList()
    print(l1.is_empty())
    print(l1.length())

    l1.add(1)
    l1.add(2)
    l1.add(3)
    l1.add(4)
    l1.travel()
    l1.insert(2, 100)
    l1.travel()
    l1.remove(4)
    l1.travel()





