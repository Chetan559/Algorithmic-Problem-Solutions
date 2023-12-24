#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender) {
  //Write your code here.
  int finalanswer,a=0,x=0;
      for(int i=0;i<=number_of_students;i++){
         if(i%2 == 0){
             a = a + marks[i];
         }
         else if(i%2 != 0){
             x = x + marks[i];
         }
          
      }
  if(gender=='g'){ finalanswer = x;}
  else if(gender=='b'){ finalanswer = a; }
  
  return finalanswer;
}

int main() {
    int number_of_students;
    char gender;
    int sum;
  
    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));
 
    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }
    
    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);
 
    return 0;
}