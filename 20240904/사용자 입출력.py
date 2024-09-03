f = open("C:/work/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f = open("C:/work/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("C:/work/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("C:/work/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("C:/work/새파일.txt", 'r')
data = f.read()
print(data)
f.close

f = open("C:/work/새파일.txt", 'r')
for line in f:
    print(line)
f.close

f = open("C:/work/새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close

with open("C:/work/복습.txt", 'w') as f:
    f.write("Life is too short, you need python")
