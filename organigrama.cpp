#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;


int main(){
	int n;
	cin >> n;

	for (int i = 0; i < 10000; i++){
		n -= 2;
		if (n == 0){cout << "el numero es par"; break;}
		else if (n < 0){ cout << "el numero es impar"; break;}
	}
	return 0;
}
