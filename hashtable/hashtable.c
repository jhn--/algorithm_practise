#include <stdio.h>
#include <stdlib.h>

/* 
let's create a hash table
of...
an array of 0 to 9 which will contain names based on 
    the number of characters
from a list of _first_ names ie john, terry, jerome, jebediah, jezebel, simon, etc
the names will assigned to the corresponding slot in the array 
as linked list
example - 
array -
[0]
[1]
[2]
[3]
[4]->john->terry
[5]->simon
[6]->jerome
[7]->jezebel
[8]->jebediah
[9]
*/

int main(int argc, char const *argv[])
{
    // so... let's create an array of 10 pointers.. do i need to create a struct? i'll need a struct for the node in the linked list.
    // actually lets create a 2 element array _OF_ pointers
    int *hashtable[2]; 

    // lets create a linked list node
    typedef struct linknode
    {
        char *name; // 1 char takes up 1 byte of space, since we have ... names ranging from 0 characters (i know it doesnt make sense), to 9 characters, technically we ought to have 1 extra byte for /0, but im adding 1 extra byte just in case;
        struct linknode *next;
    }
    node;

    // now.. lets create a node...
    node *zero = malloc(sizeof(node));
    zero->name = "zero";
    zero->next = NULL;

    printf("zero pointer:\t%p\n", zero);
    printf("zero name:\t%s\n", zero->name);
    printf("zero next:\t%p\n", zero->next);

    // now... lets point the first (and only element) to the root node....?
    hashtable[0] = zero;

    // lets create the next node..... idk if im doing this right
    node *one = malloc(sizeof(node));
    one->name = "one";
    one->next = NULL;

    printf("one pointer:\t%p\n", one);
    printf("one name:\t%s\n", one->name);
    printf("one next:\t%p\n", one->next);

    // assign *one to hastable[1]
    hashtable[1] = one;

    // ok lets ... do a print of the array, along w the linked list
    for (int i = 0; i < 2; i++)
    {
        // don't know what to expect here
        node *traverse;
        printf("hastable[%i]:\t%p\n", i, hashtable[i]);
        printf("\n");
        traverse = hashtable[i];
        printf("traverse pointer:\t%p\n", traverse);
        printf("traverse val:\t%s\n", traverse->name);
        printf("traverse next:\t%p\n", traverse->next);
        printf("\n");
    }
    return 0;
}
