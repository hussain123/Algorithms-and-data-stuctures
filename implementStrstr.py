def Solution( haystack: str, needle: str) -> int:
    i = 0 
    count = len(needle)
    while count <= len(haystack):
        temp = haystack[i:count]
        if temp == needle:
            return i
        i +=1
        count +=1
    return -1
if __name__ =='__main__':
    print(Solution('hello', 'll'))
    print(Solution('aaaa', 'ab'))
    print(Solution('aaaa', 'a'))
    print(Solution('aaaa', ''))
    print(Solution("mississipi","issipi"))
    print(Solution("mississippi","pi"))
    print(Solution("mississippi","sipp"))
    print(Solution("babbbbbabb","bbab"))
    print(Solution("baabbaaaaaaabbaaaaabbabbababaabbabbbbbabbabbbbbbabababaabbbbbaaabbbbabaababababbbaabbbbaaabbaababbbaabaabbabbaaaabababaaabbabbababbabbaaabbbbabbbbabbabbaabbbaa","bbaaaababa"))