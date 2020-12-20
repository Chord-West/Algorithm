/*
 * File processing, 2020
 * btree.cpp
 * implementation of B-tree
 */

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stack>

using namespace std;
 /**
  * BTNode represents a single node in B-tree.
  */

typedef class BTNode {
public:
	int	n; // �ڷ� ����
	int * K; // Ű��
	class BTNode** P; // ��� ����Ʈ�� �迭
} BTNode;
typedef BTNode* BTree;

BTNode* getBTNode(int m);
void insertBT(BTree* T, int m, int newKey);
void deleteBT(BTree* T, int m, int oldKey);
void inorderBT(BTree T);
BTNode* findSibling(BTNode* x, BTNode* y, int m);
/**
 * getBTNode retruns a new BTNode.
 * @param m: number of branch points in B-tree
 * @return a new BTNode
 */
BTNode* getBTNode(int m) {
	BTNode* node = new BTNode;
	node->n = 0;
	node->K = new int[m - 1]; // m-1���� ������
	node->P = new BTNode * [m]; // m���� ��� ����
	for (int i = 0; i < m; i++) {
		node->P[i] = NULL; // ������ NULL �� ó��
	}
	return node;
}

/**
 * insertBT inserts newKey into T.
 * @param T: a B-tree
 * @param m: number of branch points in B-tree
 * @param newKey: a key to insert
 */

void insertBT(BTree* T, int m, int newKey) {
	/* write your code here */
	BTNode* node = *T;
	// ��尡 ����ִ� ���
	if (node == NULL) {
		node = getBTNode(m);
		node->K[0] = newKey;
		node->n = 1;
		*T = node;
		return;
	}

	BTNode* x = *T; // newKey�� ���Ե� ��ġ Ž��
	BTNode* y = NULL;
    BTNode* tmpNode;
	stack<BTNode*> BTstack;
    
	int idx;
	while (x!=NULL) {
		idx = 0;
        for (int i = 0; i < x->n; i++) {
                if (x->K[i] < newKey) idx++;  //�б��� ������ ���ϱ�
        }
		if (idx <= x->n && x->K[idx] == newKey)  return; //�Ȱ��� Ű�� �߰�, ���� �Ұ�
		BTstack.push(x); 
        x = x->P[idx]; //������ �̵�
	} 
    
   
	bool finish = false;
	x=BTstack.top();
	BTstack.pop();

    
    while (!finish) {
        if (x->n < m - 1) //Ű ���� ���� �� ������
        {
            idx = x->n;
            // ��� ����
            for (int i = x->n; i >= 0; i--) {
                if (x->K[i] > newKey) {
                    x->K[i + 1] = x->K[i];
                    x->P[i + 2] = x->P[i + 1];
                    idx = i;
                }
            }
            x->K[idx] = newKey;
            x->P[idx + 1] = y; // �ٲ�� �� ����
            x->n = x->n + 1;
            finish = true;
        }

        else // ���Ҽ� ���� �ؾ� �ϴ� ���
        {
            tmpNode = getBTNode(m + 1); // �� ���� �ӽ� ��� ����
            for (int i = 0; i <= x->n; i++) // �����ϱ��� ��� ����
            {
                if (i < x->n)
                {
                    tmpNode->K[i] = x->K[i];
                    tmpNode->n++;
                }
                tmpNode->P[i] = x->P[i];
            }

            // �����ϱ��� �ӽ� ��� ����
            idx = x->n;
            for (int i = x->n; i >= 0; i--) {
                if (tmpNode->K[i] > newKey) {
                    tmpNode->K[i + 1] = tmpNode->K[i];
                    tmpNode->P[i + 2] = tmpNode->P[i + 1];
                    idx = i;
                }
            }
            tmpNode->K[idx] = newKey;
            tmpNode->P[idx + 1] = y;
            tmpNode->n = x->n + 1;


            int center = (tmpNode->n / 2);
            newKey = tmpNode->K[center]; // �θ� ���� ����

            y = getBTNode(m); // �и��ؼ� �����ʿ� ���� ��������� ���

            for (int i = center + 1; i <= tmpNode->n; i++) // center =1 ,  n=3
            {
                y->P[i - (center + 1)] = tmpNode->P[i]; // y�� 1,2,3 ��° ������
                if (i < tmpNode->n)
                {
                    y->K[i - (center + 1)] = tmpNode->K[i];
                    y->n++;
                }
            }

            //���ʿ� ��������� ���
            x->n = 0;
            x->K[center] = 0;
            for (int i = 0; i <= center; i++)
            {
                x->P[i] = tmpNode->P[i];
                if (i < center)
                {
                    x->K[i] = tmpNode->K[i];
                    x->n++;
                }
            }

            if (!BTstack.empty())
            {
                x = BTstack.top();
                BTstack.pop();
            }
            else
            {
                node = getBTNode(m);
                node->K[0] = newKey;
                node->P[0] = x;
                node->P[1] = y;
                node->n = 1;
                *T = node;
                finish = true;
            }
        }
    }
}



