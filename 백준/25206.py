grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

tot_credit = 0 # 누적 단위수(sum 단위수)
tot_score = 0 # 누적 성적(sum 단위수x성적)

for i in range(20):
    a = list(map(str, input().strip().split()))
    credit = float(a[1])
    if a[2] == "P":
        continue
    else:
        idx = grade_list.index(a[2])
        score = score_list[idx]
        tot_score += (credit*score)
        tot_credit += credit

avg_score = float(tot_score / tot_credit)
print(avg_score)