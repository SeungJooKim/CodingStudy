# 기초 출력하기
#/n 줄바꿈, /t은 줄 탭, \\는 \ 자체 출력
print("hi hello\n")
print("nice to meet you\r")
print("1\\21")


#윈도우 운영체제의 파일 경로 출력
path="C:\download\hello.cpp"
#c:\download\hello.cpp 사용자가 입력
path.replace('\\','\\\\')
print(path)

#1008 유니코드 특수문자 출력 \u
print("\u250C\u252C\u2510\n")

#1010 입출력
name=input("이름을 입력하세요")
print("이름: {0}, type :{1}".format(name,type(name)))

age=int(input("나이를 입력하세요"))
#age=map(int,input("나이를 입력하세요").split) map 형식으로 저장
print(age)

#1015 실수 자리수 맞춰 출력
weight=float(input("몸무게를 입력하세요"))
print(weight)
print(round(weight,2))

#1017 같은 변수 반복 출력
print("{0} {1} {2}".format(name,name,name))

#형식 지정 출력
print('Today is %d %s.' % (3, 'April'))

# 자리 지정 출력
print('이름:{0:<10}이며 나이는 {1}세입니다.'.format('박은정',24)) #왼쪽 정렬
print('이름:{0:>10}이며 나이는 {1}세입니다.'.format('박은정',24)) #오른쪽 정렬

#특정 문자 제거
"asdfhelloasfasdf".replace("hello"," ")

#1020
x,y = input("주민번호를 입력하세요").split('-')
print(x,y,sep='',end='/')#x,y/
print(x,y,end='')#x,y다음줄의것

#1021
str1=input()
print(str1)

#1023 실수 정수 부분과 실수 부분으로 나누어 출력
x = input("실수를 입력하세요").split('.')
print("정수부분 : ",x[0])
print("실수부분 : ",x[1])

#1024 한 글자씩 분리
x=input("단어를 입력하세요")
for i in range(len(x)):
  print("'",x[i],"'",end='\n')

#1025 5자리 정수를 각 자리별로 나누어 출력
x1,x2,x3,x4,x5=map(int,input("5자리 정수를 입력하세요"))
print('['+str(x1)+'0000]\n')
print('['+str(x2)+'000]\n')
print('['+str(x3)+'00]\n')
print('['+str(x4)+'0]\n')
print('['+str(x5)+'\n')

import math
i=3.52
math.ceil(i)	#올림
math.floor(i)	#내림
math.trunc(i)	#버림

#re모듈 , match
import re
p=re.compile('[a-z]+')
m=p.match("python")
#m.group match 된 것을 string으로 반환
print(m.group())

#1026 시분초에서 분만 출력
time = input("시간을 입력하세요: ")
print(time.split(':')[1]+"분 입니다.")

#1027 년월일 출력 형식 변경
date = input("년월일을 입력하세요 (yyyy.mm.dd)")
print('{0}-{1}-{2}'.format( date.split('.')[0],date.split('.')[1],date.split('.')[2]))

print('Today is %s - %s - %s.' % (date.split('.')[0],date.split('.')[1],date.split('.')[2]))

#8진수로 입력받기
a=int(input(),8) #8진수로 입력받음
print(a)

#8진수,16진수로 출력하기
i = 31
print('%o' %(i))
print('%x' %(i))

#1038 정수 2개 입력받아 더하기
input=input("정수 두개를 입력하세요: ")
input=input.split(" ")

if(len(input) !=2):
  print("error")
else :
  print(int(input[0])+int(input[1]))

a,b = map(int,input().split())
print(a+b)

#1040 부호 바꾸어 출력하기
a = int(input("정수를 입력하세요"))
print(a*-1)

#1041 다음 영문자 출력하기
a = str(input("영문자 하나를 입력하세요"))

#ord() 아스키코드로 변환
a= ord(a)+1

if(a<65 or 90<a<97 or a>123):
  print("영문자를 입력하세요")
else:
  if(a==91 or a==123):
     print("z는 마지막 영문자 입니다.")
  else :
    print(chr(a))


#1042 정수 2개 입력받아 나눈 몫 출력
a = input("정수 2개를 입력하세요 : ").split()
print(int(a[0])/int(a[1]))

a,b=map(int,input().split())
print(a//b)
#c언어는 /가 몫

#1043 정수 2개를 입력받아 나눈 나머지 출력하기
print(a%b)


#1049 기초 비교 연산
a,b = map(int, input("두 정수를 입력하세요 : ").split())

if a>b :
   print("1")
else:
   print("0")

#1050 기초 비교 연산
a,b = map(int, input("두 정수를 입력하세요 : ").split())
if a==b :
  print("1")
else:
  print("0")

#1051 기초 비교 연산
a,b = map(int, input("두 정수를 입력하세요 : ").split())
if a <=b :
   print("1")
else :
   print("0")

#1052
a,b = map(int, input("두 정수를 입력하세요 : ").split())
if a!=b:
  print("1")
else:
  print("0")

# 1053 논리연산
ans= int(input())
if ans ==1:
  print(0)
else :
  print(1)

#1054 논리연산
a,b= map(int,input("참 거짓 중 두 개를 입력하세요").split())
if a==1 and b==1 :
  print("true")

#1055 논리연산
a,b= map(int,input("참 거짓 중 두 개를 입력하세요").split())
if a==1 or b==1 :
  print("true")


#1059 비트단위논리연산 not
a = int(input("정수를 입력하세요"))
print(~a)

#1060 비트단위논리연산 and
a,b = map(int,input("두 개의 정수를 입력하세요").split())
print(a & b)

#1061 비트단위논리연산 or
a,b =map(int,input("두 개의 정수를 입력하세요").split())
print(a|b)

#1062 비트단위논리연산 xor
#xor 배타적 논리합 => 서로 다를 때 1
# 그래픽 처리에 효과적으로 사용 ex. 두 장의 이미지가 겹쳤을 때 서로 다른 부분만 처리가능
a,b =map(int,input("두 개의 정수를 입력하세요").split())
print(a^b)

#1063 삼항 연산
a,b =map(int,input("두 개의 정수를 입력하세요").split())
print(a if a>b else b)

#1064 삼항 연산
a,b,c=map(int,input("세 개의 정수를 입력하세요").split())
x = (a if (a<b) else b)
print(x if x<c else c)

#1065 짝수만 출력
a,b,c=map(int,input("세 개의 정수를 입력하세요").split())
if a%2==0:
  print(a)
if b%2==0 :
  print(b)
if c%2==0:
  print(c)