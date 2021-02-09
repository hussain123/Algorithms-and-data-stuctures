def reverse_a_string(s):
    new_string = ""
    i = len(s)-1
    for i in s:
        new_string =i + new_string 
        print(new_string)
    print(new_string)
    return new_string
    
if __name__ == "__main__":
    assert reverse_a_string('Hussain') == "niassuH"