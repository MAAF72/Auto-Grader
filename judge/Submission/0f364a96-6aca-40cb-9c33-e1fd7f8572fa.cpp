#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	
	int N, K, TotA, TotB, TotC, TotD;
	
	cin >> N >> K;
	cin >> TotA >> TotB >> TotC >> TotD;
	
	int ValP[N];
	int ValA[N];
	int ValB[N];
	int ValC[N];
	int ValD[N];
	int**** DP = new int***[TotA + 1];
	
	/* Initialize DP */
	for (int i = 0; i <= TotA; i++) {
		DP[i] = new int**[TotB + 1];
		for (int j = 0; j <= TotB; j++) {
			DP[i][j] = new int*[TotC + 1];
			for (int k = 0; k <= TotC; k++) {
				DP[i][j][k] = new int[TotD + 1];
				for (int l = 0; l <= TotD; l++) {
					DP[i][j][k][l] = 0;
				}
			}
		}
	}
	
	for (int i = 0; i < N; i++) {
		cin >> ValA[i] >> ValB[i] >> ValC[i] >> ValD[i] >> ValP[i];
	}
	
	for (int e = 0; e < N; e++) {
		for (int m = 0; m < K; m++) {
			for (int i = TotA; i >= ValA[e]; i--) {
				for (int j = TotB; j >= ValB[e]; j--) {
					for (int k = TotC; k >= ValC[e]; k--) {
						for (int l = TotD; l >= ValD[e]; l--) {
							DP[i][j][k][l] = max(DP[i][j][k][l], ValP[e] + DP[i - ValA[e]][j - ValB[e]][k - ValC[e]][l - ValD[e]]);
						}
					}
				}
			}
		}
	}
	
	cout << DP[TotA][TotB][TotC][TotD] << endl;
	return 0;
}