#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    int Hmf = 0, Hmt = 0, OutRes = 0; // How many faces and How many throws
    float Probability;
   
    while ((Hmf > 25) || (Hmf < 1) || (OutRes != 1)) { /* Used or operator to make conditions*/
        printf("Please specify a number of faces between 1 and 25: ");
        OutRes = scanf("%d", &Hmf);
        getchar();
    }
    while ((Hmt > 500) || (Hmt < 1) || (OutRes != 1)) { 
        printf("Please specify a number of throws between 1 and 500: ");
        OutRes = scanf("%d", &Hmt);
        getchar();
    }
    char s[] = {"Generating Throws:\n"};
    int index;
    
    for(index = 0; s[index] != '\0'; index++)//loop to simulate a typewriter effect printing each letter until the termination sign \0 is reached
    {
        printf("%c",s[index]);
        fflush(stdout);
        usleep(100000);
    }
    usleep(1000000); //delay to simulate the program thinking to itself
    int ThrowCounter[Hmf]; // Store counter of throw results.
    for (int i = 0; i != Hmf; i++) { // Initlize array forcefully.
        ThrowCounter[i] = 0;
        /* Since C doesn't set all positions to 0 upon initlization, this loop will do that.
           Not doing this loop results in garbage data. */
    }
    srand(time(NULL)); // Grab current UNIX Timestamp and then use as seed for RNG.
    for (int i = 0; i != Hmt; i++) {
        int RandInt = (rand() % Hmf) + 1; // Generate Random Number.
        // ThrowCounter[RandInt-1] = ThrowCounter[RandInt-1] + 1; // Grab counter from position given by generated throw.
        ThrowCounter[RandInt-1]++;
        printf("%d\n", RandInt);
    };
    for (int i = 0; i != Hmf; i++) {
        int Count = ThrowCounter[i]; // Grab counter from array
        if ((Count == 0) || (Hmt == 0)) { // Because division is involved, check to see if either side is 0.
            printf("Occurences of %d : 0.00%% \n",i+1); // If either side is 0, don't attempt division, continue.
            continue;
        }
        Probability = 100.0 / Hmt * Count;// Calculate probability for occurences
        printf("Occurences of %d : %.2f%% \n",i+1,Probability);
        // %.2f will display the floating point number with two decimal places.
    };
    return 0; // Return 0 to OS, siginalling successful execution.
}       


