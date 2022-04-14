// GNU C++17 (64)

#include <stdio.h>
#include <math.h>

int main(){
    int n;
    scanf("%i",&n);

    if(n >= 1 && n <= pow((double)10,(double)9)){
        int b=0, db[5]={1,5,10,20,100};
        
        for(int i=4;i>=0;i--){
            while(n >= db[i]){
                ++b;
                n-=db[i];
            }
        }

        printf("%i",b);

    }

    return 0;
}
