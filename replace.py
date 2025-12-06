A, N = list(map(int, input().split()))
text = input()
find = input()

def delete_find(text, find):
    flag = 1
    while flag == 1:
        text = text.replace(find, "") # w3 python string functions
        if find in text:
            pass
        else:
            flag = 0
    
    return len(text)
    
print(delete_find(text, find))
