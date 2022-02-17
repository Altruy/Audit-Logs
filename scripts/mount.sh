TIM=$(date +"%H:%M:%S")
mkdir /home/altruy/$TIM
guestmount -a /buster.img -m /dev/sda  --ro /home/altruy/mnt
ls -lh /home/altruy/mnt/root/ 
cp /home/altruy/mnt/root/* /home/altruy/$TIM 
cp /home/altruy/gopath/src/github.com/google/syzkaller/log.txt /home/altruy/$TIM
cp /home/altruy/mnt/var/log/audit/audit.log /home/altruy/$TIM 
# cp /home/altruy/run1.sh /home/altruy/$TIM
guestunmount /home/altruy/mnt
cp /home/altruy/run-compare.sh /home/altruy/$TIM 
cd /home/altruy/$TIM
chmod 777 /home/altruy/$TIM -R