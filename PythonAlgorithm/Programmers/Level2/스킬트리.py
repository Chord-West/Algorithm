def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        ch=[st.index(s) if s in st else len(skill_trees) for s in skill ]
        if all(ch[i]<=ch[i+1] for i in range(len(ch)-1)):
            answer+=1
    return answer