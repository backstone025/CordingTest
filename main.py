peace = input()
b = [1,1,2,2,2,8]

for i in range(6):
    w = int(peace.split(' ')[i])
    print(b[i]-w, end=' ')