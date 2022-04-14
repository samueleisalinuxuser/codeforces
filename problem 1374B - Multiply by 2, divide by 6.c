// GNU C11

#include <stdio.h>

int main(){
    int t;
    scanf("%i",&t);
    if(1 <= t <= 2*10^4){
	int r[t],n,m;
	for(int ts=0; ts<t; ts++){
	    scanf("%i",&n);
	    if(1 <= n <= 10^9){
		m = 0;
		while(n != 1){
		    if(!(n%6)){
			n/=6;
			++m;
		    } else if(!(n%3)){
			n*=2;
			++m;
		    } else{
			m = -1;
			break;
		    }
		}
		r[ts] = m;
	    }
	}
	for(int ts=0; ts<t; ts++) printf("%i\n",r[ts]);
    }
    
    return 0;
}
