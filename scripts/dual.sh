TIM=$(date +"%H:%M:%S")
mkdir /home/altruy/$TIM

guestmount -a /stretch.img -m /dev/sda  --ro /home/altruy/mnt
cp /home/altruy/gopath/src/github.com/google/syzkaller/log.txt /home/altruy/$TIM
cp /home/altruy/mnt/var/log/audit/audit.log /home/altruy/$TIM 
guestunmount /home/altruy/mnt

cd /home/altruy/$TIM
cp /home/altruy/syscalls.py ./
cp /home/altruy/parsing_audit.py ./
cp /home/altruy/parsing_outs.py ./
cp /home/altruy/compare.py ./

cat audit.log | grep -a "type=SYSCALL" > audit.txt
sed -i 's/#>>>>>>>>/\n#>>>>>>>>/g' log.txt
cat log.txt | grep -a "] -> " > outs.txt
cat log.txt | grep -a "] <- " > outs_res.txt
python3 parsing_audit.py 
sed -i 's/$[a-zA-Z]*/ $/g' outs.txt
sed -i 's/$[a-zA-Z]*/ $/g' outs_res.txt
sed -i 's/(/( /g' outs.txt
python3 parsing_outs.py
python3 compare.py > compare_log.txt

chmod 777 /home/altruy/$TIM -R
rm __pycache__ -r




# TIM=$(date +"%H:%M:%S")
# mkdir /home/altruy/$TIM

# guestmount -a /stretch.img -m /dev/sda  --ro /home/altruy/mnt
# cp /home/altruy/gopath/src/github.com/google/syzkaller/log.txt /home/altruy/$TIM
# cp /home/altruy/mnt/var/log/audit/audit.log /home/altruy/$TIM 
# cp /home/altruy/mnt/root/status.txt /home/altruy/$TIM 
# guestunmount /home/altruy/mnt
# echo "Mount and unmount done"

# cd /home/altruy/$TIM
# cp /home/altruy/syscalls.py ./
# cp /home/altruy/script_audit.py ./
# cp /home/altruy/count.py ./

# sed -i 's/#>>>>>>>>/\n#>>>>>>>>/g' log.txt
# cat log.txt | grep -a "] -> " > outs.txt
# cat log.txt | grep -a "] <- " > outs_res.txt
# python3 script_audit.py 
# sed -i 's/$[a-zA-Z]*/ $/g' outs.txt
# sed -i 's/$[a-zA-Z]*/ $/g' outs_res.txt
# python3 count.py >> /home/altruy/data.txt
# echo "Count Done"
# ls -lh > sizes.txt

# chmod 777 /home/altruy/$TIM -R
# rm ./syscalls.py ./script_audit.py ./count.py ./outs.txt ./outs_res.txt ./outa.txt ./audit.log ./log.txt
# rm __pycache__ -r

