#shell 실행  -> python main.py

#리스트 컴프리헨션
#2차원 리스트를 초기화할 때 효율적

array=[i for i in range(20) if i%2==1]
print(array)

n=4
m=3
#2차원 리스트 초기화
array=[[0]*m for _ in range(n)]
#_는 특별한 동작 없음
array[2][1]=5
print(array)


#잘못된 예시
array =[[0]*m] *n
print(array)

array[2][1]=5
print(array)
# 1열 전체의 값이 5로 바뀜. 묶음으로 인식?!

#실수형
a = 0.3 + 0.6
print(a)

if a==0.9:
  print(True)
else:
  print(False)
#결과값은 false
#round를 사용할 것

if round(a,4) == 0.9 :
  print(True)
else:
  print(False)
#결과값은 true

#문자열 연산
#파이썬은 문자열 연산 지원

#튜플 자료형
# 리스트와 유사하지만 한 번 선언된 값을 변경할 수 없음
#소괄호 ()를 사용
#리스트 보다 메모리를 효율적으로 사용
tuple =(1,2,3,4,5,6,7,8)
print(tuple[1])

#사전 자료형
#키와 값의 쌍으로 가지는 자료형
data=dict()
#data = {}
data['사과'] = 'apple'
data['바나나']= 'banana'
print(data)
if '사과' in data :
   print("there is apple")

key_list=data.keys()
value_list=data.values()
print(key_list)
print(value_list)

for key in key_list:
  print(data[key])

#set
lst = [1,1,2,3,4,4,4,5]
data = set(lst)
#중복된 값은 하나로 본다

data1={1,1,2,3,4,4,4,5}
#이렇게 쓰면 집합 자료형


#입력예시
#input()의 리턴값 -> string
#map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
n = int(input())

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

def add_1(n):
  return n+1

target = [1,2,3,4,5]

result = map(add_1, target)
print(result)

# 3개보다 적거나 많게 입력시 오류
n,m,k=map(int,input().split())
print(n,m,k)
print(type(n))