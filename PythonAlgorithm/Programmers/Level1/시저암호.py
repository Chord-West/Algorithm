def solution(s, n):
    answer = ''
    arr = list(map(str,s))
    aph = [ chr(x) for x in range(ord('a'),ord('z')+1)]
    aph.extend(aph)
    Aph = [ chr(x) for x in range(ord('A'),ord('Z')+1)]
    Aph.extend(Aph)
    for x in s:
        if x in aph:
            answer+=aph[aph.index(x)+n]
        elif x in Aph:
            answer+=Aph[Aph.index(x)+n]
        else:
            answer+=' '
    return answer