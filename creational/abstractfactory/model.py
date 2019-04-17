class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def paint(self, factory):
        point = factory.get_point()
        corner = factory.get_corner()
        corner.left_up()
        point.line(self.width - 2)
        corner.right_up()
        print()
        for i in range(self.height - 2):
            point.line(self.width)
            print()
        corner.left_down()
        point.line(self.width - 2)
        corner.right_down()
        print()


class Dot:
    def line(self, width):
        for i in range(width):
            print("-", end='')


class Sharp:
    def left_up(self):
        print("#", end='')

    def left_down(self):
        print("#", end='')

    def right_up(self):
        print("#", end='')

    def right_down(self):
        print("#", end='')


class DotSharpFactory:
    def get_point(self):
        return Dot()

    def get_corner(self):
        return Sharp()
