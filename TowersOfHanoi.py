from Stack import Stack

# This will implement a version of the game Towers of Hanoi
post1 = Stack("Post 1")
post2 = Stack("Post 2")
post3 = Stack("Post 3")
posts = [post1, post2, post3]

class Ring:
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size
    def draw_ring(self):
        ring_drawing = ""
        num_dashes = self.size * 2 + 1
        num_top_spaces = abs(self.size - 4)
        num_bottom_spaces = abs(self.size - 3)
        for i in range(num_bottom_spaces):
            ring_drawing += " "
        ring_drawing += "|"
        for i in range(num_dashes):
            ring_drawing += "-"
        ring_drawing += "|"
        for i in range(num_bottom_spaces):
            ring_drawing += " "
        return ring_drawing

def draw_hanoi(pillar_contents):
    print("    _        _        _    ")
    print("   | |      | |      | |   ")
    try:
        print(pillar_contents[0][0].draw_ring(), end = "")
    except (IndexError, TypeError):
        print("   | |   ", end = "")
    try:
        print(pillar_contents[1][0].draw_ring(), end = "")
    except (IndexError, TypeError):  
        print("   | |   ", end = "")
    try:
        print(pillar_contents[2][0].draw_ring())
    except (IndexError, TypeError):
        print("   | |   ")
    try:
        print(pillar_contents[0][1].draw_ring(), end = "")
    except (IndexError, TypeError):
        print("   | |   ", end = "")
    try:
        print(pillar_contents[1][1].draw_ring(), end = "")
    except (IndexError, TypeError):
        print("   | |   ", end = "")
    try:
        print(pillar_contents[2][1].draw_ring())
    except (IndexError, TypeError):
        print("   | |   ")
    try:
        print(pillar_contents[0][2].draw_ring(), end = "")
    except (IndexError, TypeError):
        print("   | |   ", end = "")
    try:
        print(pillar_contents[1][2].draw_ring(), end = "")
    except (IndexError, TypeError):
        print("   | |   ", end = "")
    try:
        print(pillar_contents[2][2].draw_ring())
    except (IndexError, TypeError):
        print("   | |   ")

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
        if len(post3_list) != 3:
            return False
    except TypeError:
        return False
    victory_sizes = [1, 2, 3]
    for i in range(len(post3_list)):
        print(str(victory_sizes[i]) + "->" + str(post3_list[i].get_size()))
        if victory_sizes[i] != post3_list[i].get_size():
            return False
    return True

def update_view():
    post_contents = [post.listify_stack_values() for post in posts]
    draw_hanoi(post_contents)

large_ring = Ring(3)
medium_ring = Ring(2)
small_ring = Ring(1)

post1.push(large_ring)
post1.push(medium_ring)
post1.push(small_ring)

update_view()

play_game = True

while play_game:
    source = int(input("Select post 1, 2, or 3 with ring to move"))
    destination = int(input("Where would you like to move the ring to?"))
    
    try:
        source_object = posts[source - 1]
        destination_object = posts[destination - 1]
    except (IndexError, TypeError):
        print("Please make valid selections for your move")
    
    move_ring(source_object, destination_object)
    update_view()
    if victory(post3.listify_stack_values()):
        print("You won! Yay!")
        play_game = False
    
