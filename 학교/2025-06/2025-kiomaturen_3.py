def main():
    print("""
==== 학생 성적 관리 프로그램 ====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
""")



def input_student(students):
    student_num = int(input("학번 입력"))    
    if student_num in students:
        print("이미 등록된 학번입니다")
        return
    name = input("이름 입력: ")
    korean = int(input("국어 성적: "))
    english = int(input("영어 성적: "))
    math = int(input("수학 성적: "))
        
    students[student_num] = {
        "name" : name ,
        "korean" : korean ,
        "english" : english ,
        "math" : math ,
        "total" : korean + math + english ,
        "average" :  (korean + math + english) / 3
        }
    print("성적이 저장 되엇습니다")
    print()


def print_all_students(students):
    if students:
        print("[ 전체 학생 성적 ]")
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
        
        for k , v in students.items():
            print(k , end="\t")
            for info in v.values():
                print(info , end="\t")
            print()
    else:
        print("저장된 학생 정보가 없습니다")


def search_students(students):
    search_student_num = int(input("조회할 학번 입력"))
        
    if search_student_num in students:
        search_student_info = students[search_student_num]
        print(f"[ 학생 정보 ]\n학번: {search_student_num}")
        for key , value in search_student_info.items():
            print(f"{key}: {value}") 
    else:
        print("해당 학번의 학생 정보가 없습니다")

def delete_students(students):
    pop_student_num = int(input("삭제할 학번 입력: "))
        
    if pop_student_num in students:
        students.pop(pop_student_num)
        print("학생 정보가 삭제되엇습니다")
        
    else:
        print("해당 학번의 학생 정보가 없습니다")




students = {}

while True:
    main()
    user_input = int(input("메뉴 선택 (1~5): "))
    
    #1번
    if user_input == 1:
        input_student(students)
    
    #2번
    elif user_input == 2:
        print_all_students(students)
        
    #3번
    elif user_input == 3:
        search_students(students)
    
    #4번
    elif user_input == 4:
        delete_students(students)
        
    #5번
    elif user_input == 5:
        print("프로그램을 종료합니다")
        break
    
    
    else:
        print("잘못된 입력입니다")
    
        
                
    