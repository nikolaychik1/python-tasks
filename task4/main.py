# В олимпиаде участвовало N человек. Каждый получил определенное количество баллов,
# при этом оказалось,
# что у всех участников разное число баллов.
# Упорядочите список участников олимпиады в порядке убывания набранных баллов.
class Pupil:
    lastname = ''
    score = 0


i = int(input())
listpupil = []
for j in range(i):
    data = list(input().split())
    student = Pupil()
    student.lastname = data[0]
    student.score = int(data[1])
    listpupil.append(student)
listpupil.sort(key=lambda x: -x.score)
for student in listpupil:
    print(student.lastname)
