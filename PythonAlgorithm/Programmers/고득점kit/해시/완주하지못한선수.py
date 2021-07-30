from collections import defaultdict
def solution(participant, completion):
    ans = defaultdict(int)
    for player in completion:
        ans[player] += 1
    for noplayer in participant:
        if noplayer not in ans:
            return noplayer
        else:
            ans[noplayer]-=1
            if ans[noplayer]<0:
                return noplayer