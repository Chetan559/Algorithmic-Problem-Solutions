#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max_of_two(int i,int j);
int max_of_four(int a, int b, int c, int d);
int max_of_two(int i,int j){
    int temp;
    if(i>=j){
        temp = i;
    }
    else if(j>=i){
        temp = j;
    }
    return temp;
}

int max_of_four(int a, int b, int c, int d){
    
    int x = max_of_two(a,b);
    int y = max_of_two(c,d);
    int maxNum = max_of_two(x,y);
    return maxNum;    
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}