import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# List of words
word_list = [
    "PYTHON",
    "JAVASCRIPT",
    "HANGMAN",
    "COMPUTER",
    "GAMING",
    "PROGRAMMING",
    "DEVELOPER",
]

# Hangman stages (coordinates for drawing parts)
hangman_parts = [
    lambda: pygame.draw.line(screen, BLACK, (150, 500), (450, 500), 10),  # Base
    lambda: pygame.draw.line(screen, BLACK, (300, 500), (300, 150), 10),  # Pole
    lambda: pygame.draw.line(screen, BLACK, (300, 150), (400, 150), 10),  # Top bar
    lambda: pygame.draw.line(screen, BLACK, (400, 150), (400, 200), 5),  # Rope
    lambda: pygame.draw.circle(screen, BLACK, (400, 250), 50, 5),  # Head
    lambda: pygame.draw.line(screen, BLACK, (400, 300), (400, 400), 5),  # Body
    lambda: pygame.draw.line(screen, BLACK, (400, 350), (350, 300), 5),  # Left arm
    lambda: pygame.draw.line(screen, BLACK, (400, 350), (450, 300), 5),  # Right arm
    lambda: pygame.draw.line(screen, BLACK, (400, 400), (350, 450), 5),  # Left leg
    lambda: pygame.draw.line(screen, BLACK, (400, 400), (450, 450), 5),  # Right leg
]

# Game variables
word = random.choice(word_list)  # Select a random word
guessed = set()
incorrect_guesses = 0
max_incorrect = len(hangman_parts)
running = True


# Function to display the current state of the word
def display_word():
    display = " ".join([letter if letter in guessed else "_" for letter in word])
    text = font.render(display, True, BLACK)
    text_rect = text.get_rect(
        center=(WIDTH - 200, 100)
    )  # Aligning word display to the right
    screen.blit(text, text_rect)


# Function to display a message
def display_message(message, y_offset=300):
    text = font.render(message, True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, y_offset))
    screen.blit(text, text_rect)


# Function to display the title
def display_title():
    title_text = font.render("Hangman Game", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(title_text, title_rect)


# Main game loop
while running:
    screen.fill(WHITE)

    # Display the title at the top
    display_title()

    # Display the guessed word on the right side
    display_word()

    # Draw hangman parts based on incorrect guesses, aligned on the left
    for i in range(incorrect_guesses):
        hangman_parts[i]()

    # Check for win or loss
    if all(letter in guessed for letter in word):
        display_message("You Win!", 250)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    elif incorrect_guesses == max_incorrect:
        display_message("You Lose!", 250)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha() and event.unicode.upper() not in guessed:
                letter = event.unicode.upper()
                guessed.add(letter)
                if letter not in word:
                    incorrect_guesses += 1

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
