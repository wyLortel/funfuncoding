N = int(input())
co_count = 0

for _ in range(N):
    word = input()
    used = []
    word_1 = ""
    
    for i in word:
        if i in used and word_1 != i:
            break
        used.append(i)
        word_1 = i
    else:
        co_count += 1


print(co_count)