import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("K-means Visualization")

running = True
clock = pygame.time.Clock()

# Định nghĩa màu sắc
BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)
BUTTON_COLOR = (0, 122, 204)
BUTTON_HOVER_COLOR = (0, 153, 255)

# Định nghĩa font chữ
font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)

# Tạo các đối tượng văn bản
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render("Run", True, WHITE)
text_random = font.render("Random", True, WHITE)
text_algorithm = font.render("Algorithm", True, WHITE)
text_reset = font.render("Reset", True, WHITE)

# Khởi tạo các biến
K = 0
error = 0
points = []

# Hàm vẽ nút
def draw_button(rect, text, hover=False):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect)
    screen.blit(text, (rect.x + (rect.width - text.get_width()) // 2, rect.y + (rect.height - text.get_height()) // 2))

# Vòng lặp chính
points = []
while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Vẽ giao diện
    # Vẽ panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500), border_radius=10)
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490), border_radius=10)

    # K button + 
    plus_rect = pygame.Rect(850, 50, 50, 50)
    draw_button(plus_rect, text_plus, plus_rect.collidepoint(mouse_x, mouse_y))

    # K button -
    minus_rect = pygame.Rect(950, 50, 50, 50)
    draw_button(minus_rect, text_minus, minus_rect.collidepoint(mouse_x, mouse_y))

    # K value
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k, (1050, 50))

    # Run button
    run_rect = pygame.Rect(850, 150, 150, 50)
    draw_button(run_rect, text_run, run_rect.collidepoint(mouse_x, mouse_y))

    # Random button
    random_rect = pygame.Rect(850, 250, 150, 50)
    draw_button(random_rect, text_random, random_rect.collidepoint(mouse_x, mouse_y))

    # Reset button
    reset_rect = pygame.Rect(850, 550, 150, 50)
    draw_button(reset_rect, text_reset, reset_rect.collidepoint(mouse_x, mouse_y))

    # Algorithm button
    algorithm_rect = pygame.Rect(850, 450, 150, 50)
    draw_button(algorithm_rect, text_algorithm, algorithm_rect.collidepoint(mouse_x, mouse_y))

    # Error text
    text_error = font.render("Error = " + str(error), True, BLACK)
    screen.blit(text_error, (850, 350))

    # Vẽ vị trí chuột khi chuột nằm trong panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")", True, BLACK)
        screen.blit(text_mouse, (mouse_x + 10, mouse_y))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                point = [mouse_x - 50, mouse_y - 50]
                points.append(point)
                print(points)
            if plus_rect.collidepoint(mouse_x, mouse_y):
                K += 1
                print("Press K +")
            if minus_rect.collidepoint(mouse_x, mouse_y):
                if K > 0:
                    K -= 1
                print("Press K -")
            if run_rect.collidepoint(mouse_x, mouse_y):
                print("run pressed")
            if random_rect.collidepoint(mouse_x, mouse_y):
                print("random pressed")
            if reset_rect.collidepoint(mouse_x, mouse_y):
                print("reset button pressed")
            if algorithm_rect.collidepoint(mouse_x, mouse_y):
                print("Algorithm button pressed")

    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6)
        pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)

    pygame.display.flip()

pygame.quit()
