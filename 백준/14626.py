num = input()


total = 0
star_index = 0


for index , i in enumerate(num):
    if i == "*":
        if index % 2 == 0:
            star_index = 1
        else:
            star_index = 3
        continue
    
    if index % 2 == 0:
        n_1 = int(i) * 1
        total += n_1
    else:
        n_1 = int(i) * 3
        total += n_1 

for star in range(10):
    to_total = total + star * star_index
    if to_total % 10 == 0:
        print(star)
        break



# for star in range(10):
#     if total + (star * star_index) % 10 == 0:
#         print(star)
#         break