# 1 ~ 10 사이 정수 중 홀수의 합 출력
sum = 0

for i in range(1, 10+1):
    if i % 2 == 0: continue
    sum += i

print(sum)


i = 1
tot = 0

while i <= 100:
    if 1 % 3 == 0 or i % 7 == 0:
        i += 1
        continue

tot += i
i += 1
print(tot)