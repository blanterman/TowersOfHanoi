from Stack import Stack

# This game is an implementation of the game Towers of Hanoi
# This game was developed as an exercise to learn about stacks, so the stack 
# data structure is fully implemented

# There are 3 posts that the rings can be on. A stack is initialized for each 
# post to keep track of rings. 
post1 = Stack("Post 1")
post2 = Stack("Post 2")
post3 = Stack("Post 3")

# Put the post stacks in a list for ease of reading and manipulating
posts = [post1, post2, post3]

# Ring class that has size and ascii art drawing representation
class Ring:
    
    def __init__(self, size):
        self.size = size
    
    def __repr__(self):
        ring_drawing = ""
        num_dashes = self.size * 2 + 1
        ring_drawing += "|"
        for i in range(num_dashes):
            ring_drawing += "-"
        ring_drawing += "|"
        return ring_drawing
    
    def get_size(self):
        return self.size

# Draws the top of the posts that will be visible no matter how many rings 
# there are. Their spacing changes depending on the size of the larges ring
# The size of the largest ring is equal to the global number of rings set by
# the user.
def draw_top_of_posts():
    row_of_text = ""
    for post in posts:
        for i in range(num_rings + 1):
            row_of_text += " "
        row_of_text += "_"
        for i in range(num_rings + 1):
            row_of_text += " "
    print(row_of_text)
    row_of_text = ""
    for post in posts:
        for i in range(num_rings):
            row_of_text += " "
        row_of_text += "| |"
        for i in range(num_rings):
            row_of_text += " "
    print(row_of_text)

# Draws the base of the posts that will be visible no matter how many rings 
# there are. Each post is labled with a number. The spacing of the labels 
# changes depending on the size of the larges ring
# The size of the largest ring is equal to the global number of rings set by
# the user.
def draw_base():
    row_of_text = ""
    for i in range(len(posts)):
        for j in range(num_rings + 1):
            row_of_text += "/"
        row_of_text += str(i + 1)
        for j in range(num_rings + 1):
            row_of_text += "/"
    print(row_of_text)


# Ascii art printout of the current state of the posts with the rings.
def draw_hanoi(post_contents):
    
    # First draw the tops of the posts
    draw_top_of_posts()
    
    # Make all the post stacks the same size, filling empty slots with Nones 
    for post in post_contents:
        if len(post) == 0:
            for i in range(num_rings):
                post.append(None)
        else:
            post.reverse()
            while len(post) != num_rings:
                post.append(None)
            post.reverse()
            
    # Next draw the rings or an empty post in every position of each post
    for i in range(num_rings):
        for j in range(len(posts)):
            ring_text = ""
            ring = post_contents[j][i]
            try:
                if ring:
                    for k in range(num_rings - ring.get_size()):
                        ring_text += " "
                    ring_text += str(ring)
                    for k in range(num_rings - ring.get_size()):
                        ring_text += " "
                    print(ring_text, end = "" if j != len(posts) - 1 else "\n")
                else:
                    for k in range(num_rings):
                        ring_text += " "
                    ring_text += "| |"
                    for k in range(num_rings):
                        ring_text += " "
                    print(ring_text, end = "" if j != len(posts) - 1 else "\n")
            except IndexError:
                for k in range(num_rings):
                    ring_text += " "
                ring_text += "| |"
                for k in range(num_rings):
                    ring_text += " "
                print(ring_text, end = "" if j != len(posts) - 1 else "\n")
    
    # Finally, draw the base with the labels of the posts
    draw_base()

# Checks the selected move to see if it is a valid move
def is_valid_move(source, destination):
    if source.is_empty():
        print("Cannot select an empty post as source")
        return False
    elif destination.is_empty():
        return True
    elif source.peek().get_size() < destination.peek().get_size():
        return True
    else:
        print("Destination must be empty or have a larger ring than the source post")
        return False

# Moves the ring from one post to another using pop and push
def move_ring(source, destination):
    if is_valid_move(source, destination):
        ring_to_move = source.pop()
        destination.push(ring_to_move)

# Checks to see if the current state of the game is a victory
def victory(post3_list):
    try:
        if len(post3_list) != num_rings:
            return False
    except TypeError:
        return False
    return True

# Updates the ascii drawing of the current state of the game
def update_view():
    post_contents = [post.listify_stack_values() for post in posts]
    draw_hanoi(post_contents)

# Initialize game variables
play_game = True
cont = True
valid_input = False

# Get the users input for the number of rings
while not valid_input:
    try:
        valid_input = True
        print("\n*************************************************************\
               \n*                                                           *\
               \n*              WELCOME TO THE TOWERS OF HANOI!              *\
               \n*                                                           *\
               \n*  PLEASE INPUT THE NUMBER OF RINGS YOU WISH TO PLAY WITH   *\
               \n*                                                           *\
               \n*************************************************************")
        num_rings = int(input())
    except ValueError:
        valid_input = False
        print("\nPlease enter a number.\n")

for i in range(num_rings, 0, -1):
    post1.push(Ring(i))

# Print the initial state of the game
update_view()

# Game loop
while play_game:
    try:
        source = int(input("Select post 1, 2, or 3 with ring to move. "))
        destination = int(input("Where would you like to move the ring to? "))
        cont = True
    except (TypeError, ValueError):
        cont = False
        print("Input not valid")
    
    try:
        source_object = posts[source - 1]
        destination_object = posts[destination - 1]
        cont = True
    except (NameError, IndexError, TypeError, ValueError):
        cont = False
        print("Please make valid selections for your move")
    
    if cont:
        move_ring(source_object, destination_object)
        update_view()
        if victory(post3.listify_stack_values()):
            print("\n***************************************\
                   \n*                                     *\
                   \n*             VICTORY!                *\
                   \n*                                     *\
                   \n***************************************")
            play_game = False
    
