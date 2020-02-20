#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

typedef char* WORD;
typedef WORD* Sentence;
typedef Sentence* PARA;
typedef PARA* DOC;

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n) {
    return document[n-1][m-1][k-1];
}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m) { 
    return document[m-1][k-1];
}

char*** kth_paragraph(char**** document, int k)
{
    return document[k-1];
}

Sentence getSentence(char *text, int *pos)
{
    WORD w[MAX_CHARACTERS];
    WORD *finalW = NULL;
    int begin = *pos;
    int end;
    int count = 0;
    for(end=begin; text[end]; end++)
    {
        if(text[end]==' ' || text[end]=='.')
        {
            w[count] = calloc(end-begin+1, sizeof(char));
            memcpy(w[count], text+begin, end-begin);
            count++;
            if(text[end] == '.') break;
            begin=end+1;
        }
    }
    *pos = end;
    finalW = malloc(count*sizeof(WORD));
    memcpy(finalW, w, count*sizeof(WORD));
    return finalW;
}

PARA getPara(char *text, int *pos)
{
    Sentence s[MAX_CHARACTERS];
    Sentence *finalS = NULL;
    int n;
    for(n=0; n<MAX_CHARACTERS; n++)
    {
        s[n] = getSentence(text, pos);
        if(text[*pos]==0 || text[1+*pos] == '\n')
        {
            break;
        }
        (*pos)++;
    }
    finalS = malloc((1+n)*sizeof(Sentence));
    memcpy(finalS, s, (1+n)*sizeof(Sentence));
    return finalS;
}

char**** get_document(char* text) {
    PARA p[MAX_PARAGRAPHS]={0,};
    DOC d=NULL;
    int n;
    int pos = 0;
    for(n=0; n<MAX_PARAGRAPHS; n++, pos++)
    {        
        p[n] = getPara(text, &pos);
        if(text[pos]) pos++;
    }
    d = malloc(n*sizeof(PARA));
    memcpy(d, p, n*sizeof(PARA));
    return d;
    
}


char* get_input_text() {	
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

void print_word(char* word) {
    printf("%s", word);
}

void print_sentence(char** sentence) {
    int word_count;
    scanf("%d", &word_count);
    for(int i = 0; i < word_count; i++){
        printf("%s", sentence[i]);
        if( i != word_count - 1)
            printf(" ");
    }
} 

void print_paragraph(char*** paragraph) {
    int sentence_count;
    scanf("%d", &sentence_count);
    for (int i = 0; i < sentence_count; i++) {
        print_sentence(*(paragraph + i));
        printf(".");
    }
}

int main() 
{
    char* text = get_input_text();
    char**** document = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            char* word = kth_word_in_mth_sentence_of_nth_paragraph(document, k, m, n);
            print_word(word);
        }

        else if (type == 2){
            int k, m;
            scanf("%d %d", &k, &m);
            char** sentence = kth_sentence_in_mth_paragraph(document, k, m);
            print_sentence(sentence);
        }

        else{
            int k;
            scanf("%d", &k);
            char*** paragraph = kth_paragraph(document, k);
            print_paragraph(paragraph);
        }
        printf("\n");
    }     
}
