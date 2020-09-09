# todo: Objectives
# 1)Main menu
# 1.5) tie main menu to A* Maze Algorithm
# 2)A* Algorithm

# When using queue for the algorithm because the algorithm is queue based not stack based
from queue import PriorityQueue

# We will use pygame as GUI
import pygame

# Width x Width
WIDTH = 1000
WIN = pygame.display.set_mode((WIDTH, WIDTH))
# Main menu height and width
# main_win = pygame.display.set_mode((500, 500))
# What to fill the back ground with
# main_win.fill((255, 255, 255))
# Window Name
pygame.display.set_caption("A* Algorithm  ")
# I will set colors as constants
# Thus they being in cap
TURQUOISE = (64, 224, 208)
GREY = (128, 128, 128)
# ALWAYS NEED RGB RIGHT
# If we already looked at that square
RED = (255, 0, 0)
# start
BLUE = (0, 255, 0)
# when there is no point
GREEN = (0, 204, 0)
YELLOW = (255, 255, 0)
# If white it is a barrier
WHITE = (255, 255, 255)
# A it is a square we have not looked at
BLACK = (0, 0, 0)
# Purple is the end node
PURPLE = (102, 0, 204)
# Start Node
ORANGE = (255, 102, 0)


# here we are going make the visualization of the actual program
# Meaning the grid and colors of each node
# NODES

class Spotterspot:
    # grid
    # constructor
    def __init__(self, row, columns, width, amount_rows):
        # rows
        self.row = row
        # x axis amount of rows
        # Columns
        self.columns = columns
        # the position of cube
        self.x = row * width
        self.y = columns * width
        # Color of cubes
        self.color = BLACK
        # each one needs to be in a black list
        self.neighbors = []
        self.width = width
        # Amount of rwos as constant
        self.amount_rows = amount_rows

    # Setting methods which will decide what color is what and other things
    # You will see below all the methods
    def get_position(self):
        # indexing rows and columns
        # NEEDS TO BE IN ORDER IT WILL BREAK MY FIRST MISTAKE
        return self.row, self.columns

    # IF this spot is closed i will return red
    # Since we already looked at that spot it returns that spot red
    def if_closed_color(self):
        # Thus we just return red
        # since red is constant we can put it anywhere
        return self.color == RED

    # if in the open set
    def if_open_color(self):
        # Returned Green
        return self.color == GREEN

    # Color will be white so this will be the barrier color
    def if_barrier_color(self):
        # Return White
        return self.color == WHITE

    # Starting Node Color
    def if_starting_color(self):
        # Return orange
        return self.color == ORANGE

    def if_end_color(self):
        return self.color == TURQUOISE

    # When the user resets it goes back to black which is the back ground
    def if_rest_color(self):
        self.color = BLACK

    # This will make the colors what they are
    # above we only set the numbers what they represent but we need to tell the program its what they are
    def is_maker_color_closed(self):
        self.color = RED

    def is_maker_color_open(self):
        self.color = GREEN

    # Barrier Color
    def is_maker_color_barrier(self):
        self.color = WHITE

    # end point
    def is_maker_color_end(self):
        self.color = TURQUOISE

    # when Path is found
    def is_maker_color_path(self):
        self.color = PURPLE

    # start point
    def is_maker_color_start(self):
        self.color = ORANGE

    # Drawing windows position
    def draw(self, win):
        # Giving the window/Rectanlge a color, x, y, width & height and where to draw/make
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # And no not like updating your neighbors on a power outage
    # Here check if the AI can go up down left right  and check if it is a barrier or not
    # then it will add it to a list so it will push to the list not pop but push
    # OVERALL IF IT IS NOT BARRIER ADD TO Neighbors
    # EXAMPLE IF IT IS NOT ONE OF YOUR NEIGHBORS ITS A BARRIER
    def update_the_neighbors(self, grider):
        self.neighbors = []
        # check if the row amount of rows is +1
        # right we are check if we could go down a row
        # DOWN
        # so if there was a barrier
        if self.row < self.amount_rows - 1 and not grider[self.row + 1][self.columns].if_barrier_color():
            # check move to the next row down and check
            self.neighbors.append(grider[self.row + 1][self.columns])

        # we already did down les do up
        # since we are going up we have to check if there is a barrier there
        if self.row > 0 and not grider[self.row - 1][self.columns].if_barrier_color():
            self.neighbors.append(grider[self.row - 1][self.columns])

        # since we did down and up now we do left
        # new we dow our columns
        # moving to the Right
        # if valid
        if self.columns < self.amount_rows - 1 and not grider[self.row][self.columns + 1].if_barrier_color():
            # check move to the next row down and check
            # if valid add to neighbors
            self.neighbors.append(grider[self.row][self.columns + 1])

        # since we did up down Right now we finally do left
        if self.columns > 0 and not grider[self.row][self.columns - 1].if_barrier_color():
            self.neighbors.append(grider[self.row][self.columns - 1])

    # A __lt__(self, other) is what most call a magic method I have used it in many of my side assignment
    # IT is really used a distant operator it used for comparing a objects distance.
    # The lt part stands for 'less than' again it is used for distands
    # since I am comparing the distance between to spot
    # meaning I am comparing my start to my finish
    # All in all I am comparing this spot to another spot on the board
    # one spot will be greater than the other spot
    # so over all this is step two of the algorithm
    # where we set up the nodes each node has a neighbor
    # can we go left or can we go right up down
    # So the nodes will have to be setup as a graph
    # Example:
    # lets say yo ran out of sugar
    # so your going to got to each neighbor until you finally found who has it which will be your end point
    # so how this going to work it is going to be setup in a graph like function
    # lets get algorithmic
    # say your start point is surrounded my barriers you cant go to your end point to get that sugar
    # so no sugar because you cant go left right up and down

    def __lt__(self, other):
        return False


