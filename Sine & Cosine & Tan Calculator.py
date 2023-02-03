import math


def sine_calculator(angle):
    return math.sin(angle)
def cosine_calculator(angle):
    return math.cos(angle)
def tangent_calculator(angle):
    return math.tan(angle)

angle = float(input("Enter the angle in radians: "))

sine_result = sine_calculator(angle)
cosine_result = cosine_calculator(angle)
tangent_result = tangent_calculator(angle)

height = int(input("Enter the height of the triangle: "))

print("The sine of", angle, "is", sine_result)
print("The cosine of", angle, "is", cosine_result)
print("The tangent of", angle, "is", tangent_result)
# All in radians

print("\nThe right-angled triangle formation is like that:")
for i in range(1, height + 1):
    for j in range(i):
        print("*", end=" ")
    print("")

message  = """

Created by asaksh__


"""

print(message)

