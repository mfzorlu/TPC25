"""A, N = list(map(int, input().split()))
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

A, N = map(int, input().split())
text = input()
find = input()

def delete_find(text, find):
    while True:
        new_text = "".join(text.split(find))
        if new_text == text:
            return len(new_text)
        
        text = new_text

print(delete_find(text, find))"""

A, N = map(int, input().split())
text = input()
find = input()

def delete_find(text, find, N):
    last = []

    for ch in text:
        last.append(ch)

        if "".join(last[-N:]) == find:
            del last[-N:]

    return len(last)

print(delete_find(text, find, N))

