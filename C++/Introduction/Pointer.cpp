#include <iostream>
#include <stdlib.h>

using namespace std;

void update(int *a,int *b) 
{
   int c = *a + *b;
   int d = abs(*a - *b);  
   *a = c;
   *b = d; 
}

int main() 
{
    int a, b;
    int *pa = &a, *pb = &b;
    cin >> a >> b;
    update(pa, pb);
    cout << a << endl << b;

    return 0;
}
