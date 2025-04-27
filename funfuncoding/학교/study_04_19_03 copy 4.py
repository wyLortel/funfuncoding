text = input("문자열 입력")
word = input("단어 입력")

current_word = ''
count = 0

for char in text:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
        current_word += char
    else:
        if current_word == word:
            count = count + 1
        current_word = ''  

if current_word == word:
    count = count + 1

print(f"단어 {word}의 출현 빈도: {count}")

