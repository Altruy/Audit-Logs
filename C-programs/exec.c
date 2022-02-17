#include <stdio.h>
#include <unistd.h>
#include<sys/vfs.h>
#include <sys/statfs.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#define _GNU_SOURCE 
int main(){
char old_name1[] = "file1.txt";
int count =0;
while(1)
{
	if(count>=1000000)
		break;
	char new_name1[] = "file2.txt";
	int value;
	value = rename(old_name1, new_name1);
	strcpy(new_name1,"file1.txt");
	value = rename(old_name1, new_name1);
	strcpy(old_name1,new_name1);

	count=count+1;
	sleep(0.0001);	
}
;
return 0;
}

