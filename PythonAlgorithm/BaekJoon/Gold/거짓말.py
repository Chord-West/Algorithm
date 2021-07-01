import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline

n, m = map(int, input().split())
tknow = deque(list(map(int, input().split()))[1:])  # 진실을 아는 사람
visit = [0] * (n + 1)
for k in tknow:
    visit[k] = 1
parties = [list(map(int, input().split()))[1:] for _ in range(m)]
party_visit = [0] * m  # 진실을 말해야 하는 파티
while tknow:
    known_guest = tknow.popleft()
    candidate = set()
    for i in range(len(parties)):
        party = set(parties[i])
        if known_guest in party:
            candidate = candidate.union(party)
            party_visit[i] = 1
    for guest in candidate:
        if not visit[guest]:
            tknow.append(guest)
            visit[guest] = 1
print(party_visit.count(0))
