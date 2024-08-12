import pygame
import time

# Pygame 초기화
pygame.init()

# 게임 시작 시점의 시간을 밀리초 단위로 저장
start_time_1 = pygame.time.get_ticks()
print("start_time_1: ", start_time_1) # 236 ms

time.sleep(3) # 3초 지연 3000ms


start_time_2 = pygame.time.get_ticks()
print("start_time_2: ", start_time_2) # 3236
import pygame

# Pygame 초기화
pygame.init()

# 게임 시작 시점의 시간을 밀리초 단위로 저장
start_time = pygame.time.get_ticks()

# 게임 루프 시작
while True:
    # 현재 시간에서 게임 시작 시간을 뺀 값을 초 단위로 변환하여 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # 초 단위 경과 시간

    # 경과 시간을 소수점 둘째 자리까지 출력
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    # 경과 시간이 10초를 초과하면 게임 루프 종료
    if elapsed_time > 10.0:
        break
