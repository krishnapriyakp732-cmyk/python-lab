import geometry

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"Area of rectangle: {geometry.area_of_rectangle(length, width)}")

radius = float(input("Enter the radius of the circle: "))
print(f"Area of circle: {geometry.area_of_circle(radius)}")
