typedef struct DNode {
    Element data;
    struct DNode* prev;
    struct DNode* next;
} DNode;

DNode org;

DNode* alloc_node(Element e){
    Node* p = (DNode*) malloc(sizeof(DNode));
    p->data = e;
    p->prev = NULL;
    p->next = NULL:
    return p;
}

Element free_Node(DNode* p)
{
    Element e = p->data;
    free(p);
    return e;
}

void error(char* str){
    printf("%s\n", str);
    exit(1);
}

int is_empty() { return org.next == NULL;  }
int is_full() {  return 0;  }
void init_list() {  org.next = NULL;  }

DNode* get_Node(int pos){
    DNode* p = org.next;
    for(int i=0; i < pos; i++){
        if(p == NULL) return NULL;
    }
    return p;
}

Element get_entry(int pos) {
    DNode* p= get_Node(pos);
    if(p == NULL)
        error("해당 위치의 노드가 없어요\n");
    return p->data;
}

void insert(int pos, Element e) {
    DNode* before = get_Node(pos-1);
    if(before == NULL)
            error("위치가 잘못됨\n");
    DNode* p = alloc_node(e);
    p->next = before->next;
    p->prev = before;
    before->next = p;
    if(p->next != NULL)
            p->next->prev = p;
}

Element delete(int pos) {
    if( is_empty())
        error("빈 리스트에서 삭제는 불가능");

    DNode* p = get_Node(pos);
    if( p == NULL)
        error("삭제할 위치의 노드가 없어요");

    p->prev->next = p->next;
    if(p->next != NULL)
            p->next->prev = p->prev;

    return free_Node(p);
}

void destory_list(){
    while( is_empty() == 0 ) delete(0);
}

int size(){
    int count = 0;
    for(DNode* p=org.next; p != NULL; p=p->next) count++;
    return count;
}

void append(Element e){
    insert( size(), e);
}

Element pop() {
    return delete(size()-1);
}

void replace(int pos, Element e){
    DNode* p = get_Node(pos);
    if(p == NULL)
        error("해당 위치의 노드가 없어요 \n");
    p->data = e;
}

int find2(int start, Element e){
    int i = start;
    for(Node*p = get_Node(start); p != NULL ; p=p->next){
        if(p->data == e )
            return i;
        i++;
    }
    return -1;
}

int find1(Element e){
    return find2(0, e);
}
