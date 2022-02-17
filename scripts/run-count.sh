cp /home/altruy/syscalls.py ./
cp /home/altruy/script_audit.py ./
cp /home/altruy/count.py ./
sed -i 's/#>>>>>>>>/\n#>>>>>>>>/g' log.txt
cat log.txt | grep -a "] -> " > outs.txt
cat log.txt | grep -a "] <- " > outs_res.txt
python3 script_audit.py
sed -i 's/$[a-zA-Z]*/ $/g' outs.txt
sed -i 's/$[a-zA-Z]*/ $/g' outs_res.txt
python3 count.py
rm __pycache__ -r