#과제 25 과제노트 05번
keys = input().split()
values = list(map(int,input().split()))
a = dict(zip(keys, values))
print(a)

#과제 26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(park['english'])
print(park['science'])

#과제 27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
for subject in kim:
    kim[subject] = 100
print(kim)

#과제 28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
if 'english' in lee:
    del lee['english']
    print("'english' 과목을 삭제했습니다.")
else:
    print("'english' 키가 없습니다.")
print("삭제 후 lee =", lee)

#과제 29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
for subject, score in lim.items():
    print(subject, ":", score)

#과제 30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
high_scores = {subject: score for 
               subject, score in choi.items() if score >= 90}
print("90점 이상 과목의 키:", list(high_scores.keys()))

#과제 31
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
scores = list(y00.values())
if len(scores) == 0:
    print("딕셔너리에 과목이 없습니다.")
else:
    avg = len(scores)
    print("4과목의 평균", avg)