#include <stdio.h>

int main() {
    char sentence[1000];
    
    fgets(sentence, sizeof(sentence), stdin);

    int i = 0;
    char current_word[100]; 
    while (sentence[i] != '\0') {
        int j = 0;
        while (sentence[i] != ' ' && sentence[i] != '\0') {
            current_word[j++] = sentence[i++];
        }
        current_word[j] = '\0'; 
        
        printf("%s\n", current_word);

        if (sentence[i] != '\0') {
            i++;
        }
    }

    return 0;
}
