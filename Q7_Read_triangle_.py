1 = float(input())
2 = float(input())
3 = float(input())
if 1 + 2 + 3 != 180 or 1 <= 0 or 2 <= 0 or 3 <= 0:
    print("The angles do not form a valid triangle.")
else:
    if 90 in (1, 2, 3):
        print("Right triangle")
    elif any(angle > 90 for angle in (1, 2, 3)):
        print("Obtuse triangle")
    else:
        print("Acute triangle")
