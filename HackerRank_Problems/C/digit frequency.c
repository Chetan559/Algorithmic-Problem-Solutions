#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int a,b,c,d,e,f,g,h,i,j;
    a=b=c=d=e=f=g=h=i=j=0;
    char *arr = malloc(1001 * sizeof(char));
    char temp;
    int y = 0;
    while(scanf("%c",&temp) == 1 && temp != "\n"){
        arr[y++] = temp;
    }
    
    for(int x = 0 ; x <= y ;x++){
        if(arr[x] == '0'){a++;}
        else if(arr[x] == '1'){
            b++;
            }
        else if(arr[x] == '2'){
            c++;
            }
        else if(arr[x] == '3'){
            d++;
            }
        else if(arr[x] == '4'){
            e++;
            }
        else if(arr[x] == '5'){
            f++;
            }
        else if(arr[x] == '6'){
            g++;
            }
        else if(arr[x] == '7'){
            h++;
            }
        else if(arr[x] == '8'){
            i++;
            }
        else if(arr[x] == '9'){
            j++;
            }
    } 
    
    printf("%d %d %d %d %d %d %d %d %d %d ",a,b,c,d,e,f,g,h,i,j);
    
    free(arr);
    
    return 0;
}
