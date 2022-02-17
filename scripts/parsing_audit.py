from datetime import datetime
from syscalls import *

big_file = open('./audit.txt', 'r')
small_file3 = open('./parsed_audit.txt', 'w')
count = 0

try: 
   for line in big_file:
      lins = line.split()
      for word in range(len(lins)):
         if lins[word][:8]=='syscall=':
            try:
               call=calls[int(lins[word][8:])]
               # if call in enable_syscalls:
               output = call+ " "
               small_file3.write(output)
               count+=1
               # else:
               #    break
            except:
               pass
         elif lins[word][:3] == 'a0=':
            ans = lins[word][3:]+' '+lins[word+1][3:]+' '+lins[word+2][3:]+' '+lins[word+3][3:]+'\n'
            small_file3.write(ans)
            break

except Exception as e:
   nfile = open('./error', 'w')
   nfile.write(str(e))
big_file.close()
small_file3.close()

