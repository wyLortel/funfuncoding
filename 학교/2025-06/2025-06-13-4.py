words = "apple banana orange apple kiwi apple apple"

words = list(words)

print(words)

s = ""
new_list = []
for i in words:
    if i == " ":
        new_list.append(s)
        s = ""
        continue
    s += i
    
if s:
    new_list.append(s)

print(new_list)

msg = input("찾을 문자열을 입력하세요")

count = 0
index_list = []

for index, k in enumerate(new_list):
    if k == msg:
        count += 1
        index_list.append(index)

print(f"{msg}은 총 {count}번 등장합니다")
print(f"위치 (인덱스) : {index_list}")