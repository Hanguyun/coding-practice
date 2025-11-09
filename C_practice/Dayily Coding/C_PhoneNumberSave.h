typedef struct Node {
    Element data;
    struct Node* link;
} Node;

Node* rear = NULL;

Node* alloc_node(Element e)
{
    Node* p = (Node*)malloc(sizeof(Node));
    p->data = e;
    p->link = NULL;
    return p;
}
Element free_node(Node* p)
{
    Element e = p->data;
    free(p);
    return e;
}

void error(char* str)
{
    printf("%s\n", str);
    exit(1);
}

int is_empty() { return rear == NULL; }
int is_full() { return 0; }
void init_queue() { rear = NULL; }

void enqueue(Element e)
{
    Node* p = alloc_node(e);
    if (is_empty()) {
        rear = p;
        p->link = p;
    }
    else {
        p->link = rear->link;
        rear->link = p;
        rear = p;
    }
}

Element dequeue()
{
    if (is_empty())
        error("Underflow Error!");

    Node* p = rear->link;
    if (rear == p)
        rear = NULL;
    else
        rear->link = p->link;
    return free_node(p);
}

Element peek()
{
    if (is_empty())
        error("Underflow Error!");
    return rear->link->data;
}

void destroy_queue()
{
    while (is_empty() == 0) dequeue();
}
