#include <stdio.h>
#include <stdlib.h>

#define DATA_SIZE 1000

int main()
{
    /* Variable to store user content */
    char data[DATA_SIZE];

    /* File pointer to hold reference to our file */
    FILE * fInp;
    FILE * fOut;


    /*
     * Open file in w (write) mode.
     * "data/file1.txt" is complete path to create file
     */
    fInp = fopen("/home/randall/harddisk.sh", "r");
    if(fInp == NULL){
      printf("error");
      exit(EXIT_FAILURE);
    }

    fOut = fopen("/home/randall/test2.sh", "w");
    /* fopen() return NULL if last operation was unsuccessful */
    if(fOut == NULL)
    {
        /* File not created hence exit */
        printf("Unable to create file.\n");
        exit(EXIT_FAILURE);
    }


    /* Input contents from user to store in file */
    printf("Enter contents to store in file : \n");
    fgets(data, DATA_SIZE, stdin);


    /* Write data to file */
    fputs(fInp, fOut);


    /* Close file to save file data */
    fclose(fOut);
    fclose(fInp);

    /* Success message */
    printf("File created and saved successfully. :) \n");


    return 0;
}
