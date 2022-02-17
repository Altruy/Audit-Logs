#include <stdio.h>
#include<sys/vfs.h>
#include <sys/statfs.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/uio.h>
#include <fcntl.h>
#define _GNU_SOURCE 
int main(){
int p[2];
int count=0;
while(1)
{
	if(count>=100000)
		break;
int f;

f=syscall(SYS_gettid,&f, 0x0);
syscall(SYS_ptrace,0x4202, f, 0x35,&p);						101
syscall(SYS_ptrace,0x4202, f, 0x35,&p);						101
syscall(SYS_add_key,&f,&p,0x0, 0x0, 0xfffffffffffffffd);	248
syscall(SYS_add_key,&f,&p,0x0, 0x0, 0xfffffffffffffffd);	248
syscall(SYS_keyctl,0x1, 0x0);								250
syscall(SYS_add_key,&f,&p,0x0, 0x0, 0xfffffffffffffffd);	248
syscall(SYS_add_key,&f,&p,0x0, 0x0, 0xfffffffffffffffd);	248
syscall(SYS_sync,0x1, 0x0);									162
sleep(0.0001);	
count = count +1;
}
;
return 0;
}
