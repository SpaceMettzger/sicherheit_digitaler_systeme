# include <stdio.h>
# include <stdlib.h>

enum {BUFFER_SIZE = 10};


int main () {

int check1 = 0;
char buffer[BUFFER_SIZE];
int check2 = 0;

// scanf("%s", buffer);
fgets(buffer, BUFFER_SIZE, stdin);

if (check1 || check2) puts ("You Win");

return EXIT_SUCCESS;
}


/* 
11 wahlose Zeichen im Buffer führen zu der "You Win" Nachricht.
python -c 'print("A"*11)' | ./a2_1
Durch das Ersetzen der scanf Funktion mit fgets kann das vermieden werden.
*/
