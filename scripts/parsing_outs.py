sample = open('./outs.txt', 'r')
out = open('./parsed_outs.txt', 'w')
temp=''
for line in sample:
   sl=line.split()
   temp=sl[3] +' '
   try:
      for i in range(len(sl)):
         if sl[i]=='(':
            temp =temp+sl[i+1][2:] +' ' + sl[i+3][2:] +' '+ sl[i+4][3:]+' '+ sl[i+5][3:]+  '\n'
            break
      out.write(temp)
   except:
      pass
sample.close()
out.close()