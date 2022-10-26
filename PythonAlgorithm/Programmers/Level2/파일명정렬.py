import re
def solution(files):
    answer = []
    words = []
    HEAD,NUM = "",""

    for idx,file in enumerate(files):
        NUM = re.sub('\D'," ",file).split()[0]
        HEAD = file[:file.find(NUM)]

        words.append([file,HEAD.lower(),int(NUM),idx])
    words.sort(key = lambda x:(x[1],x[2]))
    for word in words:
        answer.append(word[0])
    return answer