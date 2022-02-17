from time import time
from syscalls import calls


def get_key(val):
    for key, value in calls.items():
        if val == value:
            return key

    return "key doesn't exist"


big_file = open('./result.txt', 'r')
small_file = open('./spade_input.txt', 'w')
count = 0
found = 0
notthere = 0
st = time()

logs = [x for x in big_file]


ans = []
for x in range(len(logs)):
    if logs[x].split()[0] == '--':
        an = ''
        for y in range(11):
            call = logs[x-10+y].split()[3]
            an += str(get_key(call)) + ' '
        ans.append(an+'\n')
        count += 1
    if x % 10000 == 0:
        print(x)
print('count=', count)
small_file.write(''.join(ans))
