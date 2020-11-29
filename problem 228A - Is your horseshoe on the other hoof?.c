/*
A. Is your horseshoe on the other hoof?
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Valera the Horse is going to the party with friends.
He has been following the fashion trends for a while, and he knows that it is very popular to wear all horseshoes of different color.
Valera has got four horseshoes left from the last year, but maybe some of them have the same color.
In this case he needs to go to the store and buy some few more horseshoes, not to lose face in front of his stylish comrades.
Fortunately, the store sells horseshoes of all colors under the sun and Valera has enough money to buy any four of them.
However, in order to save the money, he would like to spend as little money as possible, so you need to help Valera and determine what is the minimum number of horseshoes he needs to buy to wear four horseshoes of different colors to a party.

Input
The first line contains four space-separated integers s1, s2, s3, s4 (1 ≤ s1, s2, s3, s4 ≤ 109) — the colors of horseshoes Valera has.
Consider all possible colors indexed with integers.

Output
Print a single integer — the minimum number of horseshoes Valera needs to buy.

Examples
input
1 7 3 3
output
1
input
7 7 7 7
output
3
*/

// lang: GNU C++17 (64)

#include <stdio.h>
#include <math.h>

int main(){
    int s[4],n=0;
    scanf("%i %i %i %i",&s[0],&s[1],&s[2],&s[3]);
    if(s[0] >= 1 && s[1] >= 1 && s[2] >= 1 && s[3] >= 1 && s[0] <= pow((double)10,(double)9) && s[1] <= pow((double)10,(double)9) && s[2] <= pow((double)10,(double)9) && s[3] <= pow((double)10,(double)9)){

        for(int i=0; i<4; i++){
            for(int ii=0;ii<4;ii++){
                if(i != ii && s[i] == s[ii]){
                    ++n;
                    s[i] = 0;
                }
            }
        }

        printf("%i",n);
    }

    return 0;
}
