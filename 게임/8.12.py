# import random
# import pygame

# pygame.init()

# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# clock = pygame.time.Clock()
# running = True

# # 게임 변수
# fall_rect_width = 80
# fall_rect_height = 40


# # 떨어지는 사각형 -> 3개
# fall_rect_list = []

# for _ in range(3):
#     while True:
#         rect_x = random.randint(0, screen_width - fall_rect_width) # 0 <= x <= 720
#         rect = pygame.Rect(rect_x, 0, fall_rect_width, fall_rect_height)
        
#         # 충돌이 발생하지 않았을 경우
#         if rect.collidelist(fall_rect_list) == -1:
#             # 사각형을 리스트에 추가
#             fall_rect_list.append(rect)
#             break
    

# # 객체 이동 속도
# speed = 100 # 300 pixel / second

# # 사용자 정의 이벤트 생성
# # MY_EVENT는 pygame.USEREVENT에 1을 더하여 고유한 이벤트로 정의
# MY_EVENT = pygame.USEREVENT + 1

# # 타이머 설정: 2초마다 MY_EVENT는 이벤트가 발생하도록 설정
# pygame.time.set_timer(MY_EVENT, 2000)  # 2000밀리초(2초)마다 이벤트 발생


# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == MY_EVENT:
#             print("My event 발생")

#     dt = clock.tick(60) / 1000  
    
#     # 사각형의 y축 좌표 증가 (위에서 아래로 이동)
#     for rect in fall_rect_list:
#         rect.y += speed * dt
#     # 화면 아래이면 리스트에 삭제
#     for rect in  fall_rect_list[:]:
#         if rect.y > screen_height:
#             fall_rect_list.remove(rect)

        
    
#     # 화면 그리기
#     screen.fill((255, 255, 255))
    
#     for rect in fall_rect_list:    
#         pygame.draw.rect(screen, (0, 0, 255), rect)
        
#     # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
#     pygame.display.flip()


    
# pygame.quit()



import random
import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# 게임 변수
fall_rect_width = 80
fall_rect_height = 40
moving_rect_width = 50
moving_rect_height = 40

# 움직이는 사각형
mov_rect_x = screen_width // 2 - moving_rect_width // 2
mov_rect_y = screen_height - moving_rect_height - 5
moving_rect = pygame.Rect(mov_rect_x, mov_rect_y, moving_rect_width, moving_rect_height)

# 떨어지는 사각형 -> 3개
fall_rect_list = []

def generate_falling_rect():
    for _ in range(random.randint(2, 6)):
        while True:
            rect_x = random.randint(0, screen_width - fall_rect_width) # 0 <= x <= 720
            rect = pygame.Rect(rect_x, 0, fall_rect_width, fall_rect_height)
            
            # 충돌이 발생하지 않았을 경우
            if rect.collidelist(fall_rect_list) == -1:
                # 사각형을 리스트에 추가
                fall_rect_list.append(rect)
                break
    

# 객체 이동 속도
speed = 100 # 100 pixel / second

# 사용자 정의 이벤트 생성
# MY_EVENT는 pygame.USEREVENT에 1을 더하여 고유한 이벤트로 정의
MY_EVENT = pygame.USEREVENT + 1

# 타이머 설정: 2초마다 MY_EVENT는 이벤트가 발생하도록 설정
pygame.time.set_timer(MY_EVENT, 2000)  # 2000밀리초(2초)마다 이벤트 발생


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MY_EVENT:
            generate_falling_rect()

    dt = clock.tick(60) / 1000  
    
    # 사각형의 y축 좌표 증가 (위에서 아래로 이동)
    for rect in fall_rect_list:
        rect.y += speed * dt
        
    # 플레이어 사각형 움직임 처리
    keys = pygame.key.get_pressed()
    
    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt 
            
    # 충돌 감지
    if moving_rect.collidelist(fall_rect_list) != -1:
        print("충돌 발생, 게임 종료")
        running = False
        
    # 화면 아래이면 리스트에 삭제
    for rect in fall_rect_list[:]:
        if rect.y > screen_height:
            fall_rect_list.remove(rect)
    
    # 화면 그리기
    screen.fill((255, 255, 255))
    
    # 떨어지는 사각형
    for rect in fall_rect_list:    
        pygame.draw.rect(screen, (0, 0, 255), rect)
        
    # 플레이어 사각형
    pygame.draw.rect(screen, (255, 0, 0), moving_rect)
        
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    print(len(fall_rect_list))
        
pygame.quit()





