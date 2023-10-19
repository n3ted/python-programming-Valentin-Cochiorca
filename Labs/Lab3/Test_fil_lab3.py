# Exempel på hur du kan använda klasserna:

from geometry_shapes import Circle, Rectangle

cirkel1 = Circle(x=0, y=0, radius=1)
cirkel2 = Circle(x=1, y=1, radius=1)
rektangel = Rectangle(x=0, y=0, side1=1, side2=1)

print(cirkel1 == cirkel2)  # True
print(cirkel2 == rektangel)  # False
print(cirkel1.is_point_inside(0.5, 0.5))  # True
cirkel1.translate(5, 5)
print(cirkel1.is_point_inside(0.5, 0.5))  # False
cirkel1.translate("TRE", 5)  # Invalid coordinates. Please provide numeric values.

##########################################


rektangel1 = Rectangle(0, 0, 4, 3)
rektangel2 = Rectangle(0, 0, 6, 2)
cirkel1 = Circle(0, 0, 2)
cirkel2 = Circle(0, 0, 1)

print(rektangel1)
print(cirkel1)

rektangel1.translate(2, 2)
cirkel1.translate(1, 1)

print(rektangel1)
print(cirkel1)

print(f"Rektangel1 är en kvadrat: {rektangel1.is_square()}")
print(f"Cirkel1 är en enhetscirkel: {cirkel1.is_unit_circle()}")

print(f"Rektangel1 är lika med Rektangel2: {rektangel1 == rektangel2}")
print(f"Cirkel1 är mindre än Cirkel2: {cirkel1 < cirkel2}")
