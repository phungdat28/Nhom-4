class Snake:
    def __init__(self):
        self.length = 1
        self.position = [100, 50]
        self.direction = 'down'
        self.body = [[100, 50], [90, 50], [80, 50]]

    def move(self):
        head = self.body[0]
        new_head = [head[0], head[1] + SPACE_SIZE]
        self.body.insert(0, new_head)
        self.body.pop()

class Food:
    def __init__(self):
        self.position = [random.randint(1, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE,
                         random.randint(1, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE]
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = [random.randint(1, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE,
                             random.randint(1, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE]
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self, choice):
        self.is_food_on_screen = choice
