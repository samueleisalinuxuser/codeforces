// GNU C++17 (64)

#include <stdio.h>
#include <math.h>

int main(){
	int t;
	scanf("%i",&t);
	if(t >= 1 && t <= pow((double)10,(double)4)){
		int r[t];
		for(int stc=0;stc<t;stc++){
			int n;
			scanf("%i",&n);

			if(n >= 1 && n <= 2*pow((double)10,(double)9)){
				int a=n-1,b=1,w=0;

				while(a > b){
					--a;
					++b;
					++w;
				}
				printf("-----\na=%i\nb=%i\nw=%i\n-----\n",a,b,w);
				r[stc]=w;
			}

		}
		
		for(int i=0;i<t;i++) printf("%i\n",r[i]	);
	}
	return 0;
}
