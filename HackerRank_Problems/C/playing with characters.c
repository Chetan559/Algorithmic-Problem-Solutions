#include <stdio.h>


int main() 
{
    char ch;
    char s[98];
    char sen[98];
    
    scanf("%c",&ch);
    scanf("%s", s);
    scanf("\n");
    scanf("%[^\n]%*c", sen);
    
    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s\n",sen);
        
    return 0;
}
