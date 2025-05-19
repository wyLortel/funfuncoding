bar = [val for val in range(1,11,2)]


foo = list(bar)
pos = bar.copy()
kin = bar[:]

bar[0] = 100

print(bar)
print(foo)
print(pos)
print(kin)

print(id(bar))
print(id(foo))
print(id(pos))
print(id(kin))
