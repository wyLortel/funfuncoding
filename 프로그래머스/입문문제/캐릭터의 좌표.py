def solution(keyinput, board):
    answer = []
    
    x, y = 0, 0

    for key in keyinput:
        if key == "left":
            x -= 1
        elif key == "right":
            x += 1
        elif key == "up":
            y += 1
        elif key == "down":
            y -= 1

    
    if x > board[0] // 2:
        x = board[0] // 2
    elif x < -(board[0] // 2):
        x = -(board[0] // 2)

    if y > board[1] // 2:
        y = board[1] // 2
    elif y < -(board[1] // 2):
        y = -(board[1] // 2)

    
    answer = [x,y]
    
    
    return answer

lis = ["left", "right", "up", "right", "right"]
bord = [11, 11]

print(solution(lis , bord))