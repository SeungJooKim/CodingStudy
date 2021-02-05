# 기초 출력하기
# /n 줄바꿈, /t은 줄 탭, \\는 \ 자체 출력
print("hi hello\n")
print("nice to meet you\r")
print("1\\21")

# 윈도우 운영체제의 파일 경로 출력
path = "C:\download\hello.cpp"
# c:\download\hello.cpp 사용자가 입력
path.replace('\\', '\\\\')
print(path)

# 1008 유니코드 특수문자 출력 \u
print("\u250C\u252C\u2510\n")

# 1010 입출력
name = input("이름을 입력하세요")
print("이름: {0}, type :{1}".format(name, type(name)))

age = int(input("나이를 입력하세요"))
# age=map(int,input("나이를 입력하세요").split) map 형식으로 저장
print(age)

# 1015 실수 자리수 맞춰 출력
weight = float(input("몸무게를 입력하세요"))
print(weight)
print(round(weight, 2))

# 1017 같은 변수 반복 출력
print("{0} {1} {2}".format(name, name, name))

# 형식 지정 출력
print('Today is %d %s.' % (3, 'April'))

# 자리 지정 출력
print('이름:{0:<10}이며 나이는 {1}세입니다.'.format('박은정', 24))  # 왼쪽 정렬
print('이름:{0:>10}이며 나이는 {1}세입니다.'.format('박은정', 24))  # 오른쪽 정렬

# 특정 문자 제거
"asdfhelloasfasdf".replace("hello", " ")

# 1020
x, y = input("주민번호를 입력하세요").split('-')
print(x, y, sep='', end='/')  # x,y/
print(x, y, end='')  # x,y다음줄의것

# 1021
str1 = input()
print(str1)

# 1023 실수 정수 부분과 실수 부분으로 나누어 출력
x = input("실수를 입력하세요").split('.')
print("정수부분 : ", x[0])
print("실수부분 : ", x[1])

# 1024 한 글자씩 분리
x = input("단어를 입력하세요")
for i in range(len(x)):
    print("'", x[i], "'", end='\n')

# 1025 5자리 정수를 각 자리별로 나누어 출력
x1, x2, x3, x4, x5 = map(int, input("5자리 정수를 입력하세요"))
print('[' + str(x1) + '0000]\n')
print('[' + str(x2) + '000]\n')
print('[' + str(x3) + '00]\n')
print('[' + str(x4) + '0]\n')
print('[' + str(x5) + '\n')

import math

i = 3.52
math.ceil(i)  # 올림
math.floor(i)  # 내림
math.trunc(i)  # 버림

# re모듈 , match
import re

p = re.compile('[a-z]+')
m = p.match("python")
# m.group match 된 것을 string으로 반환
print(m.group())

# 1026 시분초에서 분만 출력
time = input("시간을 입력하세요: ")
print(time.split(':')[1] + "분 입니다.")

# 1027 년월일 출력 형식 변경
date = input("년월일을 입력하세요 (yyyy.mm.dd)")
print('{0}-{1}-{2}'.format(date.split('.')[0], date.split('.')[1], date.split('.')[2]))

print('Today is %s - %s - %s.' % (date.split('.')[0], date.split('.')[1], date.split('.')[2]))

# 8진수로 입력받기
a = int(input(), 8)  # 8진수로 입력받음
print(a)

# 8진수,16진수로 출력하기
i = 31
print('%o' % (i))
print('%x' % (i))

# 1038 정수 2개 입력받아 더하기
input = input("정수 두개를 입력하세요: ")
input = input.split(" ")

if (len(input) != 2):
    print("error")
else:
    print(int(input[0]) + int(input[1]))

a, b = map(int, input().split())
print(a + b)

# 1040 부호 바꾸어 출력하기
a = int(input("정수를 입력하세요"))
print(a * -1)

# 1041 다음 영문자 출력하기
a = str(input("영문자 하나를 입력하세요"))

# ord() 아스키코드로 변환
a = ord(a) + 1

if (a < 65 or 90 < a < 97 or a > 123):
    print("영문자를 입력하세요")
else:
    if (a == 91 or a == 123):
        print("z는 마지막 영문자 입니다.")
    else:
        print(chr(a))

# 1042 정수 2개 입력받아 나눈 몫 출력
a = input("정수 2개를 입력하세요 : ").split()
print(int(a[0]) / int(a[1]))

