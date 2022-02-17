#include <stdio.h>
#include<sys/vfs.h>
#include <sys/statfs.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/stat.h>
#include<sys/socket.h> 
#include <fcntl.h>
#include <string.h>
int main(){
int count =0;
sleep(5);
while(1)
{
	if(count>=10000)
		break;
int value;
value = rename("file1.txt", "file2.txt");
value = rename("file2.txt", "file1.txt");

syscall(SYS_sync);
syscall(SYS_getpid);
syscall(SYS_gettid);
int socket_desc;
socket_desc = socket(AF_INET , SOCK_STREAM , 0);
close(socket_desc);
// syscall(SYS_pipe2,20000);
// syscall(SYS_signalfd);
count=count+1;
sleep(0.0001);	
}
;
return 0;
}
