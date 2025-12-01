#include "Ch07-01.h"

static TNode* root = NULL;

void VisitNode(TNode* n){
    printf("%d ", n->data);
}

void insert_bst(TNode* nroot, TNode* p){
    if (p->data < nroot->data) {
        if (nroot->left == NULL) nroot->left = p;
        else insert_bst(nroot->left, p);
    }
    else if (p->data > nroot->data) {
        if (nroot->right == NULL) nroot->right = p;
        else insert_bst(nroot->right, p);
    }
}

void build_tree(void){
    TElement temp;
    while (1) {
        printf("데이터 값:");
        scanf("%d", &temp);
        if (temp == 0) {
            printf("트리 완성\n");
            return;
        }
        TNode* p = creat_node(temp, NULL, NULL);
        if (root == NULL)
            root = p;
        else
            insert_bst(root, p);
    }
}

void inorder(TNode* p){
    if (p != NULL) {
        inorder(p->left);
        VisitNode(p);
        inorder(p->right);
    }
}

void insert_node(void) {
    TElement temp;
    printf("데이터 값:");
    scanf("%d", &temp);

    TNode* p = creat_node(temp, NULL, NULL);
    if (root == NULL)
        root = p;
    else
        insert_bst(root, p);
}

TNode* search_bst(TNode* nroot, TElement temp){
    if (nroot == NULL) return NULL;
    if (nroot->data == temp) return nroot;
    else if (temp < nroot->data)
        return search_bst(nroot->left, temp);
    else
        return search_bst(nroot->right, temp);
}

void search_node(void){
    TNode* searchNode;
    TElement temp;
    printf("데이터 값:");
    scanf("%d", &temp);
    searchNode = search_bst(root, temp);
    if (searchNode == NULL)
        printf("찾는 값이 트리에 없습니다.\n");
    else
        printf("찾는 값이 트리에 있습니다.\n");
}

TNode* delete_bst(TNode* nroot, TElement temp) {
    TNode* n = nroot;
    TNode* parent = NULL;

    while (n != NULL && temp != n->data) {
        parent = n;
        if (temp < n->data)
            n = n->left;
        else
            n = n->right;
    }
    if (n == NULL) return nroot;

    // case 1: 자식이 없는 단말 노드
    if (n->left == NULL && n->right == NULL) {
        if (parent == NULL) {      // 루트가 단말 노드였음
            nroot = NULL;
        } else {
            if (parent->left == n) parent->left = NULL;
            else parent->right = NULL;
        }
        free(n);
    }
    // case 2: 자식이 1개인 노드
    else if (n->left == NULL || n->right == NULL) {
        TNode* child = (n->left != NULL) ? n->left : n->right;
        if (parent == NULL) {
            nroot = child;
        } else {
            if (parent->left == n) parent->left = child;
            else parent->right = child;
        }
        free(n);
    }
    // case 3: 자식이 2개인 노드
    else {
        TNode* succ_parent = n;
        TNode* succ = n->right;
        while (succ->left != NULL) {
            succ_parent = succ;
            succ = succ->left;
        }
        n->data = succ->data;
        if (succ_parent->left == succ)
            succ_parent->left = succ->right;
        else
            succ_parent->right = succ->right;
        free(succ);
    }

    return nroot;
}

void delete_node(void){
    TElement temp;
    printf("삭제할 데이터 값:");
    scanf("%d", &temp);
    root = delete_bst(root, temp);
}

int main(void){
    int menu;

    while (1) {
        printf("1.트리구성 2.노드추가 3.노드 삭제 4.탐색 5.종료\n");
        scanf("%d", &menu);
        switch (menu) {
        case 1:
            build_tree();
            inorder(root);
            printf("\n");
            break;
        case 2:
            insert_node();
            inorder(root);
            printf("\n");
            break;
        case 3:
            delete_node();
            inorder(root);
            printf("\n");
            break;
        case 4:
            search_node();
            break;
        case 5:
            printf("프로그램을 종료합니다.\n");
            exit(0);
        default:
            printf("잘못된 입력입니다.\n");
        }
    }
}