# greenButton = main_menu((0, 255, 0), 150, 225, 250, 100, 'Clicked')
#######################################################################################################################
# when I did my pass pathfinding algorithm you have to assume the AI thinks the position is always infinity distance
# away
######################################################################################################################
# There are many way to do a algorithm after researching I decided to do the Heuristic method because I found it
# easier to do especially with the amount of time I have
# to be honest its more like a function
# thus we find the distance between point1 and point2

# figuring out the distance between point 1 and point 2
def heuristic(point1, point2):
    # to find distance we will use the manhattan distance formula
    # It is kind cool equation
    # So since the pathfinder cant go diagonally we are going to use that equation so it goes in a l shape
    x1, y1 = point1
    x2, y2 = point2
    # Then return the abs which is absolute distance
    return abs(x1 - x2) + abs(y1 - y2)


# Redraws the path
def path_the_Reconstruct(where_you_coming_from, current, draw):
    # where it hold not data
    while current in where_you_coming_from:
        current = where_you_coming_from[current]
        current.is_maker_color_path()
        draw()


# THIS IS WHERE MAGIC HAPPENS ALL THE COOL STUFF. THE GUTS, THE GOOD LOOKING AMAZING STUFF HAPPENS THE MAGIC
# A* ALGORITHM
def algorithm(draw, grider, start, end):
    # The reason why I can call the draw function like this is because of lambda
    # Now it does what ever the draw function does
    # draw()
    # Defining some vars so the algorithm works
    # to keep track of item in the queue
    # So the queue is zero right meow
    countin = 0
    # open set
    # uses a heap sort algorithm
    open_Q_set = PriorityQueue()
    # pushing start node to open set
    open_Q_set.put((0, countin, start))
    # keeps track of where we came from
    where_you_coming_from = {}
    # Storing G scorces
    # Remember I said the AI assumes the position is infinity away
    # Each spot visited is a Key Node so
    # I just learned list comprehension
    # more like a holder
    # float(inf) infinite
    # keep track of the current shortest distances from start to a different node
    g_key_keeper = {spotterspot: float("inf") for row in grider for spotterspot in row}
    # zero is the starting position
    g_key_keeper[start] = 0
    # This is for the start node
    # keeps track of the predicted distance from current to end
    first_key_keeper = {spotterspot: float("inf") for row in grider for spotterspot in row}
    # here I used the heuristic to guess the the distance betweeen the start and end node
    first_key_keeper[start] = heuristic(start.get_position(), end.get_position())
    # technically a hash table
    # but what ever is in the hash
    set_hash = {start}
    # while open make sure game is not quitting
    while not open_Q_set.empty():
        # where the user can still hit the red X button at the corner of the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # this will hold the store count, the start node
        # mean I will POP from the lowest node
        # also therefore meaning 'currently' is the start node
        currently = open_Q_set.get()[2]
        # got the position remove all else from the hash
        set_hash.remove(currently)

        # Found the path
        if currently == end:
            path_the_Reconstruct(where_you_coming_from, end, draw)
            end.is_maker_color_end()
            return True

        # Dont forget about your neighbors. We need our neighbor sometime
        # ALL IN ALL THIS JUST FINDS THE SHORTEST BEST PATH AND PRINTS
        for neighbor in currently.neighbors:
            temp_g_key_keeper = g_key_keeper[currently] + 1
            # Now we are keeping track of our g key mean we are keeping track of each node to
            # to figure out what is the shortest path
            # or what I am trying to say is if we found a better path update
            if temp_g_key_keeper < g_key_keeper[neighbor]:
                # where the node was just at
                where_you_coming_from[neighbor] = currently
                g_key_keeper[neighbor] = temp_g_key_keeper
                # so right here if you look on line 189 and 190 you will see that it is expecting two positions
                # not 1
                first_key_keeper[neighbor] = temp_g_key_keeper + heuristic(neighbor.get_position(), end.get_position())
                if neighbor not in set_hash:
                    # is
                    countin += 1
                    # push new neihbor because one found a better path
                    open_Q_set.put((first_key_keeper[neighbor], countin, neighbor))
                    # adding to hash
                    set_hash.add(neighbor)
                    neighbor.is_maker_color_open()
        # The reason why I can call the draw function like this is because of lambda
        # Now it does what ever the draw function does
        draw()

        if currently != start:
            currently.is_maker_color_closed()
    #
    return False


