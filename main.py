from shapes import Shape, Circle, Rectangle, Triangle

def main():
    #shapes call
    circle = Circle("red", 10)
   
    rectangle = Rectangle("blue", 3, 5)
    
    triangle = Triangle("pink", 3, 3, 3)
    
    #store shapes in list
    shapes = [circle, rectangle, triangle]
    #iterate over list of shapes
    for shape in shapes:
        print(f"Area is: {shape.calculate_area():.2f}")
        print(f"Perimeter is: {shape.calculate_perimeter():.2f}")
        print()

if __name__ == "__main__":
    main()