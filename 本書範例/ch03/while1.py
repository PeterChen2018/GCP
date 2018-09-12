total = person = score = 0
while(score != -1):
    person += 1
    score = int(input("請輸入第 %d 位學生的成績：" % person))
    total += score
average = total / person
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))