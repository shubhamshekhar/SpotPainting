import colorgram
from turtle import Turtle, Screen
import random


class SpotPainting:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.colors = []
        self.number_of_colors_to_extract = 20
        self.screen_width = 640
        self.screen_height = 640
        self.screen = Screen()
        self.screen.colormode(255)
        self.screen.title("Spot Painting")
        self.screen.setup(self.screen_width, self.screen_height)

    def extract_color_from_image(self):
        self.colors = colorgram.extract('hirst.jpg', self.number_of_colors_to_extract)

    def move_pointer_to_left_bottom(self):
        self.turtle.penup()
        self.turtle.setpos(-self.screen_width/2 + 40, -self.screen_height/2 + 40)
        self.turtle.pendown()

    def get_random_colour(self):
        random_index = random.randint(0, self.number_of_colors_to_extract-1)
        return self.colors[random_index]

    def draw_spot_on_position(self, color):
        self.turtle.dot(20, (color.rgb.r, color.rgb.g, color.rgb.b))

    def move_turtle_to_next_position(self):
        self.turtle.penup()
        current_turtle_position = self.turtle.position()
        if current_turtle_position[0] >= self.screen_width/2 - 40:
            self.turtle.setpos(- self.screen_width/2 + 40, current_turtle_position[1] + 40)
            if current_turtle_position[1] >= self.screen_height / 2 - 40:
                return True
        else:
            self.turtle.setpos(current_turtle_position[0] + 40, current_turtle_position[1])

        self.turtle.pendown()
        return False

    def draw(self):
        self.extract_color_from_image()
        self.move_pointer_to_left_bottom()
        self.turtle.speed("fastest")
        reached_the_top = False
        while not reached_the_top:
            color = self.get_random_colour()
            self.draw_spot_on_position(color)
            reached_the_top = self.move_turtle_to_next_position()
        self.screen.exitonclick()
