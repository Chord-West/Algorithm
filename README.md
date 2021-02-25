# Algorithm



### 유클리드 호제법 

> 유클리드 호제법은 2개의 자연수의 **최대공약수**`(Greatest Common Divisor)`를 구하는 알고리즘의 하나
>
> 2개의 자연수 a,b에 대해서 a를 b로 나누 나머지를 r이라 하면 **(단, a>b)**, a와 b의 최대고양수는 b와 r의 
>
> 최대공약수와 같다.

- 그림설명 

  - ex ) 106와 16의 최대공약수 구하기 - **GCD( 106 , 16 )**

    ![image](https://user-images.githubusercontent.com/50789483/108161488-85abdf80-712e-11eb-8b6a-3f3279b76725.png)

- 응용 

  - **최소공배수** `(Least Common Multiple)`은 a와 b의 공통된 배수 가운데 최소값을 의미한다.

    최소공배수는 주어진 수의 a,b의 곱에서 a,b의 최대공약수를 나누어 준것과 같다

    즉, 유클리드 호제법을 사용해 최대공약수를 구한 다음, x와 y의 곱한 값을 나눠주면 최소공배수를 

    구할 수 있다
    
    

- 코드

  ```python
  import math
  math.gcd(a,b) # 내장함수 math를 통해 사용도 가능
  
  def gcd(a,b):
      while b!=0:
          r = a%b
          a,b = b,r
      return a
  
def lcm(a,b):
      return a*b // gcd(a,b)
  ```
  
  





### 자료구조

#### 	- 스택 (Stack)



#### - 힙 ( Heap )

> Heap 이란 자료구조 형태 중 하나로서 우선순위 쿠를 위해 만들어진 구조이다.
>
> 코딩 테스트 문제 중 최솟값 , 혹은 최댓값을 계속해서 호출해야 하는 상황인 경우 **Heap 구조를 이용하여 **
>
> **구현하면 시간측면에서 굉장히 효율적인 구현이 가능**하다.

- 코드 구현

  ``` python
  # heapq 모듈을 이용하요 힙 자료구조를 사용할 수 있다. heapq 는 내장 모듈이므로 따로 설치가 필요하지 않는다. 기본적으로 Min-priority-queue 구조를 가지고 있다.
  import heapq
  
  
  # 기존 배열을 Heap 구조로 - heapify()
  testheap = [1,3,2,6,8,0,6]
  heap.heapify(testheap)
  print(testheap)
  # 프린트의 결과값 => Heap구조로 변환
  [0,3,1,6,8,2,6]
  
  
  # Heap 에 요소 추가하기 - heappush(배열이름, 요소
  testheap = [] 
  heapq.heappush(testheap, 3) 
  heapq.heappush(testheap, 5) 
  heapq.heappush(testheap, 1) 
  heapq.heappush(testheap, -3) 
  print(testheap)
  # print 결과값 => 
  [-3, 1, 3, 5]
  
  # Heap 요소를 삭제하기 - heappop(배열이름)
  testheap = []
  heapq.heappush(testheap, 3)
  heapq.heappush(testheap, 5)
  heapq.heappush(testheap, 1)
  heapq.heappush(testheap, -3) 
  heapq.heappop(testheap)
  heapq.heappop(testheap) 
  print(testheap) 
  # print 결과값 => 
  [3, 5]
  
  # MaxHeap 구현하기
  a = [3,5,2,4,1] 
  testheap = [] 
  for i in a: 
      heapq.heappush(testheap, (-i,i))
  
  
  ```

  





#### 	- 딕셔너리 (dictionary)

> : 해시 테이블 (hash table) 자료 구조 기반으로 하는 `dictionary`는 키(key)와 값(value)으로 이루어진 여러 쌍의 데이터를 담아 둘 때 사용



### **DP (동적 계획법)**


> :  다음 조건을 만족할 때 사용가능
>
> - 최적 부분 구조 (Optimal Substructre)ㅇ 문제의 답을 모아서 큰 문제를 해결 가능
> - 중복되는 부분 문제 (Overlapping Subproblem)
>    - 동일한 작은 문제를 반복적으로 해결해야 함
> - 탑다운, 보텀업 방식 존재
> - 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식 ( 반복문 사용)
>  - 결과 저장용 리스트는 DP 테이블이라고 부름



##### 메모이제이션(Memoization) - 탑다운(하향식)

- 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나

- 한 번 계산한 결과를 메모리 공간에 메모하는 기법

  - 같은 문제를 다시 호출하면 메모 했던 결과를 그대로 가져옴

  - 값을 기록해 놓는다는 점에서 **`캐싱(Caching)`** 이라고도 한다.

    

- **피보나치 수열**

  : 프로그래밍에서는 수열을 배열이나 리스트를 이용해 표현

  

  - 피보나치 수열의 시간 복잡도 분석

    : 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도는  **`O(2^N)`** 

    

  - 피보나치 수열 : 탑다운 다이나믹 프로그래밍 소스코드

     - 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 **`O(N)`**

     ```python
     # 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
     d = [0] * 100
     # 피보나치 함수 (Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
     def fibo(x):
         # 종료 조건(1 혹은 2일 때 1을 반환)
         if x == 1 or x==2:
             return 1
         # 이미 계산한 적 있는 문제라면 그대로 반환
         if d[x] !=0:
             return d[x]
         # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
         d[x] = fibo(x-1) + fibo(x-2)
         return d[x]
     print(fibo(99))
     ```

     

  - 피보나치 수열 : 보텀업 다이나믹 프로그래밍 소스코드

     ```python
     # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
     d= [0] * 100
     # 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
     d[1] = 1
     d[2] = 1
     n = 99
     
     # 피보나치 함수 (Fibonacci Function) 반복문으로 구현 (보텀 업 다이나믹 프로그래밍)
     for i in range(3,n+1):
         d[i] = d[i-1] + d[i-2]
         
     print(d[n])
     ```

     

   

​    

### 최단 경로 알고리즘

>최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘
>
>각 지점은 그래프에서 노드로 표현
>
>지점 간 연결된 도로는 그래프에서 간선으로 표현



##### 다익스트라 최단 경로 알고리즘

- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산

- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작

  - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않습니다.

- 다익스트라 최단 경로 알고리즘은 **`그리디 알고리즘`** 으로 분류

  - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복

- **동작과정**

  1. 출발 노드를 설정

  2. 최단 거리 테이블을 초기화

  3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택

  4. 해낭 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신

  5. 위 과정에서 3번과 4번을 반복

     

  ```python
  import sys
  input = sys.stdin.readline
  INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
  
  # 노드의 개수, 간선의 개수를 입력받기
  n,m = map(int, input().split())
  
  # 시작 노드 번호를 입력받기
  start = int(input())
  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
  graph = [[] for i in range(n + 1)]
  # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
  visited = [False] * (n + 1)
  # 최단 거리 테이블을 모두 무한으로 초기화
  distance = [INF] * (n + 1)
  
  # 모든 간선 정보를 입력받기
  for _ in range(m):
      a, b, c = map(int,input().split())
      # a번 노드에서 b번 노드를 가는 비용이 c라는 의미
      graph[a].append((b,c))
      
  # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
  def get_smallest_node():
      min_value=INF
      index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
      for i in range(1, n + 1):
          if distance[i] < min_value and not visited[i]:
              min_value = distance[i]
              index = i            
      return index
  
  
  def dijkstra(start):
      # 시작 노드에 대해서 초기화
      distance[start] = 0
      visited[start] = True
      for j in graph[start]:
          distance[j[0]] = j[i]
      # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
      for i in range(n - 1):
          # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
          now = get_smallest_node()
          visited[now] = True
          # 현재 노드와 연결된 다른 노드를 확인
          for j in graph[now]:
              cost = distance[now] + j[i]
              # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
              if cost < distance[j[0]]:
                  distance[j[0]] = cost
                  
  # 다익스트라 알고리즘을 수행
  dijkstra(start)
  
  # 모든 노드로 가기 위한 최단 거리를 출력
  for i in range(1,n+1):
      # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
      if distance[i] = INF:
          print("INFINITY")
      # 도달할 수 있는 경우 거리를 출력
      else :
          print(distance[i])
  
  ```

  





### 파이썬 라이브러리

#### - itertools 



