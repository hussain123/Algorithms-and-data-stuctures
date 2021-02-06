import cmath
import regex as re

r = complex('1+2j')
print(*cmath.polar(complex('1+2j')),sep='\n')
# N = 7
# M  = N*3

# dots = ".|."
# # print top layer
# for i in range(0,N//2): 
#   #  print(((dots*i)+ dots + (dots*i)).center(M,'-'))


# #print('Welcome'.center(M,'-'))

# # print bottom layer
# for i in range(0,N//2): 
#  #   print(((dots* (N//2-1-i))+dots+(dots* (N//2-1-i))).center(M,'-'))


# 
l = ['1.414','+.5486468','0.5.0'
,'1+1.0'
,'0']
for i in l:
    try:
      
      print(isinstance(i, float))
    except:
        print(False)

n = 2
b_len = len("{0:b}".format(n))
width_d = 1
for i   in range(1,n+1):
    # b_len = len(str(i))
    print("{0:>{width_d}d}{0:>{width}o}{0:>{width}X}{0:>{width}b} ".format(i, width=b_len, width_d = width_d))


class hash_set:
    def __init__(self):
        self.size  = 1000
        self.s = []
    def add(self,key):
      hash_key = self.generate_hash(key)
      if key not in self.s:
          self.s[hash_key].append(key)
    def generate_hash(self,key):
        return key % self.size


class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data
        
    def get_next(self):
        return self.next
    def set_next(self,new_next):
        self.next = new_next

class SLL:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    def add_front(self, new_data):
        node = Node(new_data)
        if self.is_empty():
            node.next = None
            self.head = node
        else:   
            node.next = self.head
            self.head = node
    def size(self):
        return len(self.head)
    def search(self,data):
        pass
    def remove(self,data):
        pass
    def traverse(self):
        pass


l = SLL()
l.add_front('hussian')
l.add_front('aqsa')
print(l.head.data)