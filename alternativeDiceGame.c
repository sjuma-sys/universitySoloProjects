#include <stdio.h> /*Standard input and output*/
#include <stdlib.h> /*Utility functions*/
#include <time.h> /*Time functions */

int main () {
   int i, n_of_f, n_of_t, ans; /*Set every variables as integers*/
   time_t t;
   float per; /*sets per as a float*/
 
   printf("%s\n", "How many faces?");
   scanf("%d", &n_of_f);
   
   while ((n_of_f >= 25) || (n_of_f <= 1)) { /* Used or operator to make conditions*/
        printf("please enter a value between 25 and 1:");
        scanf("%d", &n_of_f);
    }
   
   printf("%s\n", "How many throws?");
   scanf("%d", &n_of_t);
    while ((n_of_t >= 500) || (n_of_t <=1)) { 
        printf("please enter a value between 1 and 500");
        scanf("%d", &n_of_t);
   }
   /* Intializes random number generator */
   srand((unsigned) time(&t)); /*time is my seed for the rng, gets time from the CPU and creates a number based on that*/
    /*Unsigned integer used to define srand*/
   /*and t is used to set the time*/
   for( i = 0 ; i < n_of_t ; i++ ) {
      ans = rand() % n_of_f;
      per = ans * n_of_f; /*we times these two together to give us the percentage chance of getting that number*/
      printf("\nYour number is\t\t\t\t\t");
      printf("%d\n",ans);
      printf("The chances of generating this number is \t");
      printf("%f", per);/* Print random numbers divided by the number of faces*/
      printf("%%");
   }
   
   return(0);
}
