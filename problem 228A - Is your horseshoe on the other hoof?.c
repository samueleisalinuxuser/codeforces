// GNU C++17 (64)

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
