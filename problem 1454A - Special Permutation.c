// GNU C++17 (64)

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
