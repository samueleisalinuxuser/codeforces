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
