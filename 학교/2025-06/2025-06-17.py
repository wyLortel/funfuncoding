# def calculate_average(*arg):
#     n = len(arg)
#     s= sum(arg)
#     avg = s/n
#     return n , s , avg

# n , s, avg = calculate_average(70,80,90,100,200)

# print(n,s,avg)

# def student_score(name,**kwarg):
#     print(f"{name}의 성적: ")
#     for k,v in kwarg.items():
#         print(f"{k}: {v}점")
    
#     print(f"총점:{sum(kwarg.values())}")

# student_score("우영", math=90 , engish=85 , scienece = 88)


# def add_number(*arg,**kawrgs):
#     keys = ["abs" , "only_even" , "unique"]
    
    
#     for key in kawrgs:
#         if key not in keys:
#             print("none")
#             return
    
#     lis = list(arg)
    
#     if kawrgs.get("abs" , False):
#         lis = [abs(i) for i in lis]
    
#     if kawrgs.get("only_even",False):
#         lis = [i for i in lis if i % 2 == 0]
    
#     if kawrgs.get("unique",False):
#         lis_2 = []
        
#         for i in lis:
#             if i not in lis_2:
#                 lis_2.append(i)
        
#         lis = lis_2
    
#     total = sum(lis)
    
#     print(f"{total}입니다")
    
#     return lis

# add_number(1,2,2,3,3,4,5 , round = True)


def generate_profile(name , age , *arg , gender="미정" , **kwargs):
    print(f"""
    [고객 프로필]
    이름 : {name}
    나이 : {age}
    성별 : {gender}
    """)
    
    if arg:
        print("관심사 : " , end="")
        for i in arg:
            print(f"{i}",end=" , ")
        print()
    
    if kwargs:
        print("추가 정보: " ,end=" ")
        for k,v in kwargs.items():
            print(f"{k}={v}" ,end=" ")

generate_profile("지민" , 26 , *["여행" , "사진" , "독서"], gender="여성", job = "디자이너" , country = "한국" )
        
        