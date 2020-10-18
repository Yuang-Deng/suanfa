#include <vector>
#include <iostream>
using namespace std;
//Please do NOT change the file name.
/*
This function computes he least amount of egg drops one has to perform to find out the threshold floor
oor F
Args:
    n: number of floors
    e: number of eggs
Return:
    The least amount of egg drops one has to perform to find out the threshold floor
*/
int Egg_drop(int n, int e) {
    //complete the function
    int dp[e+1];
    int step=0;
    memset(dp,0,sizeof(dp));
    while (dp[e]<n){
        for (int i = e; i >= 1 ; --i) {
            dp[i]+=dp[i-1]+1;
        }
        step++;
    }
    return step;
}
//Please do NOT modify anything in main(). Thanks!
int main()
{
    int n,e;
    cin>>n>>e;
    cout<<Egg_drop(n,e);
    return 0;
}