# need a list to manipulate data
def making_the_grid(rOWS, width):
    grider = []
    # gabs between rows
    # width is the of the grid
    # rows will be the how many rows we got
    # meaning the width of the little cudes
    gap = width // rOWS
    # building the grid
    for i in range(rOWS):
        # appending my empty list
        grider.append([])
        # 2D list
        for j in range(rOWS):
            # SpotterSpot = new Spotter
            # So I called the class pass in elements
            # since I called it; it is now an object
            spotterspot = Spotterspot(i, j, gap, rOWS)
            grider[i].append(spotterspot)
    return grider


# by the this function draws the grid
def draw_grid_lines(win, rOWS, width):
    gap = width // rOWS
    # here is where I draw the horizontal lines
    for i in range(rOWS):
        # I want the lines to be grey as you see below
        # we are going to multiply the current index the row the user is on by the gap
        # simply put where the grid line starts.
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        # The next for loop will be the complete opposite which will be the vertical lines
        for j in range(rOWS):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# the main drawing where it displays everything
def drawing(win, grider, rOWS, width):
    # REQUIRED FOR EVERY PYGAME TO UPDATE EVERY FRAME
    # To put it simply this will paint over everything that was on the canvas
    # Then redraw everything in its current state
    # fill grid
    win.fill(BLACK)
    # drawed the lines
    for row in grider:
        for spotterspot in row:
            spotterspot.draw(win)
    draw_grid_lines(win, rOWS, width)
    pygame.display.update()


