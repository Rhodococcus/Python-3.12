money = True
if money:
    print("택시를")
    print("타고")
    print("가라")

for i in range(10):
    print(i, end='')

f = open("새파일.txt", 'w')
f.close()

f = open("C:/work/복습.txt", 'w')
f.close()

f = open("C:/work/복습.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
    

