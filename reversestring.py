import stack as Stack

s  = Stack.Stack()
s.push('H')
s.push('U')
s.push('S')
s.push('S')
s.push('A')
s.push('I')
s.push('N')

for _ in range(0, s.size()):
    s.push(s.pop())

for _ in range(0, s.size()):
    print(s.pop(), end="")

