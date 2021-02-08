# start the loop from lenth(s) keep ignoring ' ' once it is not  ' ' keep increasing the counter until the s[i] runs into a space 
def lengthOfLastWord( s: str) -> int:
        i = len(s) -1
        count = 0
        while i>=0:
            if count !=0 and s[i] ==' ':
                return count
            if s[i] != ' ':
                count +=1
            i -=1
        return count
if __name__ =='__main__':
    print(lengthOfLastWord('Hello World'))