bar = [val for val in range(1,11,2)]
print(bar)


for va in range(2,11,2):
    print(va, end="\t")

print(bar[2:11:2])
print(bar[0:5:1])
print(bar[0:])
print(bar[2:])
print(bar[2:4])
print(bar[2:3])
print(bar[2:-1])