#include <iostream>
#include <stack>

using namespace std;

class BTreeNode {
public:
    BTreeNode** p; //서브트리에 대한 포인터
    int* k; //키 값
    int n; // 한 노드 내의 키 값의 개수
};

//새로운 BTreeNode를 생성하는 메소드
BTreeNode* getNode(int m)
{
    BTreeNode* newNode = new BTreeNode();
    /*원래 k는 최대 m-1의 갯수만큼의 값을 가지지만
    인덱스 사용을 편하기 위해 m의 크기로 만듦(k[0]은 사용안함)
    */
    newNode->k = new int[m];
    //p는 최대 m만큼의 갯수를 가질 수 있다.
    newNode->p = new BTreeNode * [m];
    newNode->n = 0;
    //포인터 초기화
    for (int i = 0; i < m; ++i)
    {
        newNode->p[i] = NULL;
    }
    return newNode;
}

void insertBT(BTreeNode*& T, int m, int newKey)
{
    /*T가 null이면 노드를 만들고, 키 값의 갯수 1로 n을 초기화 한 후 키 값을 k[1]에 넣는다.
    */
    if (T == NULL)
    {
        T = getNode(m);
        T->k[1] = newKey;
        T->n = 1;
        return;
    }

    int i;
    //stack은 거쳐온 노드들 되돌아가기 위해 사용한다.
    stack<BTreeNode*> nodeStack;
    /* - x는 현재 노드를 가리킨다.
       - tempNode는 키의 허용 숫자를 넘어갈 때 split을 위한
         임시 노드이다.
       - y는 split 후 새로 생길 노드이다. 스택에서 뽑아낸
         이전 노드의 포인터에 연결할 것이다.
    */
    BTreeNode* x = T;
    BTreeNode* tempNode = NULL;
    BTreeNode* y = NULL;

    /*삽입하려는 키 값이 이미 존재하면 함수 종료.
    그렇지 않다면 터미널 노드일때(다음 포인터를 갖고 있지 않음)
    까지 내려간다.
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

    //마지막에 스택에 넣은 터미널 노드를 뺀다.
    x = nodeStack.top();
    nodeStack.pop();

    do {
        //만약 노드에 키를 넣을 자리가 남아있다면 단순삽입 후 끝낸다.
        if (x->n < m - 1)
        {
            int i = x->n;
            //삽입하려는 키보다 큰 값들을 뒤로 밀어준다.
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
        만약 키를 넣을 자리가 없다면
        (키의 갯수가 m-1보다 작지 않다면)
        더 이상 키를 넣을 수 없으니 split 해야 한다.
        */
        else
        {
            //tempNode는 기존 노드들보다 m이 하나 더 크다.
            tempNode = getNode(m + 1);
            /*
            쪼개기 전의 노드의 모든 키와 포인터를 tempNode에 복사
            하여 넣는다 (키는 인덱스 1부터).
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
            삽입하기 원하는 newKey를 tempNode에 넣어야 하는데,
            만약에 newKey가 가장 큰 값이 아니라면 기존에 들어있는
            키와 포인터들을 뒤로 밀어줘야 한다.
            */
            int i = x->n;
            while (i >= 1 && tempNode->k[i] > newKey)
            {
                tempNode->k[i + 1] = tempNode->k[i];
                tempNode->p[i + 1] = tempNode->p[i];
                i--;
            }
            /*
            찾은 자리에 키를 집어넣고, 키의 오른쪽
            포인터에는 y를 연결해준다.
            만약 첫번째 실행되는 반복문이라면 y는 null일 것이다.
            여러번 반복문이 진행됐다면, (즉 단말노드가 아닌 곳에서
            연쇄적으로 스플릿이 일어나고 있다면)
            y는 이전 단계에서 새로 만들어진 노드이다.
            */
            tempNode->k[i + 1] = newKey;
            tempNode->p[i + 1] = y;
            tempNode->n++;

            /*
            tempNode의 중간 값을 찾는다.
            ex) n이 4이면 4/2+1=3; 3번째 키가 중간 값,
                n이 3이면 3/2+1=2; 2번째 키가 중간 값..
            */
            int center = (tempNode->n / 2) + 1;

            /*
            중간 값이 되는 키는 새로운 노드나 혹은 부모노드에
            새로운 삽입하는 키가 된다. 그래서 newKey를 중간값으로
            덮는다.
            */
            newKey = tempNode->k[center];


            //y는 split할 때 새로 만들어지는 노드이다.
            //tempNode의 중간값 이후의 키와 포인터들만 넣어준다.
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

            //x는 y가 갈라져나간 기존 노드이다. tempNode에서
            //중간 값 이전의 키와 포인터들만 넣어준다.
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
            키를 넣을 때 자리가 없어서 split을 한 상태에서,
            만야에 스택이 비어있지 않았다면 중간값을 부모 노드에
            넣어주러 가야한다.
            그래서 다시 반복문을 돌아 newKey(중간값)을 넣는 동작을
            반복해야 한다.
            */
            if (!nodeStack.empty())
            {
                x = nodeStack.top();
                nodeStack.pop();
            }
            /*
            스택이 비어있다면 루트 노드까지 왔지만 키를 넣을
            자리가 없다는 뜻이므로 새로 노드를 만들어야 한다.
            그리고 finished 플래그 값을 true로 바꾼다.
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
    i가 루트노드 키의 갯수보다 작을 동안 모든 포인터에 대해
    먼저 inorder를 재귀로 실행한다.
    마지막에 키 오른쪽 포인터(즉 마지막 키의 포인터)에 대해
    한번 inorder를 실행해준다.
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
    cout << "m이 3일 때 삽입 --------" << endl;
    insertBT(T, 3, 30); inorderBT(T);
    //...............
}