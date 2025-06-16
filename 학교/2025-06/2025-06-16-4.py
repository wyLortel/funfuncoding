def generate_profile(name, age, *interests, gender="미정", **method):
    print(f"""
    출력 :
    [고객 프로필]
    이름 : {name}
    나이 : {age}
    성별: {gender}
    """)
    if interests:
        print(f"관심사: {interests}")
    
    if method:
        print(f"추가 정보:")

generate_profile("홍길동", 30, *["여행", "사진"], gender="여성",)
