from datetime import datetime
from syscalls import *

big_file = open('./audit.log', 'r')
small_file3 = open('./outa.txt', 'w')
count = 0
try: 
   for line in big_file:
      if 'type=SYSCALL' in line and 'syz-executor' in line and 'type=PROCTITLE' not in line:
         lins = line.split()
         # ts = int(lins[1][10:20])
         # st=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
         for word in lins:
            if word[:8]=='syscall=':
               try:
                  call=calls[int(word[8:])]
                  if call in enable_syscalls:
                     output = "sys: "+call+ "\n"
                     small_file3.write(output)
                     count+=1
                     break
               except:
                  pass
   small_file3.write('\ncount='+str(count))
except Exception as e:
   nfile = open('./error', 'w')
   nfile.write(str(e))
big_file.close()
small_file3.close()
