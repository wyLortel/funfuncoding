def solution(letter):
    answer = ''
    morse = { 
        '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
        '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
        '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',
        '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
        '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z'
    }

    lis = []
    mozi = ""

    for i in letter:
        if i == " ":
            lis.append(mozi)
            mozi = ""  
        else:
            mozi += i

    if mozi:
        lis.append(mozi) 

    for k in lis:
        answer += morse[k]

    return answer


print(solution(".... . .-.. .-.. ---"))
