text = input().lower()

word ={}


for i in text:
    word[i] = word.get(i,0) + 1
    
max = 0

for key, value in word.items():
    if max <= value:
        max = value


max_with_value = [k for k, v in word.items() if v == max]

if len(max_with_value) >= 2:
    print("?")
else:
    print(max_with_value[0].upper())


