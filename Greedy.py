# 동전 거스름돈
# 돈이 N원일때, 거슬러줘야하는 최소의 동전 개수

n = int(input("금액을 입력하세요 : "))
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n = n % coin

print(count)

# 1일 될때 까지
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n = n - 1
        result += 1

    n /= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# 곱하기 혹은 더하기
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result * num
print(result)

# 모험가 길드 문제 (가능한 최대 그룹 수)
n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)

