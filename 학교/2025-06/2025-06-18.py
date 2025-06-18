def input_student(students):
    student_num = int(input("학번 입력: "))
    if student_num in students.keys():
            print("이미 등록된 학번입니다")
            return
    student_name = input("이름을 입력해주세요: ")
    korean = int(input("국어 성적 입력: "))
    english = int(input("영어 성적 입력: "))
    math = int(input("수학 성적 입력: "))
        
    total = korean + english + math
    average = total / 3
        
    students[student_num] = {
        "name": student_name,
        "korean": korean,
        "english": english,
        "math": math,
        "total": total,
        "average": average
        }

def print_all_students(students):
    if students:
        print("[전체 학생 성적]")
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
        for student_num, info in students.items():
            print(f"{student_num}\t{info["name"]}\t{info["korean"]}\t{info["english"]}\t{info["math"]}\t{info["total"]}\t{info["average"]:.2f}")
    else:
        print("저장된 정보가 없습니다 ")

def search_student(students):
    search_student_num = int(input("조회할 학생 학번 입력: "))
        
    if students.get(search_student_num):

        print(f"""
        [학생정보]
        학번 : {search_student_num}
        이름 : {students[search_student_num]["name"]}
        국어 : {students[search_student_num]["korean"]}
        영어 : {students[search_student_num]["english"]}
        수학 : {students[search_student_num]["math"]}
        합계 : {students[search_student_num]["total"]}
        평균 : {students[search_student_num]["average"]}
        """)
    else:
        print("해당 학번의 정보가 없습니다.")


def delet_student(students):
    pop_student_num = int(input("조회할 학생 학번 입력: "))
        
    if pop_student_num in students:
        students.pop(pop_student_num)
        print("삭제 되엇습니다")
            
    else:
        print("해당 학번의 정보가 없습니다.")




students = {}


while True:
    print("""
----학생 성적 관리 프로그램 ----
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
""")
    
    user_input = int(input("메뉴 선택 (1~5): "))
    
    if user_input == 1:
        input_student(students)
    
    elif user_input == 2:
        print_all_students(students)
    
    elif user_input == 3:
        search_student(students)
            
            
    elif user_input == 4:
        delet_student(students)
        
    elif user_input == 5:
        print("프로그램을 종료합니다")
        break

    else:
        print("잘못된 입력입니다")