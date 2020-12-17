/*
A. Amusing Joke
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

So, the New Year holidays are over. Santa Claus and his colleagues can take a rest and have guests at last.
When two "New Year and Christmas Men" meet, thear assistants cut out of cardboard the letters from the guest's name and the host's name in honor of this event.
Then the hung the letters above the main entrance. One night, when everyone went to bed, someone took all the letters of our characters' names.
Then he may have shuffled the letters and put them in one pile in front of the door.
The next morning it was impossible to find the culprit who had made the disorder.
But everybody wondered whether it is possible to restore the names of the host and his guests from the letters lying at the door? That is, we need to verify that there are no extra letters, and that nobody will need to cut more letters.
Help the "New Year and Christmas Men" and their friends to cope with this problem.
You are given both inscriptions that hung over the front door the previous night, and a pile of letters that were found at the front door next morning.

Input
The input file consists of three lines: the first line contains the guest's name, the second line contains the name of the residence host and the third line contains letters in a pile that were found at the door in the morning.
All lines are not empty and contain only uppercase Latin letters. The length of each line does not exceed 100.

Output
Print "YES" without the quotes, if the letters in the pile could be permuted to make the names of the "New Year and Christmas Men". Otherwise, print "NO" without the quotes.

Examples
input
SANTACLAUS
DEDMOROZ
SANTAMOROZDEDCLAUS
output
YES
input
PAPAINOEL
JOULUPUKKI
JOULNAPAOILELUPUKKI
output
NO
input
BABBONATALE
FATHERCHRISTMAS
BABCHRISTMASBONATALLEFATHER
output
NO

Note
In the first sample the letters written in the last line can be used to write the names and there won't be any extra letters left.
In the second sample letter "P" is missing from the pile and there's an extra letter "L".
In the third sample there's an extra letter "L".
*/

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
