class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

pilha = Stack()

pilha.push('PRATO 1')
pilha.push('PRATO 2')
pilha.push('PRATO 3')
pilha.push('PRATO 4')
pilha.push('PRATO 5')
pilha.push('PRATO 6')

print(pilha.items)
print(pilha.peek())
print(pilha.items)

pilha.pop()
print(pilha.items)
