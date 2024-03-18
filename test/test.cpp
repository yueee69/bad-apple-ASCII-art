#include<iostream>
#include<cstdio>
using namespace std;
int main() {
	int sum{}, k, n, i, m = 0;
	long long int sumx = 1;
	cout << "請輸入N值:";
	cin >> n;
	for (i = 1; i <= n; i++)
	{
		sum = sum + i;
	}
	for (k = 1; k <= n; k++) {
		sumx = sumx * k;
	}
	cout << "1+2+3.." << "+" << n << "=" << sum;
	cout << "\n1x2x3.." << "x" << n << "=" << sumx;
}