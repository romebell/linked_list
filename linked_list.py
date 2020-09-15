class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

taylor_node = Node('Taylor', None)
rome_node = Node('Rome', taylor_node)

