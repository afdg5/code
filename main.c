#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_MODEL 25
#define MAX_LINE 50

typedef struct Car {
    char* model;
    char* color;
    int year;
    struct Car* next;
} car;

car* readFile(FILE*);
car* SortOrder(car*,char*,char*,int);
car* createCar(char*,char*,int);


int main(int argc,char** argv) {

if (argc!=2) {
    exit(0);
}
    FILE* fp = fopen(argv[1],"r");
    if (fp==NULL) {
        printf("ERROR/n");
    }

    car* head = readFile(fp);

    


return 0;

}


car* readFile(FILE* fp){
    char string[MAX_LINE];
    char* token;
    car* head;
    int year;
    char model[MAX_MODEL];
    char color[MAX_MODEL];

    while(fgets(string,MAX_LINE,fp)!=NULL) {
        token = strtok(string,"/ ");
        year = atoi(token);

        token = strtok(NULL,"/ ");
        strcpy(model,token);

        token = strtok(NULL,"/n");
        strcpy(color,token);

        car* head = SortOrder(head,model,color,year);
    }

return head;
}

car* SortOrder(car* head,char* model,char* color,int year) {
        car* new = createCar(model,color,year);
        car* temp = NULL;
        car* curr = head;

        if (head == NULL  || strcmp(model,head->model)<0) {
            new->next = head;
            head = new;
            return head;
        }

        while (curr->next != NULL && strcmp(model,curr->next->model)>0) {
                curr=curr->next;
            }
            temp = curr->next;
            curr->next = new;
            new->next = temp;

    return head;

}

car* createCar(char* model,char* color,int year) {
    car* newCar = malloc(sizeof(car*));
    newCar->model = model;
    newCar->color = color;
    newCar->year = year;
    newCar->next = NULL;
    return newCar;

}
