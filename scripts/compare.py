from datetime import datetime
from syscalls import *
from time import time
import numpy as np

big_file = open('./parsed_outs.txt', 'r')
small_file3 = open('./parsed_audit.txt', 'r')
small_file = open('./result.txt','w')
count = 0
found = 0
notthere = 0
st = time()

audit_logs=[ x for x in small_file3]
outs_logs = [x for x in big_file]
audit_logs = [(audit_logs[i],i) for i in range(len(audit_logs)) ]

tot = len(audit_logs)

sysdict = {}
for x in audit_logs:
   index = x[1]
   line = x[0]
   call = line.split()[0]
   if call in sysdict:
      sysdict[call][0].append(line)
      sysdict[call][1].append(index)
   else:
      sysdict[call] = ([line],[index])


print('Preprocessing:',time()-st)           # 3.5 seconds
# audit = np.array(audit_logs)
# audit.reshape(len(audit_logs),1)

# outs = np.array(outs_logs)
# outs.reshape(len(outs_logs),1)
ans = ''
try: 
   tim = time()
   for line in outs_logs:
      try:
         call = line.split()[0]
         i = sysdict[call][0].index(line)
         ans+='++ '+ str(sysdict[call][1][i]) +' | '+ str(line)
         sysdict[call][0][i] = '*****************'
         found +=1
      except:
         ans+='-- '+ ' | '+ str(line)
         notthere+=1
      count+=1
      # if count == 100000:
      #    break
   a = time()
   print('Executing:',time()-tim)
except Exception as e:
   print('except',count,e)
   print('Executing:',time()-tim)

small_file.write(ans)
print('Writing: ',time()-a)
print('\n---------------------------------\n')
print('Lines run:',count)
print('matched:',found,'missing:',notthere,'\naudit logs:',tot,'left:',tot-found)
big_file.close()
small_file3.close()
small_file.close()

# 14.5 secs write in each loop
