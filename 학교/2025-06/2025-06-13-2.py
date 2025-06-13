
bar = {"a":10 , "b" : 20 , "c" : 30}

# for key, item in bar.items():
#     print(f"item : {item}") 

# for key in bar.keys():
#     print(f"keys : {key}") 

for key , item in bar.items():
    print(f"item : {item} key: {key}") 

# # bar = {}
#
# # bar[0] = 10
# # bar["0"] = 20
# # bar[0.0] = 30
# # bar[True] = 40
# # bar[(1,2)] = 50
# # print(bar)

# bar = {
# "std1" : 10 , 
# "std2" : 20 ,
# "std3" : 30 ,
# }


# # keys = bar.keys()

# # print(bar.get("std4"))
# # print(bar.get("std1"))
# # print(bar.get("std5",False))
# # print(bar.get("std6","없쪄용~~"))


# print(bar.pop("std4","업쪄용~~~~~~~~~"))
# print(bar)


# # bar["std1"] = 30
# # bar[0] = 20


# # print(bar["std3"])

# # keys = bar.keys()



# # print(bar.setdefault("std4",200))
# # print(bar.setdefault("std1",100))


# # print(bar)