list1 = ['пырчухмячик',"пырчухшарик","пырчухобруч","пырчухннн"]
for i in range(len(list1)):
    f = list1[i][6:]
    list1[i] = 1

print(list1)
for i in range(len(list1)):
    ll = len(list1[i])
    ll // 2