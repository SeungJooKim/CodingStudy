# 버블정렬
# 평균, 최상, 최악 모두 O(n제곱)
# 입력자료가 역순으로 되어 있으면 최악의 경우 ( swap에서 발생하는 연산이 더해짐)
# 입력자료가 오름차순으로 되어 있으면 최상의 경우 (swap 불 필요)

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):  # n-1부터 시작해서 0까지 -1씩 감소
        # 리스트가 4 라고 하면 3,2,1
        swapped = False
        for j in range(i):  # 똑같이 뒤에 가장 큰 수! 정렬!
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

bubble_sort(arr)

for i in range(len(arr)):
    print(arr[i])

n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)


# 작은 거 부터 확정 짓는 방식

def bubble_sort_s(arr):
    for i in range(0, len(arr), 1):  # 정렬된 것의 개수 i
        # print(arr,end='')
        swapped = False
        for j in range(len(arr) - 1, i, -1):  # 비교할 대상 j,j-1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break


bubble_sort_s(arr)

for i in range(len(arr)):
    print(arr[i])

# 선택정렬
N = int(input())
lista = []
for i in range(N):
    lista.append(int(input()))

point = 0
mini = 0
while point < len(lista):
    mini = point
    for i in range(point, len(lista), 1):
        if lista[mini] > lista[i]:
            mini = i
    lista[point], lista[mini] = lista[mini], lista[point]
    point += 1
print(lista)

# 선택정렬
n = int(input())
list = []
for i in range(n):
    a = int(input())
    list.append(a)

for i in range(n):
    min = i
    for j in range(i + 1, n, 1):
        if list[i] > list[j]:
            min = j
    list[i], list[min] = list[min], list[i]

for i in range(n):
    print(list[i])


# 삽입정렬
def insert_sort(arr):
    for i in range(0, len(arr), 1):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

insert_sort(arr)
for i in range(n):
    print(arr[i])

# 3011 버블 정렬 단계 구하기
N = int(input())
lista = list(map(int, input().split()))

for i in range(0, N):  # 정렬된 개수
    swapped = False
    for j in range(0, N - 1 - i, 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            swapped = True
    if not swapped:  # 선택정렬의 경우.자기 자신만의 위치를 따지기 때문에 break 하면 안됨.
        # 버블 정렬의 경우, 전체적으로 비교하면서 가장 큰 거를 끝으로 옮기기 때문에 swap 되지 않았다면 종료 하면 됨.
        break
print(i)

# 3011 버블 정렬 단계 구하기
n = int(input())
arr = []
arr = list(map(int, input().strip().split()))


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):  # n-1부터 시작해서 0까지 -1씩 감소

        # 리스트가 4 라고 하면 3,2,1
        swapped = False
        for j in range(i):  # 똑같이 뒤에 가장 큰 수! 정렬! 0,1 ,2
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return len(arr) - i  # 정렬은 이전 단계에서 된 거고 다음 단계에서 확인해 보니 정렬 완료 됨을 확인함
    # return len(arr)-1-i할 경우
    # i가 0부터 시작하지 않기 때문에 완전히 정렬되어 있는 경우 return 값이 0 이됨
    # 완벽 정렬 시 +1해주어야 됨.


step = bubble_sort(arr)
if step != 1:  # 정렬된 것은 이전 단계 이기 떄문 -1
    print(step - 1)
else:
    print(step)

# 3004 재정렬
n = int(input())
data = list(map(int, input().split()))


def bin_search(data, start, end, k):  # 이진탐색
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == k:
            return mid
        elif data[mid] < k:
            start = mid + 1
        else:
            end = mid - 1


def resort(data):
    index_mem = ""
    sorted_data = sorted(data)
    for i in data:
        index_mem += str(bin_search(sorted_data, 0, len(data) - 1, i)) + " "
    return index_mem


print(resort(data))

# 4696 두 용액
n = int(input())
data = list(map(int, input().split()))

result = abs(data[0] + data[1])
n1 = data[0]
n2 = data[1]

for i in range(n):
    for j in range(i + 1, n, 1):
        if abs(data[i] + data[j]) <= result:
            result = abs(data[i] + data[j])
            n1, n2 = data[i], data[j]
        if result == 0:
            break
    if result == 0:
        break

if n1 < n2:
    print(n1, n2)
else:
    print(n2, n1)

# 4696 두 용액

n = int(input())
data = list(map(int, input().split()))
data.sort()  # -1 0 1
com = 1000000000
n1 = 1000000000
n2 = 1000000000

loc1 = 0

for i in range(n):
    if i > 0 and abs(data[i]) < com:
        com = abs(data[i])
        loc1 = i

# loc1이 절대값이 가장 작은 애를 가리켜
# loc2그 다음거!

loc2 = loc1 + 1

if data[0] >= 0:
    print(data[0], data[1])

elif data[n - 1] <= 0:
    print(data[n - 2], data[n - 1])

else:
    while (1):

        if abs(data[loc1] + data[loc2]) < abs(n1 + n2):
            n1 = data[loc1]
            n2 = data[loc2]

        if loc1 == 0 and loc2 == n - 1:
            break

        if (data[loc1] + data[loc2]) < 0 and loc2 < n - 1:
            loc2 += 1

        elif loc1 > 0:
            loc1 -= 1

print(n1, n2)

