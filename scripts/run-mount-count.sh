TIM=$(date +"%H:%M:%S")
mkdir /home/jellybean/$TIM

guestmount -a /stretch.img -m /dev/sda  --ro /home/jellybean/mnt
cp /home/jellybean/gopath/src/github.com/google/syzkaller/log.txt /home/jellybean/$TIM
cp /home/jellybean/mnt/var/log/audit/audit.log /home/jellybean/$TIM 
cp /home/jellybean/mnt/root/status.txt /home/jellybean/$TIM 
guestunmount /home/jellybean/mnt

cd /home/jellybean/$TIM
cp /home/jellybean/syscalls.py ./
cp /home/jellybean/script_audit.py ./
cp /home/jellybean/count.py ./

sed -i 's/#/\n#/g' log.txt
cat log.txt | grep -a "] -> " > outs.txt
cat log.txt | grep -a "] <- " > outs_res.txt
python3 script_audit.py 
sed -i 's/$[a-zA-Z]*/ $/g' outs.txt
sed -i 's/$[a-zA-Z]*/ $/g' outs_res.txt
python3 count.py >> /home/jellybean/data.txt
echo "Count Done"
ls -lh > sizes.txt

chmod 777 /home/jellybean/$TIM -R
rm ./syscalls.py ./script_audit.py ./count.py ./outs.txt ./outs_res.txt ./outa.txt 
rm __pycache__ -r

