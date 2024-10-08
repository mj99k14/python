import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collect Items Game')

WHITE = (255, 255, 255)
BLUE =(0, 0, 255)
RED = (255, 0 ,0)
GREEN = (0, 255 ,0)
YELLOW = (255, 255 , 0)

def create_obstacles(num_obstacles, size , screen_width, screen_height):

    obstacles = []

    for _ in range(num_obstacles):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),\
                               random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles):
                obstacles.append(rect)
                break
    return obstacles

def create_items(num_items, size , screen_width, screen_height, obstacles):

    items = []

    for _ in range(num_items):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),\
                                random.randint(0, screen_height - size),size, size)
            if not any(rect.colliderect(o) for o in obstacles) and \
                not any(rect.colliderect(i) for i in items):
                items.append(rect)
                break
    return items

obstacles = create_obstacles(5, 50 , screen_width, screen_height)
items = create_items(10, 20 , screen_width, screen_height ,obstacles)

m_width = m_height = 50
while True:

    m_x, m_y = random.randint(0, screen_width - m_width), random.randint(0,screen_height - m_height)
    moving_rect =  pygame.Rect(m_x,m_y ,m_width, m_height)
    if moving_rect.collidelist(obstacles) == -1 and  moving_rect.collidelist(items) == -1:
        break # -> 아무것도 부딪히지않는곳에 배치잘됫는말

velocity = 300 
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    previous_position = moving_rect.topleft # 충돌시 움직이는객체 되돌리기위해 왼쪽위모서리 기록

    dt = clock.tick(60)/1000.0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt

    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"장애물 {collision_index}와 충돌 ! 위치 복원. ")
        moving_rect.topleft = previous_position

    item_index = moving_rect.collidelist(items)
    if item_index != -1:
        print(f"아이템 수집! 남은 아이템:{len(items)-1}")
        del items[item_index]
    if not items:
        print("모든 아이템을 수집했습니다! 승리!") 
        running = False

    screen.fill(WHITE)

    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, obs)

    for item in items:
        pygame.draw.rect(screen ,YELLOW, item)

    pygame.draw.rect(screen, RED , moving_rect)

    pygame.display.flip()


pygame.quit()