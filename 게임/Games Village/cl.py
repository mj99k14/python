import socket
import pygame
import math
import time
import threading
import random

# 클라이언트 A 소켓 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('210.101.236.189', 12345))  # 서버의 IP 주소로 변경하세요

# 파이게임 초기화
pygame.init()
screen_width, screen_height = 1024, 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basketball Game - Player A")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

background = pygame.image.load("path_to_image.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# 플레이어 설정
player_x = 100
player_y = screen_height - 100
player_width = 50
player_height = 100

hoop = pygame.image.load("G.png")
hoop_rect = hoop.get_rect()
hoop_rect_width = 100
hoop_rect_height = 20
hoop_rect_x = screen_width - hoop_rect_width
hoop_rect_y = random.randint(100, screen_height - 200)

ball = pygame.image.load("ball.png")
ball_radius = 30
ball = pygame.transform.scale(ball, (ball_radius * 2, ball_radius * 2))
ball_rect_x = player_x + player_width
ball_rect_y = player_y - ball_radius
ball_angle = 45
ball_fired = False
ball_power = 0
max_power = 30

gravity = 0.5
ball_velocity_x = 0
ball_velocity_y = 0
score = 0
ball_fired_time = None
ball_bounced_time = None
bounce_reset_time = 3

start_time = time.time()
time_limit = 60
running = True
power_charging = False
clock = pygame.time.Clock()
FPS = 60

def calculate_parabola_path(start_x, start_y, velocity_x, velocity_y, gravity, steps=50):
    path = []
    t = 0
    for _ in range(steps):
        t += 0.1
        x = start_x + velocity_x * t
        y = start_y + velocity_y * t + 0.5 * gravity * t ** 2
        if x > screen_width or y > screen_height:
            break
        path.append((x, y))
    return path

def reset_ball_and_hoop():
    global ball_fired, ball_rect_x, ball_rect_y, ball_velocity_x, ball_velocity_y, ball_fired_time, ball_bounced_time
    global hoop_rect_y
    ball_fired = False
    ball_rect_x = player_x + player_width
    ball_rect_y = player_y - ball_radius
    ball_velocity_x = 0
    ball_velocity_y = 0
    ball_fired_time = None
    ball_bounced_time = None
    hoop_rect_y = random.randint(100, screen_height - 200)

def receive_data():
    global opponent_ball_rect_x, opponent_ball_rect_y
    while True:
        data = client_socket.recv(1024).decode()
        if data:
            x, y = map(float, data.split(','))
            opponent_ball_rect_x = x
            opponent_ball_rect_y = y

opponent_ball_rect_x = hoop_rect_x  # 상대방 공의 초기 위치
opponent_ball_rect_y = hoop_rect_y

threading.Thread(target=receive_data, daemon=True).start()

running = True
while running:
    current_time = time.time()
    elapsed_time = current_time - start_time
    remaining_time = max(0, time_limit - elapsed_time)

    screen.blit(background, (0, 0))

    if remaining_time <= 0:
        running = False
        client_socket.sendall("RESET".encode())
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not ball_fired:
                power_charging = True
            elif event.key == pygame.K_UP:
                ball_angle = min(90, ball_angle + 5)
            elif event.key == pygame.K_DOWN:
                ball_angle = max(0, ball_angle - 5)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and not ball_fired:
                power_charging = False
                ball_fired = True
                ball_fired_time = time.time()
                ball_velocity_x = ball_power * math.cos(math.radians(ball_angle))
                ball_velocity_y = -ball_power * math.sin(math.radians(ball_angle))
                ball_power = 0
                # 현재 상태를 서버에 전송
                client_socket.sendall(f"{ball_rect_x},{ball_rect_y}".encode())

    if power_charging and not ball_fired:
        ball_power = min(max_power, ball_power + 0.5)

    if ball_fired:
        ball_velocity_y += gravity
        ball_rect_x += ball_velocity_x
        ball_rect_y += ball_velocity_y

        if ball_rect_x < 0 or ball_rect_x > screen_width - ball_radius * 2 or ball_rect_y > screen_height - ball_radius * 2:
            reset_ball_and_hoop()

        if ball_rect_x <= 0 or ball_rect_x >= screen_width - ball_radius * 2:
            ball_velocity_x *= -1
            ball_bounced_time = time.time()

        if ball_rect_y <= 0 or ball_rect_y >= screen_height - ball_radius * 2:
            ball_velocity_y *= -1
            ball_bounced_time = time.time()

        if ball_bounced_time and time.time() - ball_bounced_time > bounce_reset_time:
            reset_ball_and_hoop()

        hoop_center_x = hoop_rect_x + hoop_rect_width / 2
        hoop_center_y = hoop_rect_y + hoop_rect_height / 2
        if (
            hoop_center_x - ball_radius < ball_rect_x < hoop_center_x + ball_radius and
            hoop_center_y - ball_radius < ball_rect_y < hoop_center_y + ball_radius
        ):
            score += 1
            reset_ball_and_hoop()

    if not ball_fired:
        angle_line_length = 100
        angle_line_x = ball_rect_x + angle_line_length * math.cos(math.radians(ball_angle))
        angle_line_y = ball_rect_y - angle_line_length * math.sin(math.radians(ball_angle))
        pygame.draw.line(screen, GREEN, (ball_rect_x, ball_rect_y), (angle_line_x, angle_line_y), 5)

        path = calculate_parabola_path(ball_rect_x, ball_rect_y, ball_velocity_x, ball_velocity_y, gravity)
        for point in path:
            pygame.draw.circle(screen, BLUE, (int(point[0]), int(point[1])), 3)

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    screen.blit(hoop, (hoop_rect_x, hoop_rect_y))
    screen.blit(ball, (ball_rect_x, ball_rect_y))

    # 상대방 공의 위치를 그리기
    pygame.draw.circle(screen, RED, (int(opponent_ball_rect_x), int(opponent_ball_rect_y)), ball_radius)

    font = pygame.font.SysFont(None, 36)
    angle_text = font.render(f"Angle: {ball_angle}°", True, BLACK)
    screen.blit(angle_text, (10, 10))
    power_text = font.render(f"Power: {int(ball_power)}", True, BLACK)
    screen.blit(power_text, (10, 50))
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 90))
    time_text = font.render(f"Time: {int(remaining_time)}s", True, BLACK)
    screen.blit(time_text, (10, 130))

    gauge_width = 200
    gauge_height = 20
    gauge_x = 10
    gauge_y = 170

    current_gauge_width = (ball_power / max_power) * gauge_width
    pygame.draw.rect(screen, BLACK, (gauge_x, gauge_y, gauge_width, gauge_height), 2)
    pygame.draw.rect(screen, GREEN, (gauge_x, gauge_y, current_gauge_width, gauge_height))

    pygame.display.flip()
    clock.tick(FPS)

screen.fill(WHITE)
final_score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(final_score_text, (screen_width // 2 - final_score_text.get_width() // 2, screen_height // 2))
pygame.display.flip()
time.sleep(2)
pygame.quit()
client_socket.close()
