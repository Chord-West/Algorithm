/* 20175161 김현서 BST 과제 */


#include<iostream>
#include<string>
#include<climits>

using namespace std;

class Node {
public:
	Node* right;
	Node* left;
	int key;
	Node() { // 초기 값
		key = INT_MIN;
		right = NULL;
		left = NULL;
	}
};
// 트리
class Tree {
private:
	Node* root; //root node
public:
	Tree() { root = NULL; }
	Node* insertBST(Node* T, int newKey);
	Node* getNode();
	void deleteBST(Node* T, int deletekey);
	Node* searchParentBST(Node* T, int newKey, Node* p);
	Node* searchBST(Node* T, int newKey);
	int height(Node* T);
	int noNode(Node* T);
	Node* maxNode(Node* T);
	Node* minNode(Node* T);
	void inorderBST(Node* T);
};

int nodecount = 0; //노드 개수

Node* Tree::getNode() {
	return new Node;
}

Node* Tree::insertBST(Node* T, int newKey) {
	Node* newNode = getNode();
	newNode->key = newKey;
	newNode->left = NULL;
	newNode->right = NULL;
	if (T == NULL)  T = newNode;  // 없으면 newkey 삽입      
	else if (newKey < T->key)     T->left = insertBST(T->left, newKey);  // 왼쪽에 newkey삽입
	else if (newKey > T->key)    T->right = insertBST(T->right, newKey); // 오른쪽에 newkey 삽입 
	return T;
}

int Tree::height(Node* T) {
	if (T == NULL) return 0;
	else {
		int lb = height(T->left);
		int rb = height(T->right);
		return max(lb, rb) + 1;
	}
}

int Tree::noNode(Node* T) {
	if (T != NULL) {
		noNode(T->left);
		nodecount++;
		noNode(T->right);
	}
	return nodecount;
}

Node* Tree::maxNode(Node* T) {
	if (T == NULL) return T;
	else {
		while (T->right != NULL) T = T->right;
		return T;
	}
}

Node* Tree::minNode(Node* T) {
	if (T == NULL) return T;
	else {
		while (T->left != NULL)  T = T->left;
		return T;
	}
}
Node* Tree::searchBST(Node* T, int newKey) {
	Node* p = T;
	while (p != NULL) {
		if (newKey == p->key) return p;
		if (newKey < p->key) p = p->left;
		else p = p->right;
	}
	return p;
}

Node* Tree::searchParentBST(Node* T, int newKey, Node* p) {
	Node* q = NULL;
	p = T;
	while (p != NULL) {
		if (newKey == p->key) return q;
		q = p;
		if (newKey < p->key) p = p->left;
		else p = p->right;
	}
	return q;
}
void Tree::deleteBST(Node* T, int newKey) {
	Node* p = searchBST(T, newKey);  //삭제할 노드
	Node* q = searchParentBST(T, newKey, p); //삭제할 노드의 부모노드
	if (q == NULL) T = NULL; //루트노드만 있는 경우
	else if (p == NULL) cout << "트리가 비어있습니다"; //삭제할 원소가 없음
	else {
		if (p->left == NULL && p->right == NULL) { // 리프노드
			if (q->left == p)	q->left = NULL;
			else	 q->right = NULL;
		}
		else if (p->left == NULL || p->right == NULL)  // 삭제할 노드의 차수가 1인경우
		{
			if (p->left != NULL) {
				if (q->left == p) q->left = p->left;
				else q->right = p->left;
			}
			else {
				if (q->left == p) q->left = p->right;
				else q->right = p->right;
			}
		}
		else if (p->left != NULL && p->right != NULL)  //삭제할 노드의 차수가 2인경우
		{
			Node* r;
			string flag = "";
			if (height(p->left) > height(p->right)) {
				r = maxNode(p->left);
				flag = "LEFT";
			}
			else if (height(p->left) < height(p->right)) {
				r = minNode(p->right);
				flag = "RIGHT";
			}
			else {
				nodecount = 0;
				int node_l = noNode(p->left);
				nodecount = 0;
				int node_r = noNode(p->right);
				if (node_l >= node_r) {
					r = maxNode(p->left);
					flag = "LEFT";
				}
				else {
					r = minNode(p->right);
					flag = "RIGHT";
				}
			}
			if (flag == "LEFT") {
				deleteBST(p, r->key);
				p->key = r->key;
			}
			else {
				deleteBST(p, r->key);
				p->key = r->key;
			}
		}
	}
}


void Tree::inorderBST(Node* T) {
	if (T != NULL) {
		inorderBST(T->left);
		if (T->key != INT_MIN) cout << T->key << " ";
		inorderBST(T->right);
	}
}

int main() {
	Tree* tree = new Tree;
	Node* T = new Node();
	tree->insertBST(T, 25);
	tree->inorderBST(T); cout << endl;
	tree->insertBST(T, 500);
	tree->inorderBST(T); cout << endl;
	tree->insertBST(T, 100);
	tree->inorderBST(T); cout << endl;
	tree->insertBST(T, 999);
	tree->inorderBST(T); cout << endl;

	tree->deleteBST(T, 25);
	tree->inorderBST(T); cout << endl;
	tree->deleteBST(T, 500);
	tree->inorderBST(T); cout << endl;
	tree->deleteBST(T, 100);
	tree->inorderBST(T); cout << endl;
	tree->deleteBST(T, 999);
	tree->inorderBST(T); cout << endl;

	tree->insertBST(T, 25);
	tree->inorderBST(T); cout << endl;
	tree->insertBST(T, 500);
	tree->inorderBST(T); cout << endl;
	tree->insertBST(T, 100);
	tree->inorderBST(T); cout << endl;
	tree->insertBST(T, 999);
	tree->inorderBST(T); cout << endl;

	tree->deleteBST(T, 999);
	tree->inorderBST(T); cout << endl;
	tree->deleteBST(T, 100);
	tree->inorderBST(T); cout << endl;
	tree->deleteBST(T, 500);
	tree->inorderBST(T); cout << endl;
	tree->deleteBST(T, 25);
	tree->inorderBST(T); cout << endl;

}