# scores = [90, 25, 67, 45, 80]
# student_number = 0
# total = 0
# average = 0

# for score in scores:
# 	student_number += 1
# 	if score >= 60:
# 		print("%d번 학생은 합격입니다." % student_number)
# 		total += score
# 	else:
# 		print("%d번 학생은 불합격입니다." % student_number)

# average = total / student_number
# print("총점은 %d, 평균은 %f입니다." % (total, average))

py_score = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
student_number = 0
total = 0
average = 0
for score in py_score:
    student_number +=1
    if score>=60:
        #print("%d번 학생은 합격입니다." % student_number)
        total += score
    else:
        pass
passstudent = 0
for score in py_score:
    passstudent +=1
    if score>=60:
        total += score

average = total / passstudent
print("평균은 %f 입니다." %(average))