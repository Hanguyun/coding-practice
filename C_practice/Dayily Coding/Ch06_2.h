typedef struct Node {
    Element data;
    struct Node* link;
} Node;

Node* head = NULL;

Node* alloc_node(Element e) {
    Node* p = malloc(sizeof(Node));
    p->data = e;
    p->link = NULL;
    return p;
}

Element free_node(Node* p) {
    Element e = p -> data;
    free(p);
    return e;
}

void error(char* str){
    printf("%s\n", str);
    exit(1);
}

int is_empty() {return head == NULL;}
int is_full() {return 0;}
void init_list() {head = NULL;}

Node* get_node(int pos) {
    if (pos < 0) return NULL;
    Node* p = head;

    for (int i = 0; i < pos; i++, p = p -> link) {
        if(p == NULL) return NULL;
    }
        return p;
}

Element get_entry(int pos) {
    Node* p = get_node(pos);
    if(p == NULL)
        error("해당 위치의 노드가 없습니다.\n");
    return p->data;
}

void insert(int pos, Element e) {
        Node*p = alloc_node(e);
        if(pos == 0) {
            p->link = head;
            head = p;
        }
        else {
            Node* before = get_node(pos-1);
            if(before == NULL)
                error("위치가 잘못 되었습니다.\n");
            p -> link = before -> link;
            before -> link = p;
        }
}

Element delete(int pos){
    if (is_empty())
        error("리스트가 빈 상황에서 삭제할 수 없습니다.\n");
    Node* p= get_node(pos);
    if(p == NULL)
        error("위치가 잘못 되었습니다.\n");
    Node* before=get_node(pos-1);
    if(before==NULL)
        head=head->link;
    else
        before->link=p->link;
    return free_node(p);
}

void destory_list() {
    while(is_empty() == 0) delete(0);
}

int size() {
    int count = 0;
    for(Node* p=head; p!=NULL; p=p->link) count++;
    return count;
}

void append(Element e) {
    insert(size(), e);
}

Element pop() {
    delete(size()-1);
}

void replace(int pos, Element e) {
    Node* p=get_node(pos);
    if(p==NULL)
        error("위치가 잘못 되었습니다.");
    p->data=e;
}

int find2(int start, Element e) {
    int i = 0;
    for(Node* p=head; p!=NULL; p=p->link, i++) {
        if(p->data==e & i>=start)
            return i;
    }
    return -1;
}

int find1(Element e) {
    return find2(0, e);
}
