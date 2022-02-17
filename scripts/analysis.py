from datetime import datetime
from syscalls import *
from time import time

big_file = open('./result.txt', 'r')
small_file = open('./analy.txt','w')
count = 0
found = 0
notthere = 0
st = time()

logs = [x for x in big_file]


sysdict = {}
for x in range(len(logs)):
   if logs[x].split()[0] == '--':
      i = 1
      while logs[x-i].split()[0] != '++':
         i+=1
      if logs[x-i].split()[3] not in sysdict:
         sysdict[logs[x-i].split()[3]] = [''.join(logs[x-i:x+1])]
      else:
         sysdict[logs[x-i].split()[3]].append(''.join(logs[x-i:x+1]))

ans = '-------------------------------\n'

for x in sorted (sysdict.keys()):
   ans+=x+' - '+str(len(sysdict[x]))+'\n\n'
   for y in sysdict[x]:
      ans+=y+'\n'
   ans+='\n\n-------------------------------\n'

small_file.write(ans)

