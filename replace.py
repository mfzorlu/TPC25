A, N = list(map(int, input().split()))
text = input()
find = input()
flag = 1

def delete_find():
    while flag == 1:
        text = text.replace(find, "") # w3 python string functions
        if find in text:
            pass
        else:
            flag = 0
    
    return len(text)
    

