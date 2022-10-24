#include <stdio.h>
int main(void){
  FILE * fOut;
  fOut = fopen("/home/randall/test2.sh", "r");
  /* fopen() return NULL if last operation was unsuccessful */
  if(fOut == NULL)
  {
      /* File not created hence exit */
      printf("Unable to create file.\n");
      }
  fclose(fOut);
}
