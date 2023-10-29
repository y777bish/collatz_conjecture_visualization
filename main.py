import pygame
import math

pygame.init()
clock = pygame.time.Clock()

blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
maroon = (144, 12, 63)
bloody = (199, 0, 57)
orange = (249, 76, 16)
submarine = (248, 222, 34)
peach = (254, 205, 166)

width, height = 800, 600
window = pygame.display.set_mode((width, height))  # Utworzenie okna o szerokości i wysokości
pygame.display.set_caption("Tytuł Okna")  # Ustawienie tytułu okna

# Punkt początkowy
start_point = (width // 4, height // 4)

# Parametry do rysowania wzoru
line_length = 20  # Długość linii
angle_change = 20  # Zmiana kąta

# Kąt początkowy
angle = 0

def collatz_sequence(n):
    sequence = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# playin = True

font = pygame.font.Font(None, 36)
text_color = peach

sequence_completed = False

while not sequence_completed:
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sequence_completed = True
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         sequence_completed = True

    #Obliczenia dla nowego punktu końcowego
    number = 140
    sequence = collatz_sequence(number)
    for x in range(len(sequence)):

        angle_rad = math.radians(angle)

        if sequence[x] % 2 == 0:
            angle_change = -10  # Dla liczby parzystej zmiana kąta w prawo
        else:
            angle_change = 10  # Dla liczby nieparzystej zmiana kąta w lewo

        end_point = (start_point[0] + line_length * math.cos(angle_rad),
                    start_point[1] - line_length * math.sin(angle_rad))
        
        pygame.draw.line(window, maroon, start_point, end_point, 2)
        
        angle += angle_change
        start_point = (end_point[0],end_point[1])

        if x == len(sequence) - 1:
            sequence_completed = True

        text_surface = font.render(f"Visualization for {number}", True, text_color)
        window.blit(text_surface, (10, 10))  # Display at (10, 10) coordinates

        pygame.display.update()
        clock.tick(5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()