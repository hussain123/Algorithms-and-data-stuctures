
def print_my_name(fname):
    print('my name is ',fname)        
def get_my_age():
    return 25
def empty_function():
    pass

print('123',' ')

year = 2100 
for i in range(0,10):
    print('1', sep='')



print('Welcome'.center(10, '-'))



def is_leap(year):
    leap = True
    
    # Write your logic here
    if year % 4 ==0:
        if year % 100 ==0 and year % 400 ==0:
            return True
        if year % 100 ==0:
            return False
        return True
    else:
        return False    
    return leap

#print("is leap =",is_leap(2400))

f = open("TeamsPremierLeague.txt", "r")
team = []
for x in f:
  team.append(x)

#print(team)
#print(3%7)
arr = [1,2,3,4,5]
d =2
i = 0
while i<d:
   k =  arr[0]
   j = 1
   while j < len(arr):
       arr[j-1] = arr[j]
       j += 1 
   arr[j-1] = k
   i += 1
#print(arr)
for i in range(1,4):
    i 
stack = [
]
#print( stack)
is_balanced = True
s = r'(('
b_close = ')}]'
b_open = '({['
for i in (range(0, len(s))):
    if s[i] in  b_open:
        stack.append(s[i])
    elif s[i] in  b_close:
        r = stack.pop()
        if s[i] == '}' and r != '{':
            is_balanced = False
            break
        elif s[i] == ']' and r != '[':
            is_balanced = False
            break
        elif s[i] == ')' and r != '(':
            is_balanced = False
            break
        else:
            pass

print(is_balanced)

roman_key = {
            'I': 1,
            'V': 5,
            'X' : 10,
             'L': 50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':50,
            'XC':90,
            'CD':400,
            'CM':900
}
number = 0
i = 0
while i< len(s):
    if  s[i:i+2]  in roman_key:
        
        number += roman_key[s[i:i+2]]
        i +=2
    else:
        
        #number += roman_key[s[i]]
        i +=1

number = 27
int_to_roman ={
             '1':'I',
             '2':'II',
             '3':'III',
             '6':'VI',
             '7':'VII',
             '8':'VIII',
            '5': 'V',
            '10' : 'X',
            '50': 'L',
            '100':'C',
            '500':'D',
            '1000':'M',
            '4':'IV',
            '9':'IX',
            '50':'XL',
            '90':'XC',
            '400':'CD',
            '900':'CM'
}

strs = ["zonka","zonking",'zoning']
prefix =''
s = strs[0]
i = 0
matched = False
while i < len(s):
    for j in range(1, len(strs)):
        
        if  i < len(strs[j]) and s[i] == strs[j][i]:
            matched = True
        else:
            matched = False
            
    if matched:
        prefix += s[i]
    else:
        break
    
    i += 1   


class Person:
    name = "hussain"
    age = 25

