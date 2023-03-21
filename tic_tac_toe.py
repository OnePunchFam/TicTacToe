import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WIDTH, HEIGHT = 600, 600

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the font
FONT = pygame.font.SysFont("comicsansms", 72)

# Create the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Define the board
board = [[None for _ in range(3)] for _ in range(3)]

# Define the turn
turn = "X"

# Define the game over flag
game_over = False

# Define the draw function
def draw():
    # Clear the window
    WIN.fill(WHITE)

    # Draw the board
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(WIN, BLACK, (i*200, j*200, 200, 200), 5)
            if board[i][j]:
                text = FONT.render(board[i][j], True, BLACK)
                WIN.blit(text, (i*200+75, j*200+50))

    # Update the window
    pygame.display.update()

# Define the check win function
def check_win():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]

    # Check for a tie
    if all(all(row) for row in board):
        return "Tie"

    # If no winner and no tie, return None
    return None

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONUP and not check_win():
            x, y = pygame.mouse.get_pos()
            i, j = x // 200, y // 200
            if board[i][j] == None:
                board[i][j] = turn
                turn = "O" if turn == "X" else "X"

    # Draw the board
    draw()

    # Check for a win or tie
    winner = check_win()
    if winner:
        if winner == "Tie":
            print("Tie!")
        else:
            print(f"{winner} wins!")
        game_over = True

# Quit Pygame
pygame.quit()