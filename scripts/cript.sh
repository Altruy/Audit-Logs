#!/bin/bash
read -d $'\x04' VAR < "/root/scripts/input.txt" # read previous time from file

TIM=$(date +"%m/%d/%y %H:%M:%S") # load current time into variable

echo $TIM > ./input.txt # save new time in file

# Logs 
echo "-------" >> /root/scripts/out_audit.txt
echo "" >> /root/scripts/out_audit.txt
echo $TIM >> /root/scripts/out_audit.txt
#aureport -ts $VAR -te now -s >> /root/scripts/out_audit.txt
cat /var/log/audit/audit.log | grep SYSCALL >> /root/scripts/out_audit.txt
echo "" > /var/log/audit/audit.log

# Auditd Status
echo "-------" >> /root/scripts/out_status.txt
echo "" >> /root/scripts/out_status.txt
echo $TIM >> /root/scripts/out_status.txt
service auditd status >> /root/scripts/out_status.txt

#Kernel buffer
echo "-------" >> /root/scripts/out_dmesg.txt
echo "" >> /root/scripts/out_dmesg.txt
echo $TIM >> /root/scripts/out_dmesg.txt
/bin/dmesg >> /root/scripts/out_dmesg.txt
/bin/dmesg --clear

