class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next_node = next_

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head
        self.count = 0

    def push(self, value) -> None:
        node = Node(value)
        node.next_node = self.head
        self.head = node
        self.count += 1

    def __getitem__(self, index):
        curr = self.head
        ans = 0
        if index < self.count:
            while index >= 0:
                ans = curr.value
                curr = curr.next_node
                index -= 1
                return ans
        else:
            raise(IndexError)

    def pop(self):
        temp = self.head.next_node
        self.head = temp
        self.count -= 1

    def __len__(self):
        return self.count

    def __repr__(self) -> str:
        curr = self.head
        node_list = []
        while curr:
            node_list.append(str(curr.value))
            curr = curr.next_node
        return " ".join(node_list) + ' length: {}'.format(self.count)

if __name__ == "__main__":
    newlist = LinkedList()
    newlist.push(2)
    newlist.push(4)
    newlist.push(3)
    print(newlist)
    newlist.pop()
    print(newlist)
    print(newlist[2])
