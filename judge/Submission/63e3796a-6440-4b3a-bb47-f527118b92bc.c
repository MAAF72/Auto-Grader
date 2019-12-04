#include <stdio.h>
#include <malloc.h>

int main(int argc, char** argv)
{
    unsigned char* a[1024*10];
    int i = 0;
    // ~10,000 blocks
    for (; i < 1024*10; i++) {
        a[i] = (unsigned char*)malloc(1024*1024); // allocate 1MB per block
    }

    return 0;
}