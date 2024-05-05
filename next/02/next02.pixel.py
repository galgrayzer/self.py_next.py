class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        gray = (self._red + self._green + self._blue) // 3
        self._red = gray
        self._green = gray
        self._blue = gray

    def print_pixel_info(self):
        if self._red == self._green == 0 and self._blue > 50:
            print(
                f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) Blue')
        elif self._red == self._blue == 0 and self._green > 50:
            print(
                f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) Green')
        elif self._green == self._blue == 0 and self._red > 50:
            print(
                f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) Red')
        else:
            print(
                f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})')


def main():
    pixel = Pixel(5, 6, 250, 0, 0)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()


if __name__ == '__main__':
    main()
