#include "Ch07-01.h"

static TNode* root = NULL;

void VisitNode(TNode* n){
    printf("%d ", n->data);
}
void insert_bst(TNode nroot, TNode* p){
    if(p->data < nroot ->data){
        if(nroot -> left == NULL) nroot -> left = p;
        else insert_bst(nroot->left, p);
    }
    else if(p->data > nroot->data) {
        if(nroot->right == NULL) nroot -> right = p;
        else insert_bst(nroot->right,p);
    }
    free(p);
}
void build_trre(){
    TElement temp;
    while(1) {
        printf("데이터 값:");
        scanf("%d", &temp);
        if(temp == 0){
            printf("트리 완성\n");
            return;
        }
        TNode* p = creat_node(temp, NULL, NULL);
        if(root == NULL)
            root = p;
        else {
            insert_bst(root, p);
        }
    }
}
void inorder(TNode* p){
    if (p != NULL) {
        inorder(p->left);
        VisitNode(p);
        inorder(p->right);
    }
}

void insert_node() {
    TElement temp;
    printf("데이터 값:");
    scanf("%d", &temp);
    
    TNode* p = creat_node(temp, NULL, NULL);
        if(root == NULL)
            root = p;
        else {
            insert_bst(root, p);
}

TNode* search_bst(TNode* nroot, TElement temp){
    if(nroot == NULL) return NULL;
    if(nroot->data == temp) return nroot;
    else if (nroot->data < temp)
        search_bst(nroot->left, temp);
    else
        return search_bst(nroot->right, temp);
}

void search_node(){
    TNode searchNode;
    TElement temp;
    printf("데이터 값:");
    scanf("%d", &temp);
    searchNode = search_bst(root, TElement temp);
    if(searchNode == NULL)
        printf("찾는 값이 트리에 없습니다.\n");
    else
        printf("찾는 값이 트리에 있습니다.\n");
}

TNode* delete_bst(TNode nroot, TElement temp) {
    TNode* n = nroot;
    TNode* parent = NULL;
    
    while(n != NULL && temp != n->data) {
        parent = n;
        n = (temp < n->data) ? n->left->right;
    }
    if(n == NULL) return nroot;
    
    if(n->left == NULL && n -> right == NULL) { // case1에 해당하는 경우
            if(parent == NULL) root = NULL;
            else{
                if(parent->left == n) parent->left=NULL;
                else parent->right = NULL;
            }
            free(n);
    }
    else if(n->left == NULL || n->right == NULL) { // case2에 해당하는 경우
        
    }
    else { // case3에 해당하는 경우
        
    }
}
void delete_node(){
    TNode searchNode;
    TElement temp;
    printf("삭제할 데이터 값:");
    scanf("%d", &temp);
    delete_bst(root, temp);
}

int main(void){
    int menu;
    
    while(1){
        printf("1.트리구성 2.노드추가 3.노드 삭제 4.탐색 5.종료");
        scanf("%d", &menu);
        switch(menu){
        case 1: build_tree();
                    inorder(root);
                    break;
        case 2: insert_node();
                    inorder(root);
                    break;
        case 3: delete_node();
                    break;
        case 4: search_node();
                    break;
        case 5: printf("프로그램을 종료합니다.\n");
                    exit(1);
        default:
        }
    }
}
