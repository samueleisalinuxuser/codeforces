// GNU C++17 (64)

#include <stdio.h>
#include <string.h>

int main(){
	char ls[3][101];
	for(int l=0; l<3; l++) fgets(ls[l],101,stdin);
	
	int v = 1;

	for(int l=0; l<3;l++) if(strlen(ls[l])-1 > 100){
		v = 0;
		break;
	}

	if(v) for(int l=0; l<3; l++) for(int c=0; c<strlen(ls[l])-1; c++) if((int) ls[l][c] < 65 || (int) ls[l][c] > 90){
		v = 0;
		break;
	}

	if(v){
		for(int l=0; l<2; l++) for(int c=0; c<strlen(ls[l]); c++) for(int cc=0; cc<strlen(ls[2]); cc++) if(ls[l][c] == ls[2][cc]){
			ls[l][c] = ' ';
			ls[2][cc] = ' ' ;
		}

		for(int l=0; l<3; l++) for(int c=0; c<strlen(ls[l])-1; c++) if(ls[l][c] != ' '){
			v = 0;
			break;
		}
		
		switch(v){
			case 1:
				printf("YES");
				break;

			case 0:
				printf("NO");
				break;
		}
	}

	return 0;
}
