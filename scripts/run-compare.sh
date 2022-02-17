cp /home/altruy/syscalls.py ./
cp /home/altruy/parsing* ./
cp /home/altruy/compare.py ./
cat audit.log | grep -a "type=SYSCALL" > audit.txt
sed -i 's/#/\n#/g' log.txt
cat log.txt | grep -a "] -> " > outs.txt
cat log.txt | grep -a "] <- " > outs_res.txt
python3 parsing_audit.py 
sed -i 's/$[a-zA-Z]*/ $/g' outs.txt
sed -i 's/$[a-zA-Z]*/ $/g' outs_res.txt
sed -i 's/(/( /g' outs.txt
python3 parsing_outs.py
python3 compare.py > compare_log.txt

rm __pycache__ -r