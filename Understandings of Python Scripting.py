#Structured Programming 
def calculate_area(length, width):
    return length * width

def main():
    length = 5
    width = 3
    area = calculate_area(length, width)
    print(f"The area is: {area}")

if __name__ == "__main__":
    main()

#Functional Programming
def calculate_area(length, width):
    return length * width

areas = list(map(calculate_area, [5, 6, 7], [3, 4, 5]))
print(f"The areas are: {areas}")

#Object Oriented Programming
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def main():
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(6, 4)
    print(f"Area of rectangle 1: {rect1.area()}")
    print(f"Area of rectangle 2: {rect2.area()}")

if __name__ == "__main__":
    main()


