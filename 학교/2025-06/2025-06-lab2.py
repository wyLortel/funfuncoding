def main():
    print(""""
    === 학생 성적 관리 프로그램 ===
    1. 학생 성적 입력
    2. 학생 성적 출력
    3. 학생 성적 확인
    4. 학생 성적 삭제
    5. 종료
    """)



def input_student(students):
        student_num = int(input("학번입력: "))
        if student_num in students:
            print("이미 등록된 학번입니다")
            return
        name = input("이름 입력: ")
        korean = int(input("국어 성적 입력: "))
        english = int(input("영어 성적 입력: "))
        math = int(input("수학 성적 입력: "))
                
        students[student_num] = {
            "이름" : name ,
            "국어" : korean ,
            "영어" : english ,
            "수학" : math ,
            "총점" : korean + math + english,
            "평균" : (korean + math + english) / 3 ,
        }
        
        print("성적이 저장되엇습니다")
        


def print_all_students(students):
    if not students:
        print("등록된 정보가 없습니다")
        return
            
    print("[ 전체 학생 관리 ]")
    print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
    for k,v in students.items():
        print(f"{k}" , end="\t")
        for info in v.values():
            print(f"{info}" , end="\t")
        print()

def search_student(students):
    search_student = int(input("조회할 학번 입력"))
        
    if search_student not in students:
        print("해당 학번의 정보가 없습니다")
        return
        
    search_info = students[search_student]
    print("[학생 정보]")
    print(f"학번 : {search_student}")
    for key , value in search_info.items():
        print(f"{key} : {value}")

def delete_student(students):
    pop_student = int(input("삭제할 학번 입력"))
        
    if pop_student not in students:
        print("해당 학번의 정보가 없습니다")
        return
        
    students.pop(pop_student)
    print("학생정보가 삭제되엇습니다")



students = {}
    
while True:
    main()
        
    input_user_num = int(input("메뉴선택( 1 ~ 5 )"))
        
    if input_user_num == 1:
        input_student(students)
        
    elif input_user_num == 2:
        print_all_students(students)
    
    elif input_user_num == 3:
        search_student(students)
    
    elif input_user_num == 4:
        delete_student(students)
        
    elif input_user_num == 5:
        print("프로그램을 종료합니다")
        break
    else:
        print("잘못된 입력입니다")
        
    
    