a, b = map(int, input().split())
print(a // b)
# c언어는 /가 몫

# 1043 정수 2개를 입력받아 나눈 나머지 출력하기
print(a % b)

# 1049 기초 비교 연산
a, b = map(int, input("두 정수를 입력하세요 : ").split())

if a > b:
    print("1")
else:
    print("0")

# 1050 기초 비교 연산
a, b = map(int, input("두 정수를 입력하세요 : ").split())
if a == b:
    print("1")
else:
    print("0")

# 1051 기초 비교 연산
a, b = map(int, input("두 정수를 입력하세요 : ").split())
if a <= b:
    print("1")
else:
    print("0")

# 1052
a, b = map(int, input("두 정수를 입력하세요 : ").split())
if a != b:
    print("1")
else:
    print("0")

# 1053 논리연산
ans = int(input())
if ans == 1:
    print(0)
else:
    print(1)

# 1054 논리연산
a, b = map(int, input("참 거짓 중 두 개를 입력하세요").split())
if a == 1 and b == 1:
    print("true")

# 1055 논리연산
a, b = map(int, input("참 거짓 중 두 개를 입력하세요").split())
if a == 1 or b == 1:
    print("true")

# 1059 비트단위논리연산 not
a = int(input("정수를 입력하세요"))
print(~a)

# 1060 비트단위논리연산 and
a, b = map(int, input("두 개의 정수를 입력하세요").split())
print(a & b)

# 1061 비트단위논리연산 or
a, b = map(int, input("두 개의 정수를 입력하세요").split())
print(a | b)

# 1062 비트단위논리연산 xor
# xor 배타적 논리합 => 서로 다를 때 1
# 그래픽 처리에 효과적으로 사용 ex. 두 장의 이미지가 겹쳤을 때 서로 다른 부분만 처리가능
a, b = map(int, input("두 개의 정수를 입력하세요").split())
print(a ^ b)

# 1063 삼항 연산
a, b = map(int, input("두 개의 정수를 입력하세요").split())
print(a if a > b else b)

# 1064 삼항 연산
a, b, c = map(int, input("세 개의 정수를 입력하세요").split())
x = (a if (a < b) else b)
print(x if x < c else c)

# 1065 짝수만 출력
a, b, c = map(int, input("세 개의 정수를 입력하세요").split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 1070 계절 출력
# 파이썬 switch 문 없음
a = int(input("월을 입력하세요: "))
if a in (12, 1, 2):
    print("winter")
elif a in (3, 4, 5):
    print("spring")
elif a in (6, 7, 8):
    print("summer")
else:
    print("fall")

# 1071
a = input().split()
for x in a:
    if int(x) == 0:
        break
    else:
        print(x)

# 1072 반복 출력
a = int(input())
b = input().split()
for i in b:
    print(i)

# 1073 while문

a = input().split()
i = 0
x = int(a[i])
while x != 0 and i < len(a):
    x = int(a[i])
    print(x)
    i = i + 1

a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] == 0:
        break
    print(a[i])

# 1074 while문
a = int(input("정수를 입력"))
while (a != 0):
    print(a)
    a = a - 1

# 1097
baduk = []
for i in range(20):
    baduk.append([])
    for j in range(20):
        baduk[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        baduk[i + 1][j + 1] = int(a[i])

n = int(input("개수를 입력하세요: "))

for i in range(n):
    x, y = input().split()
    for j in range(1, 20):
        if baduk[int(x)][j] == 0:
            baduk[int(x)][j] = 1
        else:
            baduk[int(x)][j] = 1

        if baduk[j][int(y)] == 0:
            baduk[j][int(y)] = 1
        else:
            baduk[j][int(y)] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(baduk[i][j], end='')
    print()

# 1098
h, w = map(int, input().split())
sugar = [[0] * (w + 1) for i in range(h + 1)]
# 좌표 입력이 1부터 시작이므로 +1
n = int(input())

for k in range(n):  # 입력 개수 만큼
    l, d, x, y = map(int, input().split())
    if (x > h or y > w):
        print("좌표 범위 이탈\n")
        break
    for i in range(l):
        if d == 0:
            sugar[x][y + i] = 1
        elif d == 1:
            sugar[x + i][y] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(sugar[i][j], end='')
    print()

# 1099
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

m = 1
n = 1

while (maze[m][n] != 2):
    maze[m][n] = 9
    if (maze[m][n + 1] == 1 and maze[m + 1][n] == 1) or (m == 9 and n == 9):
        break
    elif (maze[m][n + 1] == 0):
        n = n + 1
    elif (maze[m][n + 1] == 1):
        m = m + 1
maze[m][n] = 9

for i in range(len(maze)):
    for j in range(len(maze)):
        print(maze[i][j], end='')
    print()

# 1099-2
maze = [[0] * 10 for i in range(10)]
for i in range(10):
    templine = list(map(int, input().split()))
    for j in range(10):
        maze[i][j] = templine[j]

i = 1
j = 1

while True:

    if i >= 9 or j >= 9:
        break
    elif maze[i][j] == 2:  # eat
        maze[i][j] = 9
        break
    else:
        maze[i][j] = 9
        if j + 1 < 10 and maze[i][j + 1] != 1:
            j += 1
        elif j + 1 < 10 and maze[i][j + 1] == 1:
            if i + 1 < 10 and maze[i + 1][j] != 1:
                i += 1
            else:
                break
        else:
            None

for i in range(10):
    for j in range(10):
        print(maze[i][j], end=" ")
    print(" ")

# 1204 순위 출력
n = int(input())
if n % 10 in (1, 2, 3):
    if n // 10 == 1:
        print(f"{n}th")
    else:
        if n % 10 == 1:
            print(f"{n}st")
        elif n % 10 == 2:
            print(f"{n}nd")
        else:
            print(f"{n}rd")
else:
    print(f"{n}th")

# 1205
oper = ['+', '-', '/', '*', '**']
n1, n2 = input().split()
data = [eval(n1 + oper[i] + n2) for i in range(len(oper))]
for i in range(len(oper)):
    data.append(eval(n2 + oper[i] + n1))
print("%f\n" % (max(data)))

# 1205
a, b = map(int, input().split())
maxi = 0
maxi = max([a + b, a - b, b - a, a * b, a / b, b / a, a ** b, b ** a])
print("%.6f" % maxi)

# 1210
calori = [400, 340, 170, 100, 70]
menu1, menu2 = map(int, input().split())
sumi = calori[menu1 - 1] + calori[menu2 - 1]
if sumi > 500:
    print("angry")
else:
    print("no angry")

# 1222
time, one, two = map(int, input().split())
while True:
    if time >= 90:
        break
    one += 1
    time += 5
if one > two:
    print("win")
elif one == two:
    print("same")
else:
    print("lose")

# 1226
lotto = list(map(int, input().split()))
num = list(map(int, input().split()))
bonusnum = lotto[6]
bonusmatch = False
del lotto[6]
matchnum = 0
lotto.sort()
num.sort()

for lottonum in lotto:
    for inputnum in num:
        if (lottonum == inputnum):
            matchnum += 1

if (matchnum == 6):
    print("1등 \n")
elif (matchnum == 5):
    for i in inputnum:
        if (inputnum == bonusnum):
            bonusmatch = True
            print("2등 \n")
            break
        else:
            bonusmatch = False

    if bonusmatch == False:
        print("3등\n")

elif (matchnum == 4):
    print("4등\n")
elif (matchnum == 3):
    print("3등 \n")
else:
    print("no")

# 1228
height, weight = map(float, input().split())
avgweight = (height - 100) * 0.9
biman = (weight - avgweight) * 100 / avgweight

if biman > 20:
    print("비만\n")
elif biman > 10:
    print("과체중 \n")
else:
    print("정상\n")

# 1231
exp = input()
num1 = 0
num2 = 0
cal = []

for i in range(len(exp)):
    if (exp[i] == '+' or exp[i] == '-' or exp[i] == '/' or exp[i] == '*'):
        num1 = int(exp[0:i])
        num2 = int(exp[i + 1:len(exp)])
        cal = exp[i]
        if (exp[i] == '+'):
            result = num1 + num2
        elif (exp[i] == '-'):
            result = num1 - num2
        elif (exp[i] == '*'):
            result = num1 * num2
        else:
            result = num1 / num2
print(result)

# 1253
a, b = input().split()
a = int(a)
b = int(b)

if (a > b):
    for i in range(b, a + 1):
        print(i, end='')
else:
    for i in range(a, b + 1):
        print(i, end='')

    # 1255
a, b = input().split()
a = float(a)
b = float(b)

while (a <= b):
    print(round(a, 2))
    a += 0.01

# 1283
a = int(input())
b = int(input())

changes = list(map(int, input().split()))
result = a

for change in changes:
    if change < 0:
        result = result - (result * (change * -1 / 100))
    else:
        result = result + (result * (change / 100))

print(round(result - a))

if (result - a) == 0:
    print('same')
elif (result - a > 0):
    print('good')
else:
    print('bad')

# 1284
import math

n = int(input())
a = []
index = 0
sq = int(math.sqrt(float(n)))
print(sq)

for i in range(0, 30):
    a.append(0)

for i in range(2, sq + 1):
    while n % i == 0:
        n /= i
        a[index] = i
        index += 1

if n != 1:
    a[index] = n
    index += 1
if index == 2:
    print(int(a[0]), int(a[1]))
else:
    print('wrong number')

# 1273 약수 구하기

N = int(input())
yak = []
# 루트? 1 2 3 4 6 12  12의 루트는 3.xxx
for i in range(1, math.trunc(math.sqrt(N)) + 1, 1):  # a<root<b a+1 // 1,2,3
    if N % i == 0:
        yak.append(i)
        yak.append(N // i)

yak = list(set(yak))  # 중복제거위해
yak.sort()
for i in yak:
    print(i, end=" ")

# 1274 : 소수판별 알고리즘
import math

N = int(input())
yak = []
for i in range(1, math.trunc(math.sqrt(N)) + 1, 1):  # a<root<b a+1
    if N % i == 0:
        yak.append(i)
        yak.append(N // i)
yak = list(set(yak))
if len(yak) == 2:
    print("prime")
else:
    print("not prime")

# 1382
for j in range(1, 10, 1):
    for i in range(2, 6, 1):
        print("%2d x %2d = %2d" % (i, j, i * j), end='')
        if i == 5:
            print('', end='')
        else:
            print('\t', end='')
    print()

# 1368
h, k, d = input().split()
h = int(h)
k = int(k)
if d == 'L':
    for i in range(h):
        if i == h - 1:
            print(' ' * i + '*' * k, end='')
        else:
            print(' ' * i + '*' * k)
else:
    for i in range(h):
        if i == h - 1:
            print(' ' * (k - i) + '*' * k + ' ' * i, end='')
        else:
            print(' ' * (k - i) + '*' * k + ' ' * i)

# 1675
code = range(ord('a'), ord('z') + 1, 1)
encode = dict()
for i in range(0, 26, 1):
    encode[chr(code[i - 3])] = chr(code[i])
strstr = input()

for i in strstr:
    if i != ' ':
        print(encode[i], end="")
    else:
        print(i, end="")

# 1420
n = int(input())
record = {}  # dict

for i in range(0, n):
    name, score = input().split()
    record[name] = int(score)

record = sorted(record.items(), reverse=True)
print(record[2][0])

# 1461
n = int(input())
# baeyal = [[0 for col in range(n)] for row in range(n)]
baeyal = [[0] * n for i in range(n)]
ipyak = n

for i in range(n):
    ipyak = n * (i + 1)
    for j in range(n):
        baeyal[i][j] = ipyak
        ipyak -= 1

for i in range(n):
    for j in range(n):
        print(baeyal[i][j], end='')
    print('')

# 1461
n = int(input())
for j in range(0, n * n, n):
    for i in range(n, 0, -1):
        print("%d " % (i + j), end='')
    print()

n = int(input())

for i in range(1, n + 1):
    for j in range(0, n):
        print(i * n - j, end='')
    print()

# 1463
n = int(input())
baeyal = [[0] * n for i in range(n)]
for i in range(n):
    ipyak = n * (i + 1)
    for j in range(n):
        baeyal[j][i] = ipyak
        ipyak = ipyak - 1

for i in range(n):
    for j in range(n):
        print("%d " % baeyal[i][j], end='')
    print()

# 1484
n, m = map(int, input().split())
row = n
col = m
baeyal = [[0] * m for row in range(n)]
check = 0
cnt = 0
while n > 0 and m > 0:
    for i in range(check, m + check):  # 열변경
        cnt += 1
        baeyal[check][i] = cnt
    for i in range(check + 1, check + n):
        cnt += 1
        baeyal[i][check + m - 1] = cnt

    for i in range(check + m - 2, check, -1):
        cnt = cnt + 1
        baeyal[check + n - 1][i] = cnt

    for i in range(check + n - 1, check, -1):
        cnt = cnt + 1
        baeyal[i][check] = cnt

    check += 1
    m -= 2
    n -= 2

for i in range(row):
    for j in range(col):
        print("%d " % baeyal[i][j], end='')
    print()

    # 1484= snail
n, m = map(int, input().split())
dal = [[0] * m for _ in range(n)]
curi, curj = 1, 1
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
num = 2
mi = 0
dal[0][0] = 1
while True:
    if num > n * m:
        break
    nx = curi + move[mi][0]
    ny = curj + move[mi][1]
    if nx > n or ny > m or nx < 1 or ny < 1:
        mi = (mi + 1) % 4
    else:
        if dal[nx - 1][ny - 1] == 0:
            curi = nx
            curj = ny
            dal[curi - 1][curj - 1] = num
            num += 1
            # print(curi,curj,num)
        else:
            mi = (mi + 1) % 4

for i in range(0, n, 1):
    for j in range(0, m, 1):
        print("%d " % dal[i][j], end='')
    print()


