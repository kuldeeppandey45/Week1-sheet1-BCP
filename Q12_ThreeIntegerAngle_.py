A = int(input())
B = int(input())
C = int(input())
def is_valid_triangle(A, B, C):
    return A + B + C == 180

if is_valid_triangle(A, B, C):
    print("yes")
else:
    print("no")
