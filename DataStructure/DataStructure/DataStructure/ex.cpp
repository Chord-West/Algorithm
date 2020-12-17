#include <iostream>
#include <stack>

using namespace std;

class BTreeNode {
public:
    BTreeNode** p; //����Ʈ���� ���� ������
    int* k; //Ű ��
    int n; // �� ��� ���� Ű ���� ����
};

//���ο� BTreeNode�� �����ϴ� �޼ҵ�
BTreeNode* getNode(int m)
{
    BTreeNode* newNode = new BTreeNode();
    /*���� k�� �ִ� m-1�� ������ŭ�� ���� ��������
    �ε��� ����� ���ϱ� ���� m�� ũ��� ����(k[0]�� ������)
    */
    newNode->k = new int[m];
    //p�� �ִ� m��ŭ�� ������ ���� �� �ִ�.
    newNode->p = new BTreeNode * [m];
    newNode->n = 0;
    //������ �ʱ�ȭ
    for (int i = 0; i < m; ++i)
    {
        newNode->p[i] = NULL;
    }
    return newNode;
}

void insertBT(BTreeNode*& T, int m, int newKey)
{
    /*T�� null�̸� ��带 �����, Ű ���� ���� 1�� n�� �ʱ�ȭ �� �� Ű ���� k[1]�� �ִ´�.
    */
    if (T == NULL)
    {
        T = getNode(m);
        T->k[1] = newKey;
        T->n = 1;
        return;
    }

    int i;
    //stack�� ���Ŀ� ���� �ǵ��ư��� ���� ����Ѵ�.
    stack<BTreeNode*> nodeStack;
    /* - x�� ���� ��带 ����Ų��.
       - tempNode�� Ű�� ��� ���ڸ� �Ѿ �� split�� ����
         �ӽ� ����̴�.
       - y�� split �� ���� ���� ����̴�. ���ÿ��� �̾Ƴ�
         ���� ����� �����Ϳ� ������ ���̴�.
    */
    BTreeNode* x = T;
    BTreeNode* tempNode = NULL;
    BTreeNode* y = NULL;

    /*�����Ϸ��� Ű ���� �̹� �����ϸ� �Լ� ����.
    �׷��� �ʴٸ� �͹̳� ����϶�(���� �����͸� ���� ���� ����)
    ���� ��������.
    */

    do {
        i = 1; //search index
        while (i <= x->n && newKey > x->k[i])
            i = i + 1;
        if (i <= x->n && newKey == x->k[i])
            return;
        nodeStack.push(x);
    } while ((x = x->p[i - 1] != nullptr))

        bool finished = false;

    //�������� ���ÿ� ���� �͹̳� ��带 ����.
    x = nodeStack.top();
    nodeStack.pop();

    do {
        //���� ��忡 Ű�� ���� �ڸ��� �����ִٸ� �ܼ����� �� ������.
        if (x->n < m - 1)
        {
            int i = x->n;
            //�����Ϸ��� Ű���� ū ������ �ڷ� �о��ش�.
            while (i >= 1 && x->k[i] > newKey)
            {
                x->k[i + 1] = x->k[i];
                x->p[i + 1] = x->p[i];
                i--;
            }
            x->k[i + 1] = newKey;
            x->p[i + 1] = y;
            x->n = x->n + 1;

            finished = true;
        }
        /*
        ���� Ű�� ���� �ڸ��� ���ٸ�
        (Ű�� ������ m-1���� ���� �ʴٸ�)
        �� �̻� Ű�� ���� �� ������ split �ؾ� �Ѵ�.
        */
        else
        {
            //tempNode�� ���� ���麸�� m�� �ϳ� �� ũ��.
            tempNode = getNode(m + 1);
            /*
            �ɰ��� ���� ����� ��� Ű�� �����͸� tempNode�� ����
            �Ͽ� �ִ´� (Ű�� �ε��� 1����).
            */
            for (int i = 0; i <= x->n; ++i)
            {
                tempNode->p[i] = x->p[i];
                if (i >= 1)
                {
                    tempNode->k[i] = x->k[i];
                    tempNode->n++;
                }
            }
            /*
            �����ϱ� ���ϴ� newKey�� tempNode�� �־�� �ϴµ�,
            ���࿡ newKey�� ���� ū ���� �ƴ϶�� ������ ����ִ�
            Ű�� �����͵��� �ڷ� �о���� �Ѵ�.
            */
            int i = x->n;
            while (i >= 1 && tempNode->k[i] > newKey)
            {
                tempNode->k[i + 1] = tempNode->k[i];
                tempNode->p[i + 1] = tempNode->p[i];
                i--;
            }
            /*
            ã�� �ڸ��� Ű�� ����ְ�, Ű�� ������
            �����Ϳ��� y�� �������ش�.
            ���� ù��° ����Ǵ� �ݺ����̶�� y�� null�� ���̴�.
            ������ �ݺ����� ����ƴٸ�, (�� �ܸ���尡 �ƴ� ������
            ���������� ���ø��� �Ͼ�� �ִٸ�)
            y�� ���� �ܰ迡�� ���� ������� ����̴�.
            */
            tempNode->k[i + 1] = newKey;
            tempNode->p[i + 1] = y;
            tempNode->n++;

            /*
            tempNode�� �߰� ���� ã�´�.
            ex) n�� 4�̸� 4/2+1=3; 3��° Ű�� �߰� ��,
                n�� 3�̸� 3/2+1=2; 2��° Ű�� �߰� ��..
            */
            int center = (tempNode->n / 2) + 1;

            /*
            �߰� ���� �Ǵ� Ű�� ���ο� ��峪 Ȥ�� �θ��忡
            ���ο� �����ϴ� Ű�� �ȴ�. �׷��� newKey�� �߰�������
            ���´�.
            */
            newKey = tempNode->k[center];


            //y�� split�� �� ���� ��������� ����̴�.
            //tempNode�� �߰��� ������ Ű�� �����͵鸸 �־��ش�.
            y = getNode(m);
            for (int i = center; i <= tempNode->n; ++i)
            {
                y->p[i - (center)] = tempNode->p[i];
                if (i >= center + 1)
                {
                    y->k[i - (center)] = tempNode->k[i];
                    y->n++;
                }
            }

            //x�� y�� ���������� ���� ����̴�. tempNode����
            //�߰� �� ������ Ű�� �����͵鸸 �־��ش�.
            x->n = 0;
            for (int i = 0; i <= m - 1; ++i)
            {
                if (i < center)
                {
                    x->p[i] = tempNode->p[i];
                    if (i >= 1)
                    {
                        x->k[i] = tempNode->k[i];
                        x->n++;
                    }
                }
            }

            /*
            Ű�� ���� �� �ڸ��� ��� split�� �� ���¿���,
            ���߿� ������ ������� �ʾҴٸ� �߰����� �θ� ��忡
            �־��ַ� �����Ѵ�.
            �׷��� �ٽ� �ݺ����� ���� newKey(�߰���)�� �ִ� ������
            �ݺ��ؾ� �Ѵ�.
            */
            if (!nodeStack.empty())
            {
                x = nodeStack.top();
                nodeStack.pop();
            }
            /*
            ������ ����ִٸ� ��Ʈ ������ ������ Ű�� ����
            �ڸ��� ���ٴ� ���̹Ƿ� ���� ��带 ������ �Ѵ�.
            �׸��� finished �÷��� ���� true�� �ٲ۴�.
            */
            else
            {
                T = getNode(m);
                T->k[1] = newKey;
                T->p[0] = x;
                T->p[1] = y;
                T->n = 1;
                finished = true;
            }
        }
    } while (!finished);
}
void inorderBT(BTreeNode*& T)
{
    /*
    i�� ��Ʈ��� Ű�� �������� ���� ���� ��� �����Ϳ� ����
    ���� inorder�� ��ͷ� �����Ѵ�.
    �������� Ű ������ ������(�� ������ Ű�� ������)�� ����
    �ѹ� inorder�� �������ش�.
    */
    int i;
    for (i = 0; i < T->n; i++)
    {
        if (T->p[i] != nullptr)
            inorderBT(T->p[i]);

        cout << T->k[i + 1] << " ";
    }
    if (T->p[i] != nullptr)
        inorderBT(T->p[i]);
}
int main()
{
    BTreeNode* T = NULL;
    cout << "m�� 3�� �� ���� --------" << endl;
    insertBT(T, 3, 30); inorderBT(T);
    //...............
}