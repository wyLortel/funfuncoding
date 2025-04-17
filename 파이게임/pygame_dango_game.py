import pygame
import random
import sys

# 색 정의
blue = (255, 105, 180)

score = 0
high_score = 1000

# 우사마루 배열 초기화
usamaru = [[0 for _ in range(8)] for _ in range(10)]
check = [[0 for _ in range(8)] for _ in range(10)]

# 우사마루 표시 함수
def display_usamaru():
    screen.blit(bg, [0, 0])
    offsets = {1: (5, 8), 2: (5, 8), 3: (5, 8), 4: (5, 8)}
    for y in range(10):
        for x in range(8):
            if usamaru[y][x] > 0:
                img_index = usamaru[y][x]
                base_x = x * 72 + 20
                base_y = y * 72 + 20
                offset_x, offset_y = offsets.get(img_index, (0, 0))
                screen.blit(img_usamaru[img_index], [base_x + offset_x, base_y + offset_y])

# 우사마루 떨어뜨리는 함수
def drop_usamaru():
    flg = False
    for y in range(8, -1, -1):
        for x in range(8):
            if usamaru[y][x] != 0 and usamaru[y + 1][x] == 0:
                usamaru[y + 1][x] = usamaru[y][x]
                usamaru[y][x] = 0
                flg = True
    return flg

# 3개 확인 함수
def check_usamaru():
    for y in range(10):
        for x in range(8):
            check[y][x] = usamaru[y][x]

    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0 and check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                usamaru[y - 1][x] = 5
                usamaru[y][x] = 5
                usamaru[y + 1][x] = 5

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0 and check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                usamaru[y][x - 1] = 5
                usamaru[y][x] = 5
                usamaru[y][x + 1] = 5

    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    usamaru[y - 1][x - 1] = 5
                    usamaru[y][x] = 5
                    usamaru[y + 1][x + 1] = 5
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    usamaru[y + 1][x - 1] = 5
                    usamaru[y][x] = 5
                    usamaru[y - 1][x + 1] = 5

# 3개 모이면 지우는 함수
def delete_usamaru():
    num = 0
    for y in range(10):
        for x in range(8):
            if usamaru[y][x] == 5:
                usamaru[y][x] = 0
                num += 1
    if num > 0:
        pi_sound.play()  # 효과음 재생
    return num

# 스코어 표시 함수
def display_score():
    txt = font.render(str(score), True, blue)
    screen.blit(txt, [650, 299])
    txt2 = font.render(str(high_score), True, blue)
    screen.blit(txt2, [650, 412])

# 새로운 우사마루 설정 함수
def set_usamaru():
    for x in range(8):
        usamaru[0][x] = random.randint(1, 4)

# 게임 오버 체크 함수
def over_usamaru():
    return any(usamaru[0][x] > 0 for x in range(8))

def main():
    global score, high_score
    cursor_x, cursor_y = 0, 0
    state = 0
    next_usamaru = 0
    timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if state == 0:
            screen.blit(bg, [0, 0])
            screen.blit(title, title.get_rect(center=(456, 200)))
            screen.blit(click_start, click_start.get_rect(center=(456, 500)))
            state = 1

        elif state == 1:
            if mouse_click[0]:
                score = 0
                cursor_x, cursor_y = 0, 0
                set_usamaru()
                state = 2

        elif state == 2:
            if not drop_usamaru():
                state = 3
            display_usamaru()

        elif state == 3:
            check_usamaru()
            state = 4
            display_usamaru()

        elif state == 4:
            sc = delete_usamaru()
            score += sc * 10
            if score > high_score:
                high_score = score
            if sc > 0:
                state = 2
            else:
                if not over_usamaru():
                    next_usamaru = random.randint(1, 4)
                    state = 5
                else:
                    state = 6
                    timer = 0
            display_usamaru()

        elif state == 5:
            if 20 <= mouse_x < 596 and 20 <= mouse_y < 740:
                cursor_x = (mouse_x - 20) // 72
                cursor_y = (mouse_y - 20) // 72
                if mouse_click[0] and usamaru[cursor_y][cursor_x] == 0:
                    usamaru[cursor_y][cursor_x] = next_usamaru
                    next_usamaru = 0
                    state = 2
            display_usamaru()
            screen.blit(cursor, [cursor_x * 72 + 20, cursor_y * 72 + 20])

        elif state == 6:
            timer += 1
            screen.blit(displayed_gameover, displayed_gameover.get_rect(center=(456, 384)))
            if timer >= 100:
                state = 0

        display_score()
        if next_usamaru > 0:
            screen.blit(img_usamaru[next_usamaru], [732, 108])

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("dango_bgm.mp3")
    pygame.mixer.music.play(-1)
    pi_sound = pygame.mixer.Sound("pi.mp3")

    pygame.display.set_caption("うさまるゲーム")
    screen = pygame.display.set_mode((912, 768))
    font = pygame.font.Font(None, 60)
    clock = pygame.time.Clock()

    bg = pygame.image.load("usamaru_back.jpg")
    cursor = pygame.image.load("cursor.png")
    img_usamaru = [
        None,
        pygame.transform.scale(pygame.image.load("usamaru1.png"), (65, 65)),
        pygame.transform.scale(pygame.image.load("usamaru2.png"), (65, 65)),
        pygame.transform.scale(pygame.image.load("usamaru3.png"), (65, 65)),
        pygame.transform.scale(pygame.image.load("usamaru4.png"), (65, 65)),
        pygame.image.load("dango_kushi.png"),
    ]

    # 원본 비율 유지하며 크기 조정 (더 작게)
    original_title = pygame.image.load("image (1).png")
    title = pygame.transform.smoothscale(original_title, (int(original_title.get_width() * 0.3), int(original_title.get_height() * 0.3)))
    original_start = pygame.image.load("start.png")
    click_start = pygame.transform.smoothscale(original_start, (int(original_start.get_width() * 1.2), int(original_start.get_height() * 1.2)))
    original_gameover = pygame.image.load("gameover.png")
    displayed_gameover = pygame.transform.smoothscale(original_gameover, (int(original_gameover.get_width() * 0.3), int(original_gameover.get_height() * 0.3)))

    main()

