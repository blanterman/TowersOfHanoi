from Stack import Stack

# This will implement a version of the game Towers of Hanoi
post1 = Stack("Post 1")
post2 = Stack("Post 2")
post3 = Stack("Post 3")
posts = [post1, post2, post3]

class Ring:
    def __init__(self, size):
        self.size = size
    def __repr__(self):
        return str(self.size)
    def get_size(self):
        return self.size
    def draw_ring(self):
        ring_drawing = ""
        num_dashes = self.size * 2 + 1
        ring_drawing += "|"
        for i in range(num_dashes):
            ring_drawing += "-"
        ring_drawing += "|"
        return ring_drawing

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

def draw_base():
    row_of_text = ""
    for i in range(len(posts)):
        for j in range(num_rings + 1):
            row_of_text += "/"
        row_of_text += str(i + 1)
        for j in range(num_rings + 1):
            row_of_text += "/"
    print(row_of_text)

def draw_hanoi(pillar_contents):
    draw_top_of_posts()
    for pillar in pillar_contents:
        if len(pillar) == 0:
            for i in range(num_rings):
                pillar.append(None)
        else:
            pillar.reverse()
            while len(pillar) != num_rings:
                pillar.append(None)
            pillar.reverse()
    for i in range(num_rings):
        for j in range(len(posts)):
            ring_text = ""
            ring = pillar_contents[j][i]
            try:
                if ring:
                    for k in range(num_rings - ring.get_size()):
                        ring_text += " "
                    ring_text += str(ring.draw_ring())
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
    draw_base()

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

def move_ring(source, destination):
    if is_valid_move(source, destination):
        ring_to_move = source.pop()
        destination.push(ring_to_move)

def victory(post3_list):
    try:
        if len(post3_list) != num_rings:
            return False
    except TypeError:
        return False
    return True

def update_view():
    post_contents = [post.listify_stack_values() for post in posts]
    draw_hanoi(post_contents)

num_rings = int(input("\nPlease input the number of rings that you would like "))
for i in range(num_rings, 0, -1):
    post1.push(Ring(i))

update_view()
play_game = True
cont = True

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
            print("You won! Yay!")
            play_game = False
    
