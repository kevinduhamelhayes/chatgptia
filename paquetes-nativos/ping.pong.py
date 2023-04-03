import pygame
import random

# Inicializamos Pygame
pygame.init()

# Definimos los colores que vamos a utilizar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definimos las dimensiones de la pantalla
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Creamos la pantalla
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Establecemos el título de la ventana
pygame.display.set_caption("Pong")

# Definimos las variables del juego
paddle_width = 15
paddle_height = 60
ball_width = 20
ball_height = 20
ball_speed = 5
paddle_speed = 5
score_font = pygame.font.SysFont('Calibri', 30, True, False)

# Definimos la posición inicial de las paletas y la pelota
player_paddle_pos = [50, SCREEN_HEIGHT / 2 - paddle_height / 2]
computer_paddle_pos = [SCREEN_WIDTH - 50 - paddle_width, SCREEN_HEIGHT / 2 - paddle_height / 2]
ball_pos = [SCREEN_WIDTH / 2 - ball_width / 2, SCREEN_HEIGHT / 2 - ball_height / 2]

# Definimos la velocidad inicial de la pelota
ball_dir = [random.choice((-1, 1)), random.uniform(-1, 1)]
ball_dir[1] = ball_dir[1] / abs(ball_dir[1]) * ball_speed

# Definimos las funciones para dibujar las paletas y la pelota
def draw_paddle(paddle_pos):
    pygame.draw.rect(screen, WHITE, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))

def draw_ball(ball_pos):
    pygame.draw.rect(screen, WHITE, (ball_pos[0], ball_pos[1], ball_width, ball_height))

# Definimos la función para actualizar la posición de la pelota
def update_ball(ball_pos, ball_dir):
    ball_pos[0] += int(ball_dir[0])
    ball_pos[1] += int(ball_dir[1])
    if ball_pos[1] < 0:
        ball_pos[1] = 0
        ball_dir[1] = -ball_dir[1]
    elif ball_pos[1] > SCREEN_HEIGHT - ball_height:
        ball_pos[1] = SCREEN_HEIGHT - ball_height
        ball_dir[1] = -ball_dir[1]
    return ball_pos

# Definimos la función para actualizar la posición de la paleta del jugador
def update_player_paddle(player_paddle_pos, keys_pressed):
    if keys_pressed[pygame.K_UP] and player_paddle_pos[1] > 0:
        player_paddle_pos[1] -= paddle_speed
    elif keys_pressed[pygame.K_DOWN] and player_paddle_pos[1] < SCREEN_HEIGHT - paddle_height:
        player_paddle_pos[1] += paddle_speed
    return player_paddle_pos

# Definimos la función para actualizar la posición de la paleta de la computadora
def update_computer_paddle(computer_paddle_pos, ball_pos):
    if computer_paddle_pos[1] + paddle_height / 2 > ball_pos[1]:
        computer_paddle_pos[1] -= paddle_speed
    elif computer_paddle_pos[1] + paddle_height / 2 < ball_pos[1]:
        computer_paddle