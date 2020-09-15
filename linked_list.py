class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

taylor_node = Node('Taylor', None)
rome_node = Node('Rome', taylor_node)

class LinkedList:
    def __init__(self):
        self.head = None
        self.head = None
        self.size = 0

    # returns len of list
    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return '[]'
        
        current = self.head
        # what we return once we've concatenated all the nodes to it
        result = str(current)

        while current.next:
            result += f' -> {str(current.next)}'
            current = current.next
        return f'[{result}]'
            

    # insert a new node at the front of the list
    def insert_front(self, data):
        if self.size == 0: # list is empty
            # create a new node and make it the head
            self.head = Node(data, None) 
            # set the tail to the same node
            self.tail = self.head
        elif self.size == 1:
            self.head = Node(data, self.tail)
        else:
            temp = self.head
            self.head = Node(data, temp)
        self.size += 1

    def insert_end(self, data):
        if self.size == 0:
            self.head = Node(data, None)
            self.tail = self.head
        # elif self.size == 1:
        #     self.tail = Node(data, None)
        #     self.head.next = self.tail
        else:
            temp = self.tail
            self.tail = Node(data, None)
            temp.next = self.tail
        self.size += 1

    def insert_after(self, data, node_data):
        # Make sure that Pete exists
        temp = None
        current = self.head 
        while current:
            if current.data == node_data:
                print('Found Pete')
                temp = current
                break
            current = current.next
        if temp == None:
            return "Check your node_data, we couldn't find node"
        
        # Find Pete node!
        # Create a new data Node
        new_node = Node(data, temp.next)
        # Set new data Node to Pete.next
        # Set Pete.next to the new Node
        temp.next = new_node


rome_list = LinkedList()
rome_list.insert_front('Adam')
rome_list.insert_front('Pete')
rome_list.insert_front('Taylor')

rome_list.insert_end('Dan')
rome_list.insert_end('Mads')

rome_list.insert_after('Jennifer', 'Taylor')

print(len(rome_list))
print(rome_list)

