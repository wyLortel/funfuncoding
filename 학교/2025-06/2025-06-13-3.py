attendance = {
    "우영": 3,
    "민지": 5,
    "준호": 4,
    "하늘": 2,
    "도윤": 5
}

attendance["하늘"] = 3
attendance.setdefault("윤서",1)

kakusei = []

for i in attendance:
    if attendance[i] == 5:
        kakusei.append(i)

print(kakusei)
print(attendance)