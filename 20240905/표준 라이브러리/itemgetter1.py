from operator import itemgetter

students = [
    ("Jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("Sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(2))
print(result)

from operator import itemgetter

students = [
    {"name": "Jane", "age": 22, "grade": 'A'},
    {"name": "Dave", "age": 32, "grade": 'B'},
    {"name": "Sally", "age": 17, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)