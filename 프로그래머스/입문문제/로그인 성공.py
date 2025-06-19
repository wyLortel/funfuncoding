def solution(id_pw, db):
    answer = ''
    for i in db:
        if i == id_pw:
            answer = "login"
            break
        elif i[0] == id_pw[0]:
            answer = "wrong pw"
            break
        else:
            answer = "fail"
        
    return answer



id_lis = ["rabbit04", "98761"]

db_lis = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]



print(solution(id_lis,db_lis))