#include <iostream>

using namespace std;

int main() {
    double * test[100];
    for ( int x = 0; x < 100; x++ ){
        test[x] = new double[(int)(4e9 / 8)]; //4 Gigs Virtual
        for ( int y= 0; y < 10e6/8; y++ ) //Fill in 10 Megs of Real Ram
            test[x][y] = (double)y;
    }

    cin.get();
    return 0;
}
