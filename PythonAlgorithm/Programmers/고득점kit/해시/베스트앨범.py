from collections import defaultdict
from heapq import heappush,heappop
def solution(genres, plays):
    answer = []
    genres_p = defaultdict(int)
    p = defaultdict(list)
    for i in range(len(genres)):
        genres_p[genres[i]]+=plays[i]
        heappush(p[genres[i]],(-plays[i],i))
    genres_sort = sorted(genres_p,key = lambda x:genres_p[x],reverse=True) # 장르의 합으로 정렬
    for genre in genres_sort:
        if len(p[genre])<2:
            answer.append(heappop(p[genre])[1])
        else:
            answer.append(heappop(p[genre])[1])
            answer.append(heappop(p[genre])[1])
    return answer