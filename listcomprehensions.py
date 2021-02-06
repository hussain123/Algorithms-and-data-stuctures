city = ['karachi','hyderabad']

x, y, z = 1,1,1
n =2
test = [[i for i in range(x+2)], 
        [i for i in range(y+2)],
        [i for i in range(z+2)]]

l = []
l = [[c,d,f] for c in range(x+1) for d in range(y+1) for f in range(z+1) if c+d+f !=n]

print(l)



l = [57, 57, -57, 57]
max, secondMax = l[0], -2147483648
for i in l:

    if i > max :
        secondMax = max 
        max  = i 
    elif i>secondMax and i!= max:
        secondMax = i

#print(secondMax)


td = [['Harry', 20], ['Berry', 20], ['Tina', 19], ['Akriti', 21], ['Harsh', 19]]
sorted_list = sorted(td, key=lambda item:(item[1], item[0]),reverse=False)[0]
#print(sorted_list)
#second_highest = sorted(marksheet, key = lambda x: (x[1],x[0]))[1]
lsit = [i for i in sorted(td,  key=lambda item:(item[1], item[0]),reverse=False) if i[1]!=sorted_list[1]][0]
#print(lsit)
#[print(i[0]) for i in sorted(td) if i[1]==lsit[1]] 

student_marks = {}
student_marks['hussain'] = [101.00,200.00,300.00]

t = 0
t = sum(student_marks['hussain'])/len(student_marks['hussain'])
#print(t)
#print('{:0.2f}'.format(t))
N = int(input())
l =[]
i = 0 
while i < N:
    t = input().split()
    if t[0] =='insert':
        l.insert(int(t[1]),int(t[2]))
    elif t[0] =='print':
        print(l)
    elif t[0] =='remove':
        l.remove(int(t[1]))
    elif t[0] =='append':
        l.append(int(t[1]))
    elif t[0] =='sort':
        l.sort()
    elif t[0] =='pop':
        l.pop()
    elif t[0] =='reverse':
        l.reverse()

    i +=i

