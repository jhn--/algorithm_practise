#include <stdio.h>
#include <stdlib.h>
#include "llnode.h"

sllnode *create_list(int val);
void add_node(sllnode *list, int val);
void display_list(sllnode *list);
struct sllnode *search_node_val(sllnode *list, int search_val);
void display_node(sllnode *node);
struct sllnode *search_prev_node(sllnode *list, sllnode *search_address);
void del_list(sllnode *list);

sllnode *create_list(int val)
{
    sllnode *n = malloc(sizeof(sllnode));
    n->val = val;
    n->next = NULL;
    return n;
}

void del_list(sllnode *list)
{
    printf("Deleting linked list:\n");
    while (list->next != NULL)
    {
        printf("deleting node:\n");
        display_node(list);
        free(list);
        return del_list(list->next);
    }
    if (list->next == NULL)
    {
        free(list);
    }
}

void add_node(sllnode *list, int val)
{
    /*
    create new node
    if list has no next node
        add next node immediately after list
    if list has a next node
        point new node to next node
        point first node to new node
    */
   sllnode *new = create_list(val);
   if (list->next == NULL)
   {
       list->next = new;
   }
   else
   {
       new->next = list->next;
       list->next = new;
   }
}

struct sllnode *search_node_val(sllnode *list, int search_val)
{
    printf("Searching for nodes in linkedlist with the value: %i\n", search_val);
    while (list)
    {
        if (list->val == search_val)
        {
            printf("%i is in the linked list.\n", search_val);
            return list;
        }
        else if ((list->val != search_val) && (list->next == NULL))
        {
            printf("%i does not exist the linked list.\n", search_val);
            return NULL;
        }
        list = list->next;
    }
}

struct sllnode *search_prev_node(sllnode *list, sllnode *search_address)
{
    // search previous node based on address in node->next
    printf("searching for node with address:\t%p\n", search_address);
    while (list)
    {
        // printf("%p\n", list->next);
        if (list->next == search_address)
        {
            printf("previous node found:\n");
            // display_node(list);
            return list;
        }
        else if ((list->next != search_address) && (list->next == NULL))
        {
            printf("No previous node, node you're looking for might be the root node.\n");
            return NULL;
        }
        list = list->next;        
    }
}

void display_list(sllnode *list)
{
    printf("This is the entire linked list:\n");
    printf("#################################\n");
    while (list)
    {
        display_node(list);
        list = list->next;
    }
    printf("#################################\n");
}

void display_node(sllnode *node)
{
    printf("node pointer:\t%p\n", node);
    printf("node val:\t%i\n", node->val);
    printf("node next:\t%p\n", node->next);
    printf("\n");
}

int main(int argc, char const *argv[]) {
    if (argc != 2) {
        // check if arguments are correct
        printf("USAGE:\targv[0] val\n");
        printf("USAGE:\targv[0] 3\n");
        return 1;
    }

    // convert argument from character to integer.
    int value = atoi(argv[1]);

    // argument is first node aka root node
    sllnode *list = create_list(value);

    // add nodes to root node aka list from a for-loop.
    for (int i = 8; i < 13 ; i++)
    {
        add_node(list, i);
    }

    // display list
    display_list(list);

    //search node based on value
    sllnode *found = search_node_val(list, 8);

    // if node with value we're looking for is found we display the node
    if (found != NULL)
    {
        printf("found:\t%x\n", found);
        display_node(found);
        sllnode *prev = search_prev_node(list, found);
        if (prev != NULL)
        {
            display_node(prev);
        }
    }

    // free the list, dont think its working correct, we should be removing the whole list, _node_ by _node_.
    // free(list);
    del_list(list);
    return 0;
}