# This function will handle the mouse click on the squares.
# so if I clicked a square it will turn white
# there for we are going to take the pos = position, rows, width
def get_the_clicked_pos(pos, rOWS, width):
    # Again define the gaps and do some division
    # not good at math
    gap = width // rOWS
    # x and y will equal the position clicked
    y, x = pos

    # position of the x and the position of the y and dividing it by the width of the cude
    row = y // gap
    column = x // gap
    # whatever the person clicked on
    return row, column


# Main function to call all the events
# this is the main loop for the program
def main(win, width):
    # How many rows there are
    HOW_MANY_ROWS = 50
    # Drawing grid
    grider = making_the_grid(HOW_MANY_ROWS, width)
    # run
    start = None
    # stop
    end = None
    # run the program
    run = True
    # if user does nothing or something
    started = False
    # runs the event and checks what they are
    # run is true
    # main_draw_func(win,grid,HOW_MANY_ROWS,width)

    while run:
        drawing(win, grider, HOW_MANY_ROWS, width)
        # This will be  for the user like if they click something wrong or the clicked the mouse button and so on
        # I looped and checked
        for event in pygame.event.get():
            # if user clicks the X button to the upper rght hand corn of the screen
            if event.type == pygame.QUIT:
                run = False
            # if user did not click the button continue
            if started:
                continue
            # *************************************************************************
            # left mouse click = 0
            # middle/wheel button = 1
            # right/mouse click 2
            # *************************************************************************
            # if user clicks the mouse button check
            # mouse button '[0]' = left mouse button then do something
            if pygame.mouse.get_pressed()[0]:
                #     # gets x y coordinate of the board
                pos = pygame.mouse.get_pos()
                row, columns = get_the_clicked_pos(pos, HOW_MANY_ROWS, width)
                # index the row and columns
                spotterspot = grider[row][columns]
                # if start and end position is nowhere to be found
                # this also checks if the end is not on top of the start
                if not start and spotterspot != end:
                    start = spotterspot
                    # call the color for the start
                    start.is_maker_color_start()
                # Have to make end not equal to start
                # just so they dont override each other
                elif not end and spotterspot != start:
                    end = spotterspot
                    end.is_maker_color_end()
                #
                elif spotterspot != end and spotterspot != start:
                    spotterspot.is_maker_color_barrier()


            # # if Right mouse button click '[2]'
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, column = get_the_clicked_pos(pos, HOW_MANY_ROWS, width)
                # index the row and columns
                spotterspot = grider[row][column]
                # right mouse click resets the button back to its current state
                # meaning since the background it black and drawing a barrier is white
                # when holding right mouse click  the square that was set as a barrier will turn white
                spotterspot.if_rest_color()
                if spotterspot == start:
                    start = None
                elif spotterspot == end:
                    end = None

            # here is where the algorithm will be call by pressing the space bar
            if event.type == pygame.KEYDOWN:
                # if space bar hasnt been pressed do nothing
                if event.key == pygame.K_SPACE and not started and end:
                    # HERE WE CALL THE NEIGHBORS FUNC
                    # for every row in the grid
                    for row in grider:
                        # and for the spots in the
                        for spotterspot in row:
                            # update the update the neighbors func
                            spotterspot.update_the_neighbors(grider)
                    # FINALLY WE CALL THE ALGORITHM MEAN WE ARE REACHING THE END
                    # passing in some arugments
                    # algorithmic function
                    # is where I pass a function within a function call
                    # meaning with lambda I can call the draw function to another function
                    # now I can call this directly from anywhere in the code
                    algorithm(lambda: drawing(win, grider, HOW_MANY_ROWS, width), grider, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grider = making_the_grid(HOW_MANY_ROWS, width)

    pygame.quit()


# if __name__ == "__main__":
#     main(WIN, WIDTH)
