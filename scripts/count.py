big_file = open('./outa.txt', 'r')
small_file = open('./outs.txt', 'r')
min_file = open('./outs_res.txt', 'r')
small_file3 = open('./total.txt', 'w')

audit = {}
syz = {}
byz = {}
lost_calls =[]

for line in big_file:
   lins = line.split()
   try:
      if lins[1] in audit:
         audit[lins[1]]+=1
      else:
         audit[lins[1]]=0
   except:
      pass

for line in small_file:
   lins = line.split()
   try: 
      if lins[3] in syz:
         syz[lins[3]]+=1
      else:
         syz[lins[3]]=0
   except: 
      pass


# small_file3.write('-----------------------------------------------------------------------------\nAuditd:\n')
# for key in audit:
#    small_file3.write(key+' : '+str(audit[key])+'\n')

# small_file3.write('\n-----------------------------------------------------------------------------\nSyzkaller:\n')
# for key in syz:
#    small_file3.write(key+' : '+str(syz[key])+'\n')

for line in min_file:
   lins = line.split()
   try: 
      if lins[3] in byz:
         byz[lins[3]]+=1
      else:
         byz[lins[3]]=0
   except: 
      pass
got = 0
made = 0
small_file3.write('\n-----------------------------------------------------------------------------\nSyzkaller own logs:                      Audit vs Syzkaller\n')
for key in syz:
   made+= syz[key]
   try:
      if audit[key] <= syz[key]:
         got+=audit[key]
      else:
         got+= syz[key]
   except:
      pass
   try:
      small_file3.write(key+' : '+str(byz[key])+' / '+str(syz[key]))
   except: 
      small_file3.write(key+' : '+str(syz[key])+' not returned')
   try:
      small_file3.write("\n                                         "+str(audit[key])+' / '+str(syz[key]))
      if audit[key] > syz[key]:
         small_file3.write('  <+++++\n')
      elif audit[key] < syz[key]:
         small_file3.write('  <-----  '+str( syz[key] - audit[key] )+'\n')
         lost_calls.append(key)
      else:
         small_file3.write('\n')
   except: 
      small_file3.write("\n                                         "+str(syz[key])+' not returned\n')
small_file3.write('\n\n'+' '.join(lost_calls))
small_file3.write('\n\ngot: '+str(got)+' made: '+str(made)+' loss: '+str(made-got))
print(made-got)
big_file.close()
small_file.close()
small_file3.close()
min_file.close()
