import os

list1 = []
list2 = []

diff = 0

with open('input','r') as infile:
    for line in infile:
        data = line.rstrip().split('   ')
        list1.append(int(data[0]))
        list2.append(int(data[1]))
    list1.sort()
    list2.sort()
    for idx, l1 in enumerate(list1):
        l2 = list2[idx]
        if l2 < 0:
            l2 = l2 * -1
        if l1 > l2:
            diff = diff + (l1 - l2)
        else:
            diff = diff + (l2 - l1)
    print(diff)