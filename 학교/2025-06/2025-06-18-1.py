def input_student(students):
    try:
        student_num = int(input("학번 입력: "))
    except ValueError:
        print("숫자로 입력해주세요.")
        return

    if student_num in students:
        print("이미 등록된 학번입니다.")
        return

    student_name = input("이름을 입력해주세요: ")
    
    try:
        korean = int(input("국어 성적 입력: "))
        english = int(input("영어 성적 입력: "))
        math = int(input("수학 성적 입력: "))
    except ValueError:
        print("성적은 숫자로 입력해주세요.")
        return

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
    print(f"{student_name} 학생 정보가 등록되었습니다.")


def print_all_students(students):
    if not students:
        print("저장된 정보가 없습니다.")
        return

    print("\n[전체 학생 성적]")
    print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
    for num, info in students.items():
        print(f"{num}\t{info['name']}\t{info['korean']}\t{info['english']}\t{info['math']}\t{info['total']}\t{info['average']:.2f}")


def search_student(students):
    try:
        num = int(input("조회할 학생 학번 입력: "))
    except ValueError:
        print("숫자로 입력해주세요.")
        return

    student = students.get(num)
    if student:
        print(f"""
[학생 정보]
학번 : {num}
이름 : {student['name']}
국어 : {student['korean']}
영어 : {student['english']}
수학 : {student['math']}
합계 : {student['total']}
평균 : {student['average']:.2f}
""")
    else:
        print("해당 학번의 정보가 없습니다.")


def delete_student(students):
    try:
        num = int(input("삭제할 학생 학번 입력: "))
    except ValueError:
        print("숫자로 입력해주세요.")
        return

    if num in students:
        del students[num]
        print("학생 정보가 삭제되었습니다.")
    else:
        print("해당 학번의 정보가 없습니다.")


def main():
    students = {}

    while True:
        print("""
---- 학생 성적 관리 프로그램 ----
1. 학생 성적 입력
2. 전체 성적 출력
3. 개별 성적 조회
4. 학생 정보 삭제
5. 종료
""")
        try:
            choice = int(input("메뉴 선택 (1~5): "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if choice == 1:
            input_student(students)
        elif choice == 2:
            print_all_students(students)
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            delete_student(students)
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~5 사이 숫자를 선택해주세요.")


if __name__ == "__main__":
    main()
