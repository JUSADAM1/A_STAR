import pygame
from mazeBuilder.mazerunner import main

pygame.init()

# This is the window dim
window = pygame.display.set_mode((1000, 1000))
# filling the window
window.fill((0, 0, 0))
# I just decide to just set this
# RGB yellow-ish
yellow = (240, 228, 12)


class Main_menu:
    def __init__(self, color, x, y, width, height, text=''):
        # colors
        self.color = color
        # x position
        self.x = x
        # y position
        self.y = y
        # width of something
        self.width = width
        # Height of something
        self.height = height
        # text
        self.text = text
        # Run is true alway true to me
        self.run = True

    def drawing_button(self, window, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 80)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


# Font
font_title = pygame.font.SysFont('comicsans', 900)
# What to be written, show, color, background(nope)
text_menu = font_title.render('A*', True, yellow, None)
# Position set to center
text_menu_rec = text_menu.get_rect(center=(1000 // 2, 1000 // 2))
# just making sure
text_menu_rec.center = (1000 // 2, 1000 // 2)

# Added a background pic
background_image = pygame.image.load("original.jpg").convert()


def redrawingWindow():
    window.fill((0, 0, 0))
    buttonIsGreen.drawing_button(window, (0, 255, 0))


buttonIsGreen = Main_menu((0, 0, 0), 350, 800, 250, 100, 'START!!')

run = True
while run:
    # Drawing the window and button
    redrawingWindow()
    # background image on page
    window.blit(background_image, [110, 0])
    # font
    window.blit(text_menu, text_menu_rec)
    # update on what is going on at the moment and what is going to happen
    pygame.display.update()
    # for every event that happens do this
    for event in pygame.event.get():
        # mouse position
        pos = pygame.mouse.get_pos()
        # if red 'x' is pushed
        if event.type == pygame.QUIT:
            # ends program
            run = False
            pygame.quit()
            quit()
        # if boutton is green start the Algorithm
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse position is over the button start game
            if buttonIsGreen.over(pos):
                main(window, 1000)
        # if mouse is hovering over or not hovering over the button
        if event.type == pygame.MOUSEMOTION:
            # if over the button show green
            if buttonIsGreen.over(pos):
                # display color
                buttonIsGreen.color = (0, 255, 0)
            else:
                # else not over the button its yellow
                buttonIsGreen.color = (yellow)

if __name__ == '__main__':
    Main_menu()
