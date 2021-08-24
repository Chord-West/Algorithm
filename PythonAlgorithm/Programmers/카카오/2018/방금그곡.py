def change(s):
    s = s.replace('C#','c')
    s = s.replace('D#','d')
    s = s.replace('F#','f')
    s = s.replace('G#','g')
    s = s.replace('A#','a')
    s = s.replace('E#','e')
    return s
def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', None)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = change(melody)
        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title, time)
    return answer[0]