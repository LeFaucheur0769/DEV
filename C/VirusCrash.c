#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    char bat = "@echo\n\nstart";
    char greetings[] = "N";
    char Y[] = "Y";
    char y[] = "y";
    printf("Are you sure Y/n : ");
    gets(greetings);
    if(strcmp(greetings,y) == 0 | strcmp(greetings,Y) == 0){
        greetings[0] = 'n';
        printf("Last chance Y/n : ");
        gets(greetings);
        if(strcmp(greetings,y) == 0 | strcmp(greetings,Y) == 0){
            FILE * crash = fopen("C:\\crash.bat", "rw");
            (void)system("C:\\crash.bat");
            fputs(bat,crash);
            fclose(crash);
        }
    else{
        printf("ouf !!");
    }
}
else{
    printf("ouf");
}
printf("\n");
return 0;
}
