#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,digitsum;
    int a,b,c,d,e;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    
    a = n - (n/10)*10;
    b = n - (n/100)*100 ;
    b = b/10;
    c = n - (n/1000)*1000;
    c = c/100;
    d = n - (n/10000)*10000;
    d = d/1000;
    e = n - (n/100000)*100000;
    e = e/10000;
    
    digitsum = a+b+c+d+e;
    
    printf("%d",digitsum);
    
    return 0;
}