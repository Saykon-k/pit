#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct island{
    char *name;
    struct island *next;
    struct island *prev;
} island;

island* create(island *last){
    island *i = malloc(sizeof(island));
    char isl_name[40];
    printf("Write island name: ");
    scanf("%19s", isl_name);
    i -> name = malloc(strlen(isl_name) + 1);
    i -> name = strdup(isl_name);
    i -> next = NULL;
    i -> prev = NULL;
    return i;
}

island* add(island *last){
    char isl_name[40];
    printf("Enter new island name: ");
    scanf("%19s", isl_name);
    island *i = malloc(sizeof(island));
    i -> name = malloc(strlen(isl_name) + 1);
    i -> name = strdup(isl_name);
    i -> prev = last;
    last -> next = i;
    i -> next = NULL;
    return i;
}

void display(island *start){
    island *i = start;
    for(;i!=NULL;i=i->next){
        printf("%s  ", i -> name);
    }
    printf("\n");
}

island* del(island *start){
    island *i = start;
    island *next = NULL;
    island *prev = NULL;
    if(start->prev != NULL){
        prev = start->prev;
        start->prev->next = NULL;
    }
    for(;i!=NULL;i=next){
        next = i -> next;
        free(i -> name);
        free(i);
    }
    return prev;
}

island* search(island *start, char *name){
    island *i = start;
    island *res = NULL;
    for(;i!=NULL;i=i->next){
        if(strcmp(i->name,name)==0){
            res = i;
            break;
        }
    }
    return res;
}
int main()
{
    system("chcp 1251");
    system("cls");
    int ke;
    char se_name[20];
    island *start = NULL;
    island *last = NULL;
    island *i = NULL;
    island *temp = NULL;
    int bol = 1;
    while(bol){
        printf("Choose an option:\n1) Create first element\n2) Add last element\n3) Delete last element\n4) Show all list\n5) Delete list\n6) Find some element\n7) exit\n");
        printf("Your choice: ");
        scanf("%d",&ke);
        switch (ke) {
          case 1: i = create(last); printf("\n");  start = i;  last = i; break;
          case 2: i = add(last);  printf("\n");last = i;break;
          case 3: last = del(last);printf("\n");break;
          case 4: if(start -> name != NULL){ display(start);} printf("\n");break;
          case 5: last = del(start); printf("\n");break;
          case 6: printf("Enter name of an island: "); scanf("%19s", se_name); temp = search(start,se_name); if(temp!=NULL){printf("%s\n",temp->name);}else{printf("No such island\n");} printf("\n");break;
          case 7: bol=1;break;
    }
    }
    return 0;
}
