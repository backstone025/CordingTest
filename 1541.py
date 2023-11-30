A = list(map(str, input().split("-")))
ans = 0

def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)

    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        ans += temp

    else:
        ans -= temp

print(ans)