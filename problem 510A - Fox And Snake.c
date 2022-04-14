//GNU C++17 (64)

#include <stdio.h>

int main(){
    int n,m;
    scanf("%i %i",&n,&m);

    if(n >= 3 && m >= 3 && n <= 50 && m <= 50 && n%2!=0){
        char s='r';

        for(int nr=0;nr<n/2;nr++){
            for(int i=0;i<m;i++) printf("#");
            printf("\n");

            if(s=='r'){
                for(int i=1;i<m;i++) printf(".");
                printf("#\n");

                s='l';
            }
            else if(s=='l'){
                printf("#");
                for(int i=1;i<m;i++) printf(".");
                printf("\n");

                s='r';
            }
            
        }

        for(int i=0;i<m;i++) printf("#");
        printf("\n");
    }
    return 0;
}
