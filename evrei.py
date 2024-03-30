'''nums = [int(i) for i in open('data.txt').read().split()]'''

f = open('nnooo.txt', 'r').readlines()
h = len(f)
for i in range(h):
    f[i] = int(f[i].strip())
mini = 5
maxi = -7
for i in f:
    if i < mini:
        mini = i
    if i > maxi:
        maxi = i

print(mini,maxi)
