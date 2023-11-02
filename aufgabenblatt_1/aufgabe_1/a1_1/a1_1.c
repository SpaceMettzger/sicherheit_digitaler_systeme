#include <stdio.h>

#define PAUSE {printf("\nRETURN!\n"); fflush(stdin); getchar(); }

int main(void)
{
    /*lokale Variablen*/
    char name[32], vorname[32], geb_ort[32];
    unsigned int geb_jahr, geb_monat, geb_tag;


    /*Abfrage der persoenlichen Daten*/
    printf("\nBitte geben Sie folgende Daten ein:\n");
    printf("\nName: ");
    //scanf("%s", name, 31);
    scanf("%31s", name);
    printf("\nVorname: ");
    //scanf("%s", vorname, 31);
    scanf("%31s", vorname);
    printf("\nGeburtsort: ");
    //scanf("%s", geb_ort, 31);
    scanf("%31s", geb_ort);
    printf("\nGeburtsjahr im Format tt.mm.jjjj: ");
    scanf("%u.%u.%u", &geb_tag, &geb_monat, &geb_jahr);

    /*Ausgabe der persönlichen Daten in Tabellenform*/
    printf("\nName:\t\t %s", name);
    printf("\nVorname:\t %s", vorname);
    printf("\nGeburtsort:\t %s", geb_ort);
    printf("\nGeburtstag:\t %02u.%02u.%u", geb_tag, geb_monat, geb_jahr);



    /*Ausgabe der persönlichen Daten als Satz*/
    printf("\nSie heißen %s %s und wurden am %u.%u.%u in %s geboren",
            vorname, name, geb_tag, geb_monat, geb_jahr, geb_ort);

    PAUSE;

}


/*
INFO: Rückabewert der main wurde zu int geändert.
Wenn die eingelesenen Strings zu Lang werden, stürzt das Programm ab.
    python -c 'print("A"*40)' | ./a1_1
    Warum genau 40?
Durch das Begrenzen der Stringlänge in der scanf-Funktion kann der Programmabsturz vermieden werden.
*/