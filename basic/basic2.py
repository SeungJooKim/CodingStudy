
# isalpha() 는 문자열이 모두 문자(영어 또는 한글)이면 true 아니면 False, 특수문자가 있으면 false
# isdigit() 는 문자열이 모두 숫자이면 true 아니면 false
# isalnum() 는 한글 영어 혹은 숫자이면 true 아니면 false


#파이썬 정렬 조건 부여하기
#파이썬의 sorted()는 정렬 조건을 설정해 줄 수 있다.! .sort()
# 여러 개의 요소를 갖는 튜플을 원소로 갖는 리스트라면 두번째 요소 값으로 기준을 정렬한다던가 혹은 lambda함수를 이용하여 조건을 설정 할 수 있다.
listb2= sorted( listb2, key=lambda x : (x[0], x[1],x[2])) 
# -를 붙여주면 내림차순으로 비교


# a.sort는 해당 객체를 정렬해서 해당 객체에 저장
# 그러나 sorted의 경우 정렬된 객체를 반환하기 때문에 정렬된 객체를 받아줄 변수가 필요!
# sort 같은 경우 특정 조건을 주기가 어려우니 sorted를 사용하는게 좋음!


for i in range(n):
  print(listb2[i][2])


## TUPLE
# tuple이란? 몇가지 점을 제외하곤 리스트와 거의 비슷
# 리스트와의 차이점은? 리스트는 []를 사용 튜플은 ()를 사용한
# 리스트는 그 값의 생성,삭제, 수정이 가능하지만 튜플은 그 값을 변경할 수 없다!



# 튜플 사용 예시
# tu = ()
# tu = (1,) #1개의 요소만 가질 때는 뒤에 꼭 , 붙여야 한다
# tu = (1,2,3)
# tu = 1, 2, 3
# tu = ('a','b',('ab','cd'))


# 튜플은 변경, 삭제, 수정이 불가하기 때문에 잘 사용 되지는 않는다!
# 튜플 접근 방법! (리스트와 비슷 , 연산도 가능)
# t1 =(1, 2, 3) t2 = 4,5,6
# t1[1:2]
# t1+t2
# t2*3
# len(t1)


## 딕셔너리!
# 관계를 나타낼 수 있는 자료형으로 이를 연관배열 또는 해시라고 한다. 
# 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 key를 통해 value를 얻는다.


# 딕셔너리 사용법
a = dict()
a = {'seoung': 'girl'}
a['tae'] = 'boy'

# 딕셔너리 요소 삭제
# del a['seoung']

a =list(a.items())
print(a[1])
# 딕셔너리 사용 주의 사항
# 딕셔너리는 중복키를 허용하지 않는다. 
# 중복키의 경우 하나만 인식!
# a.items()는 key와 value 쌍을 튜플로 묶은 값을 객체로 반환!

# key = a.keys() 는 키값들만 모아서 반환 (dict_keys 형태로 )
# 이를 리스트로 반환받고 싶으면 key = list(a.keys())

# value = a.values() 는 value 값들만 모아서 반환
# 이를 리스트로 반환받고 싶으면 values = list(a.values())


# key로 value 얻기! (get)
# a.get('key 이름') 또는 a.get('key이름', '디폴트 값')  a.get('seoung','eunjeong')
# 해당 키 값이 없는 경우 미리 정해 둔 디폴드 값을 대신 가져옴.

# 해당 키가 딕셔너리 안에 있는지 조사하기 (in)
# 'name' in a 
# 반환값은 true or f


## zip()
# zip()은 동일한 개수로 이루어진 자료형을 묶어주는 함수
#a=[1,2,3] 
#b=[4,5,6] 
#dic={}


#for c,d in zip(a,b):
#  dic[c] = d

# print(dic[3]) # 6


# dica= {'a':1,'b':2}
# dicb={'a':2, 'c':3}

# for c,d in zip(dica.values(),dicb.values()): # 그냥 dica,dicb 하면 키 값들이 읽힘
#  print(c,d) 
