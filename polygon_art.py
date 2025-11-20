# Panisara Niyathirakul # id : 6810545751
import turtle
import random

class DrawPolygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):  
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        angle = 360 / self.num_sides
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(angle)
        turtle.penup()

    def ratio_reduction(self):
        reduction_ratio = 0.618
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        new_loc = [turtle.xcor(), turtle.ycor()]
        new_size = self.size * reduction_ratio
        inner_poly = DrawPolygon(self.num_sides, new_size, self.orientation,new_loc, self.color, self.border_size)
        inner_poly.draw_polygon()


class Gallery:
    def __init__(self):
        self.run()

    def random_color(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def random_info(self):
        size = random.randint(50,150)
        orient = random.randint(0,90)
        loc = [random.randint(-300,300), random.randint(-200,200)]
        color = self.random_color()
        border = random.randint(1,10)
        return size,orient,loc,color,border

    def make_polygon(self,sides):
        size,orient,loc,color,border = self.random_info()
        return DrawPolygon(sides,size,orient,loc,color,border)

    # art choice
    def art1(self):
        for _ in range(30):
            self.make_polygon(3).draw_polygon()

    def art2(self):
        for _ in range(30):
            self.make_polygon(4).draw_polygon()

    def art3(self):
        for _ in range(30):
            self.make_polygon(5).draw_polygon()

    def art4(self):
        for _ in range(30):
            sides = random.randint(3,5)
            self.make_polygon(sides).draw_polygon()

    def art5(self):
        for _ in range(30):
            poly = self.make_polygon(3)
            poly.draw_polygon()
            poly.ratio_reduction()
            DrawPolygon(3,poly.size*0.618,poly.orientation,poly.location,poly.color,poly.border_size).ratio_reduction()

    def art6(self):
        for _ in range(30):
            poly = self.make_polygon(4)
            poly.draw_polygon()
            poly.ratio_reduction()
            DrawPolygon(4,poly.size * 0.618,poly.orientation,poly.location,poly.color,poly.border_size).ratio_reduction()

    def art7(self):
        for _ in range(30):
            poly = self.make_polygon(5)
            poly.draw_polygon()
            poly.ratio_reduction()
            DrawPolygon(5,poly.size * 0.618,poly.orientation,poly.location,poly.color,poly.border_size).ratio_reduction()

    def art8(self):
        for _ in range(30):
            sides = random.randint(3,5)
            poly = self.make_polygon(sides)
            poly.draw_polygon()
            poly.ratio_reduction()
            DrawPolygon(sides,poly.size * 0.618,poly.orientation,poly.location,poly.color,poly.border_size).ratio_reduction()

    def art9(self):
        random.choice([self.art1, self.art2, self.art3, self.art4,self.art5, self.art6, self.art7, self.art8])()

    def run(self):
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)
        arts = {1: self.art1, 2: self.art2, 3: self.art3, 4: self.art4, 5: self.art5, 6: self.art6, 7: self.art7, 8: self.art8, 9: self.art9,}

        if choice in arts:
            arts[choice]()
        else:
            print("Invalid choice!")
        turtle.update()

# main code
Gallery()
turtle.done()