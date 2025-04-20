text = input("문자열 입력")
word = input("단어 입력")

current_word = ''
count = 0

for char in text:
    current_word += char  
    
    if current_word == word:
        count = count + 1
    current_word = ''  

if current_word == word:
    count = count + 1

print(f"단어 {word}의 출현 빈도: {count}")

