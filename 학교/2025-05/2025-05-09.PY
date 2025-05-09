
# bar = [50,10,30,40,20]


# for index in range(5):
#     print(bar[index], end="\n")
    

# bar[0] = 200
# bar[4] = 100

# print(bar)

# foo = [10, 20 ,30 ]    #리스트를 생성 , 요소는 0개 -> 빈 리스트 생성
# # pos = list()    #리스트를 생성 -> 빈 리스트 생성성
# # print(type(foo) , type(pos))

# # foo.append(10)
# # pos.append(20)

# # print(foo[0] , "\t" , pos[0])

# #갯수세기기
# print(len(foo)) 

# foo = [10,20,30,50]

# foo[2] = 100
# pos = foo[3]


# print(foo[2], "\t", pos)

foo = [10 , 20 ,30 ,50]
pos = foo
pos[3] = 200

print(foo[3])
print(id(pos) , id(foo))