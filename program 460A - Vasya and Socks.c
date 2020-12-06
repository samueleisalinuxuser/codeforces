/*
A. Vasya and Socks
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Vasya has n pairs of socks. In the morning of each day Vasya has to put on a pair of socks before he goes to school.
When he comes home in the evening, Vasya takes off the used socks and throws them away.
Every m-th day (at days with numbers m, 2m, 3m, ...) mom buys a pair of socks to Vasya.
She does it late in the evening, so that Vasya cannot put on a new pair of socks before the next day.
How many consecutive days pass until Vasya runs out of socks?

Input
The single line contains two integers n and m (1 ≤ n ≤ 100; 2 ≤ m ≤ 100), separated by a space.

Output
Print a single integer — the answer to the problem.

Examples
input
2 2
output
3
input
9 3
output
13

Note
In the first sample Vasya spends the first two days wearing the socks that he had initially.
Then on day three he puts on the socks that were bought on day two.
In the second sample Vasya spends the first nine days wearing the socks that he had initially.
Then he spends three days wearing the socks that were bought on the third, sixth and ninth days.
Than he spends another day wearing the socks that were bought on the twelfth day.
*/

//GNU C++17 (64)

#include <stdio.h>

int main(){
    int n,m;
    scanf("%i %i",&n,&m);

    if(1 <= n <= 100 && 2 <= m <= 100){
        int i=0;

        while(n >= m){
            n = n-m+1;
            ++i;
        }


        int d = m*i+n;

        printf("%i",d);
    }

    return 0;
}

/*
How the program works.
Considering the first example given by the problem:
n = 9
m = 3

                          +1          +1          +1             +1
Number of socks | 9 | 8 | 7 | 7 | 6 | 5 | 5 | 4 | 3 |  3 |  2 |  1 |  1 |
Days            | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
                          *           *           *              *
                        |i=1|       |i=2|       |i=3|         |i=4 |

It is possible to notice that in every day i*m and i*m+1 Vasya has the same number of pairs of socks,
so the number of pairs of socks decreases by n-m+1 every m days and will reach 1 when n remaining pairs of socks are equal to m days;
after that there will be only one more pair of socks resulting in another day.
Each transformation of n corresponds to an increase of the multiplier i, so the total number of days will be equal to i*m+n.
*/