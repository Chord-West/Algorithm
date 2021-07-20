# Queue
'''큐는 엔큐(Enqueue) 와 디큐(Dequeue) 로 구성
Enqueue: 데이터 인풋
Dequeue: 데이터 아웃풋
1. 가장 먼저 삽입한 데이터가 가장 먼저 출력

2. FIFO(First - in First - out), LILO(Last - in Last - out) 구조

3. 멀티 태스킹을 위한 프로세스 스케쥴링 방식 구현에서 자주 사용
'''

class Queue:
    def __init__(self):
        self.queue_list = []
    def enqueue(self, data):
        self.queue_list.append(data)

    def dequeue(self):
        if not self.queue_list:
            return False
        else:
            res = self.queue_list[0]
            del self.queue_list[0]
            return res

myQueue = Queue()

for a in range(10):
    myQueue.enqueue(a)

print(myQueue.queue_list)
for a in range(11):
    print(myQueue.dequeue())