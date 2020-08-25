import pygame
import random

pygame.init()

#화면크기세팅 
screen_width = 454
screen_height = 454
screen = pygame.display.set_mode((screen_width, screen_height))

#타이틀
pygame.display.set_caption("Puzzle Game")

#배경화면
background = pygame.image.load("background.png")

###숫자판생성
img_path = []
number = []
number_size = []
number_width = []
number_height = []
number_x_pos = []
number_y_pos = []

i = 0
for i in range(9):
    img_path.append("img_number/num{0}.png".format(i+1))
    number.append(pygame.image.load(img_path[i]))
    number_size.append(number[i].get_rect().size)
    number_width.append(number_size[i][0])
    number_height.append(number_size[i][1])
    number_x_pos.append(screen_width / 2)
    number_y_pos.append(screen_height - number_height[i])
    i += 1

#랜덤으로 숫자 배치
random_list = {}
number_list = []
random_num = random.randint(1,9)

i = 0
for i in range(9):
    while random_num in number_list:
        random_num = random.randint(1,9)
    number_list.append(random_num)
    random_list[i] = number_list[i]   # 딕셔너리 위치:현재숫자

#숫자 위치 바꿈
def swap(num1, num2):
    temp = random_list[num1]
    random_list[num1] = random_list.get(num2)
    random_list[num2] = temp

#게임 실행중
game_Running = True

select_index = 0
select_img = True
selX = 0
selY = 0

key_Left = False
key_Right = False
key_Up = False
key_Down = False
while game_Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Running = False

        # 키가 눌러졌는지 확인
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_Left = True
                if key_Left == True and select_img == True and select_index != 0 and select_index != 3 and select_index != 6:
                    swap(select_index, select_index - 1)
                    select_index -= 1
                    selX -= 151
            elif event.key == pygame.K_RIGHT:
                key_Right = True
                if key_Right == True and select_img == True and select_index != 2 and select_index != 5 and select_index != 8:
                    swap(select_index, select_index + 1)
                    select_index += 1
                    selX += 151
            elif event.key == pygame.K_UP:
                key_Up = True
                if key_Up == True and select_img == True and select_index != 0 and select_index != 1 and select_index != 2:
                    swap(select_index, select_index - 3)
                    select_index -= 3
                    selY -= 151
            elif event.key == pygame.K_DOWN:
                key_Down = True
                if key_Down == True and select_img == True and select_index != 6 and select_index != 7 and select_index != 8:
                    swap(select_index, select_index + 3)
                    select_index += 3
                    selY += 151
            elif event.key == pygame.K_RETURN:
                select_img = not select_img
                select_index = 0
                selX = 0
                selY = 0
    
    screen.blit(background, (0, 0)) #배경그리기

    #이미지 선택 표시(테두리)
    if select_img == True:
        pygame.draw.rect(screen, (255,0,0), [0 + selX, 0 + selY, 152, 152], 1)
    else:
        pygame.draw.rect(screen, (0,0,0), [0 + selX, 0 + selY, 152, 152], 1)

    #숫자 이미지 그리기
    i = 0
    posX = 151
    posY = 151
    for i in range(9): #이미지 그리기
        if i == 0:   #첫번째 줄
            screen.blit(number[random_list.get(i)-1], (1, 1))
        elif i < 3:
            screen.blit(number[random_list.get(i)-1], (posX+1, 1))
            posX = posX + 151
        elif i == 3: #두번째 줄
            screen.blit(number[random_list.get(i)-1], (1, posY+1))
            posX = 151
        elif i < 6:
            screen.blit(number[random_list.get(i)-1], (posX+1, posY+1))
            posX = posX + 151
        elif i == 6: #세번째 줄
            posY = posY + 151
            screen.blit(number[random_list.get(i)-1], (1, posY+1))
            posX = 151
        else:
            screen.blit(number[random_list.get(i)-1], (posX+1, posY+1))
            posX = posX + 151
        i += 1

    key_Left = False
    key_Right = False
    key_Up = False
    key_Down = False

    number_list.sort()
    i = 0
    clear = 0
    for i in range(9):
        if random_list.get(i) == number_list[i]:
            clear += 1

    if clear == 9:
        game_Running = False

    #게임화면 다시그리기
    pygame.display.update()


#게임 종료(클리어)
game_font = pygame.font.Font(None, 40)
game_clear = "Clear"

msg = game_font.render(game_clear, True, (0, 0, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 3초간 대기
pygame.time.delay(3000)

#게임종료
pygame.quit()

