students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, history=10)),
    dict(id=2, credits=dict(math=8, physics=9, history=10)),
    dict(id=3, credits=dict(math=5, physics=5, history=7)),
]

def decorate(student):
    return (sum(student['credits'].values()), student)

def undecorate(decorated_student):
    return decorated_student[1]


students = sorted(map(decorate, students), reverse=True)
students = list(map(undecorate, students))
print(students)

