#include <iostream>
#include <string>
using namespace std;

int main() {
	string a,b;
    cin >> a >> b;

    int len1 = a.size();
    int len2 = b.size();

    cout << len1 << " " << len2 << endl;
    
    string c = a + b;

    cout << c << endl;

    char temp1 = a[0];
    char temp2 = b[0];

    b[0] = temp1;
    a[0] = temp2;

    cout << a << " " << b;

    return 0;
}
