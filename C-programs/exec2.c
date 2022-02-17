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
	if(count>=1)
		break;
int f;
struct iovec iovecc;
syscall(SYS_pipe2,&f, 0x0);						293
syscall(SYS_vmsplice,0x1, &iovecc,1,1);			278
pipe(p);										22
int fd = open("foo.txt", O_RDONLY | O_CREAT);	2
syscall(SYS_socketpair,&f);						53
syscall(SYS_dup2,"Hello world", S_IRWXO);		33
syscall(SYS_mount,"Hello world", S_IRWXO);		165		
fd = open("foo.txt", O_RDONLY | O_CREAT);		2
syscall(SYS_socketpair,"Hello world", S_IRWXO);	53
syscall(SYS_pipe2,&f, 0x0);						293
syscall(SYS_mount,"Hello world", S_IRWXO);		165
syscall(SYS_pipe2,&f, 0x0);						293
syscall(SYS_mount,"Hello world", S_IRWXO);		165
syscall(SYS_pipe2,&f, 0x0);						293
syscall(SYS_mount,"Hello world", S_IRWXO);		165
syscall(SYS_dup2,"Hello world", S_IRWXO);		33
syscall(SYS_mount,"Hello world", S_IRWXO);		165
syscall(SYS_getdents,"Hello world", S_IRWXO);	78
syscall(SYS_lseek,"Hello world", S_IRWXO);		8

sleep(0.0001);	
break;
}
;
return 0;
}
