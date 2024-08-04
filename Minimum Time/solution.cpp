//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
//} Driver Code Ends

class Solution {
public:
    int minTime(int n, vector<int> &time, vector<int> &search, int k) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        deque<int> deq;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1] + time[i-1];
            for (int j = 1; j <= k && i - j >= 0; j++) {
                dp[i] = min(dp[i], dp[i-j] + search[i-j]);
            }
        }
        return dp[n];
    }
};

//{ Driver Code Starts
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> time(n);
        for (int i = 0; i < n; i++) {
            cin >> time[i];
        }

        vector<int> search(n);
        for (int i = 0; i < n; i++) {
            cin >> search[i];
        }

        int k;
        cin >> k;

        Solution obj;
        int res = obj.minTime(n, time, search, k);

        cout << res << endl;
    }
    return 0;
}
//} Driver Code Ends
