big_file = open('./outa.txt', 'r')
small_file3 = open('./total.txt', 'w')
from syscalls import *

audit = {}
syz = {}
byz = {}

for line in big_file:
   lins = line.split()
   try:
      if lins[1] in audit:
         audit[lins[1]]+=1
      else:
         audit[lins[1]]=0
   except:
      pass

made = 0
small_file3.write('\n--------------------------------------\nAudit vs Syzkaller\n')
for key in enable_syscalls:
   try:
      made+= audit[key]
   except:
      pass
   try:
      small_file3.write(key+' : \n                       '+str(audit[key])+'\n')
   except: 
      small_file3.write(key+' : \n                       0\n')
   
small_file3.write('\n\nmade: '+str(made))

big_file.close()
small_file3.close()
