from time import time
from syscalls import calls

big_file = open('./spade.txt', 'r')
count = 0
found = 0
st = time()

logs = [x for x in big_file]
big_file.close()
ans = []
dic = {}
dic2 = {}

for x in logs:
    freq = int(x.split('-1')[1].split()[1])
    if freq > 1:
        temp = [calls[int(y)] for y in x.split('-1')[0].split()]
        pat = len(temp)
        if pat > 1:
            an = 'length :' + str(pat) + ' | ' + ' '.join(temp) + '\n| freq : ' + \
                str(freq) + ' | lines : ' + \
                ' '.join(x.split('-1')[1].split()[3:])+'\n\n'
            if pat in dic:
                if freq in dic[pat]:
                    dic[pat][freq].append(an)
                else:
                    dic[pat][freq] = [an]
            else:
                dic[pat] = {freq: [an]}
        found += 1
    count += 1


for x in logs:
    freq = int(x.split('-1')[1].split()[1])
    if freq > 1:
        temp = [calls[int(y)] for y in x.split('-1')[0].split()]
        pat = len(temp)
        if pat > 1:
            an = 'freq :' + str(freq) + ' | ' + ' '.join(temp) + '\n| length : ' + \
                str(pat) + ' | lines : ' + \
                ' '.join(x.split('-1')[1].split()[3:])+'\n\n'
            if freq in dic2:
                if pat in dic2[freq]:
                    dic2[freq][pat].append(an)
                else:
                    dic2[freq][pat] = [an]
            else:
                dic2[freq] = {pat: [an]}

print('count=', found)
print('lines=', count)
small_file = open('./spade_pattern.txt', 'w')
for x in sorted(dic, reverse=True):
    for y in sorted(dic[x], reverse=True):
        small_file.write(''.join(dic[x][y]))

small_file1 = open('./spade_frequency.txt', 'w')
for x in sorted(dic2, reverse=True):
    for y in sorted(dic2[x], reverse=True):
        small_file1.write(''.join(dic2[x][y]))
