s = 'Www.HackerRank.com'
result = 'this is a string'
line = 'this is a string'
#
#print(result)

result = [ i.lower() if i.isupper() else i.upper()  for i in s  ]



print('Welcome'.center(10, '-'))
a = line.split(' ')

print('-'.join(a))
string = "ABCDdCDC"
substr = "CDC"
l = list(substr)
j = 0 
occurance = 0 
print(string[0])
for i in range(0, len(string)):
    # print(string[i:len(l)])
    if string[i] == l[0]:
        if string[i:i+len(l)] ==substr:
            occurance +=1

string = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW \
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"

#Replace all ______ with rjust, ljust or center. 

thickness = 5    #This must be an odd number
c = 'H'

s = "bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd"
length = len(s)
max_width = 9
j = 0
while j<length:
   
    print(s[j:j+max_width])
    j +=max_width
    

s = 'hello world'


from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u,v):
        self.graph[u].append(v)
    def BFS(self, s):
        pass