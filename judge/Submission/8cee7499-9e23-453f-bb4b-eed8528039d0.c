#include <stdio.h>
#include <stdlib.h>

int main(){
    int mult = 0;
    int chk =8;
    do{
        mult+=1;
        int *p = (int*)malloc(1024*1024*1024*mult);
        if(p==0){
            chk =0;

        }else{
            free(p);
        }
    }while(chk !=0);
    mult = mult -1;
    printf("The number of gigs allocated is : %d\n",mult);
    return 0;
}