bool underflow(BTNode* x, int m) {
    if (m / 2 != 0) { 
        m++;
    }
    if (x->n < m / 2 - 1) return true;
    else return false;
}
bool existSibling(BTNode* x, BTNode* y, int m) {
    bool check = false;
    int idx;
    for (idx=0; idx < m; idx++) {
        if (y->P[idx] == x) break; // ������ ������ã��
    }
    if (m / 2 != 0) {
        m++;
    }
    if (idx - 1 >=0&&y->P[idx - 1] != NULL&&y->P[idx-1]->n>m/2-1) {
        check = true;
    }
    else if (idx + 1 <m&& y->P[idx + 1] !=NULL&&y->P[idx + 1]->n > m / 2-1) {
        check = true;
    }
    return check;
 
}

/**
 * deleteBT deletes oldKey from T.
 * @param T: a B-tree
 * @param m: number of branch points in B-tree
 * @param oldKey: a key to delete
 */
void deleteBT(BTree* T, int m, int oldKey) {
    /* write your code here */
    BTNode* x = *T; // oldKey ��ġ Ž��
    stack<BTNode*> BTstack;
    BTNode* internalNode = NULL;
    BTNode* y = NULL;
    int idx;
    while (x != NULL) {
        idx = 0;
        for (int i = 0; i < x->n; i++) {
            if (x->K[i] < oldKey) idx++;  //�б��� ������ ���ϱ�
        }
        if (idx <= x->n && x->K[idx] == oldKey)  break; //�Ȱ��� Ű�� �߰�,
        BTstack.push(x);
        x = x->P[idx]; //������ �̵�
    }
    if (x == NULL) return; // ������ Ű �߰� ���� ��
    bool finish = false;
    bool leaf = true;
    // �͹̳� ������� Ȯ��
    for (int i = 0; i <= x->n; i++) {
        if (x->P[i] != NULL) {
            leaf = false;  //NULL �� �Ѱ��� ������ ���γ��
            break;
        }
    }

    if (!leaf) { //���� �����
        internalNode = x;
        BTstack.push(x);
        x = x->P[idx + 1];
        while (x != NULL) {
            BTstack.push(x);
            x = x->P[0];
        }
        x = BTstack.top();// ����Ű
        BTstack.pop();
        int tmp = internalNode->K[idx];
        internalNode->K[idx] = x->K[0];
        x->K[0] = tmp;
        // ����Ű�� ��ȯ �� ������
        x->K[0] = NULL;
        x->n--;
    }
    else { //�͹̳� �����
       //���� 
        for (int i = 0; i < x->n; i++) {
            if (x->K[i] == oldKey) {
                x->n--;
                x->K[i] = NULL;
                x->P[i + 1] = NULL;
                break;
            }
        }

    }


    y = getBTNode(m);  //x�� �θ��� 
    if (!BTstack.empty()) {
        y = BTstack.top();
        BTstack.pop();
    }
    while (!finish) {
        if (*T == x || !underflow(x, m)) { //���̻� ��������
            for (int i = 1; i <= x->n; i++) { // �� �������� ����
                if (x->K[i] > oldKey) {
                    x->K[i - 1] = x->K[i];
                    x->P[i] = x->P[i + 1];
                    idx = i;
                }
            }
            x->K[idx] = NULL;
            x->P[idx + 1] = NULL;
            finish = true;
        }

        else if (existSibling(x, y, m)) // �����ִ�  ������� �����ϸ�
        {
            //��й�
            int idx;
            int i;
            BTNode* sibling = findSibling(x, y, m);  // ���� ����
            BTNode* tmpNode = getBTNode(2 * m);
            bool left = false; // ������ �������϶�

            for (i = 0; i < m; i++) {
                if (y->P[i] == sibling) {
                    for (idx = 0; idx < sibling->n; idx++) {
                        tmpNode->K[idx] = sibling->K[idx];
                        tmpNode->n++;
                    }
                    tmpNode->K[idx] = y->K[i];
                    tmpNode->n++;
                    break;
                }
                else if (y->P[i] == x) {
                    tmpNode->K[0] = y->K[i];
                    tmpNode->n++;
                    for (idx = 0; idx < sibling->n; idx++) {
                        tmpNode->K[idx + 1] = sibling->K[idx];
                        tmpNode->n++;
                    }
                    left = true;
                    break;
                }
            }
            int center = (tmpNode->n / 2);
            y->K[i] = tmpNode->K[center]; //�߾Ӱ� �ٲٱ�
            sibling = getBTNode(m);
            x = getBTNode(m);
            if (!left) {
                for (int j = center + 1; j < tmpNode->n; j++)
                {
                    x->K[j - (center + 1)] = tmpNode->K[j];
                    x->n++;
                }
                for (int j = 0; j < center; j++)
                {
                    sibling->K[j] = tmpNode->K[j];
                    sibling->n++;
                }
                y->P[i] = sibling;
                y->P[i + 1] = x;
            }
            else { //������ �������϶�
                for (int j = center + 1; j < tmpNode->n; j++)
                {
                    sibling->K[j - (center + 1)] = tmpNode->K[j];
                    sibling->n++;
                }

                for (int j = 0; j < center; j++)
                {
                    x->K[j] = tmpNode->K[j];
                    x->n++;
                }
                y->P[i] = x;
                y->P[i + 1] = sibling;
            }

            finish = true;
        }
        else // ���� �̿ϼ� 
        {
            //��й�

        }

    }


}

