import math
x1, y1 = 3, 1
x2, y2 = 7, 4

point1 = (x1,y1)
point2 = (x2,y2)

def euclideanDistance(point1,point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

points = (point1,point2)

distances = ()

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances += (distance,)
        print(f"{points[i]} ve {points[j]} arasındaki mesafe: {distance:.2f}")

min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance:.2f}")
