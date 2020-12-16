/*
A. Special Permutation
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given one integer n (n>1).
Recall that a permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order.
For example, [2,3,1,5,4] is a permutation of length 5, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).
Your task is to find a permutation p of length n that there is no index i (1≤i≤n) such that pi=i (so, for all i from 1 to n the condition pi≠i should be satisfied).
You have to answer t independent test cases.
If there are several answers, you can print any. It can be proven that the answer exists for each n>1.

Input
The first line of the input contains one integer t (1≤t≤100) — the number of test cases. Then t test cases follow.
The only line of the test case contains one integer n (2≤n≤100) — the length of the permutation you have to find.

Output
For each test case, print n distinct integers p1,p2,…,pn — a permutation that there is no index i (1≤i≤n) such that pi=i (so, for all i from 1 to n the condition pi≠i should be satisfied).
If there are several answers, you can print any. It can be proven that the answer exists for each n>1.

Example
input
2
2
5
output
2 1
2 1 5 3 4
*/

#include <stdio.h>

int main(){
    int t;
    scanf("%i",&t);
    if(1 <= t <= 100){
        int ns[t], v=1;
        for(int ts=0; ts<t; ts++){
            scanf("%i",&ns[ts]);
            if(ns[ts] < 2 || ns[ts] > 100){
                v = 0;
                break;
            }
        }

        if(v){
            int n;
            for(int ts=0; ts<t; ts++){
                n=ns[ts];
                
                printf("%i ",n);
                for(int i=1; i<n; i++) printf("%i ",i);

                printf("\n");
            }
        }
    }
    return 0;
}