BTNode* findSibling(BTNode* x, BTNode* y, int m) {
    int idx; //y �� �θ�
    for (idx = 0; idx < m; idx++) {
        if (y->P[idx] == x) break;
    }
    if (idx - 1 >= 0 && y->P[idx - 1]->n > m / 2 - 1) {
        return  y->P[idx - 1];
    }
    else if (idx + 1 < m && y->P[idx + 1]->n > m / 2 - 1) {
        return  y->P[idx + 1];
    }
}
/**
 * inorderBT implements inorder traversal in T.
 * @param T: a B-tree
 */
void inorderBT(BTree T) {
	if (T == NULL) return;
    int i;
	for ( i = 0; i < T->n; i++) {
		inorderBT(T->P[i]);
		cout << T->K[i]<<" ";
	}
	inorderBT(T->P[i]);
}

int main() {
	/* do not modify the code below */

	int insertTestCases[] = { 40, 11, 77, 33, 20, 90, 99, 70, 88, 80, 66, 10, 22, 30, 44, 55, 50, 60, 100, 28, 18, 9, 5, 17, 6, 3, 1, 4, 2, 7, 8, 73, 12, 13, 14, 16, 15, 25, 24, 28, 45, 49, 42, 43, 41, 47, 48, 46, 63, 68, 61, 62, 64, 69, 67, 65, 54, 59, 58, 51, 53, 57, 52, 56, 83, 81, 82, 84, 75, 89 };
	//int deleteTestCases[] = { 66, 10, 22, 30, 44, 55, 50, 60, 100, 28, 18, 9, 5, 17, 6, 3, 1, 4, 2, 7, 8, 73, 12, 13, 14, 16, 15, 25, 24, 28, 40, 11, 77, 33, 20, 90, 99, 70, 88, 80, 45, 49, 42, 43, 41, 47, 48, 46, 63, 68, 53, 57, 52, 56, 83, 81, 82, 84, 75, 89, 61, 62, 64, 69, 67, 65, 54, 59, 58, 51 };

	BTree T = NULL;

	for (int tC : insertTestCases) { insertBT(&T, 3, tC);  inorderBT(T); printf("\n"); }
	//for (int tC : deleteTestCases) { deleteBT(&T, 3, tC); inorderBT(T); printf("\n"); }

    T = NULL;

	for (int tC : insertTestCases) { insertBT(&T, 4, tC); inorderBT(T); printf("\n"); }
	//for (int tC : deleteTestCases) { deleteBT(&T, 4, tC); inorderBT(T); printf("\n"); }

    T = NULL;


    cout <<endl<< "�ܼ�����, ����Ű�� �ٲٱ�, ����ұ��� ����" << endl<<"���� ������ �б��ϴ� �������� �������� ���� "<<endl<<endl;

    int insertTestCases2[] = { 40, 11, 77,33,20,90,99 };
    int deleteTestCases2[] = { 40,77,11,20,33,99,90 };
    for (int tC : insertTestCases2) { insertBT(&T, 3, tC);     inorderBT(T); printf("\n"); }
    for (int tC : deleteTestCases2) { deleteBT(&T, 3, tC); inorderBT(T); printf("\n"); }
    
 
   
  }