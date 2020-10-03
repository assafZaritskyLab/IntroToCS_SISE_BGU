class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return '[' + str(self.value) + ']'

class Linked_List:
    def __init__(self):
        self.head = None
        self.len = 0

    def __repr__(self):
        out = ''
        p = self.head
        while p != None:
            out += str(p) + '->'
            p = p.next
        return out

    def __len__(self):
        return self.len

    def add_at_start(self, val):
        p = Node(val)
        p.next = self.head
        self.head = p
        self.len += 1

    def insert(self, loc, val):
        if not (0 <= loc <= len(self)):
            print("Invalid location")
            return
        if loc == 0:
            self.add_at_start(val)
            return
        p = self.head
        for i in range(0, loc - 1):
            p = p.next
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1

    def delete(self, loc):
        if not (0 <= loc < len(self)):
            print("Invalid location")
            return
        if loc == 0:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(0, loc - 1):
                p = p.next
            p.next = p.next.next
        self.len -= 1

    def __getitem__(self, loc):
        if not (0 <= loc < len(self)):
            print("Invalid location")
            return
        p = self.head
        for i in range(0, loc):
            p = p.next
        return p

    # All next methods shows how we can use recursion to manipulate linked list easly

    # Append item recursively
    def append(self, val):
        def append_rec(node, val):
            if node.next is None:
                node.next = Node(val)
            else:
                append_rec(node.next, val)

        if self.head is None:
            self.head = Node(val)
            self.len += 1
        else:
            append_rec(self.head, val)
            self.len += 1


lnk = Linked_List()
lnk.add_at_start(6)
lnk.add_at_start(4)
lnk.add_at_start(3)
lnk.add_at_start(5)
lnk.insert(2, 10)
lnk.delete(2)
lnk.append(10)
print(len(lnk))
