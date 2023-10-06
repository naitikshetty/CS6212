import time
import random


def divide(points, p1, p2):#divide function of the algortihm
    if not points:
        return []
    # Find the point farthest from the line defined by p1 and p2
    farthest_point = max(points, key=lambda pointer: distance(p1, p2, pointer))
        
    # Split the points into left and right sets
    left = [pointer for pointer in points if is_left(p1,farthest_point, pointer)]
    right = [pointer for pointer in points if is_left(farthest_point, p2, pointer)]
    # Recursively find the hull on both sides and combine them
    left_hull = divide(left, p1, farthest_point)#recursive call 1
    right_hull = divide(right, farthest_point, p2)#recursive call 2
        
    return [p1] + left_hull + [farthest_point] + right_hull#merging the points to get the convex hull points
def distance(p1, p2, p3):#vector cross product to find distance
    # Calculate the distance from point p3 w.r.t line p1 and p2
    return abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]))
    
def is_left(p1, p2, p3):# Check if point p3 is to the left of the line p1, p2
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0


    
    
def merge(points):#merge function
    if len(points) < 3:#base case since a convex hull can have minimum 3 points
        return points
         
    # Finding the extreme points (leftmost and rightmost) for the initial hull
    leftmost = min(points, key=lambda point: point[0])
    rightmost = max(points, key=lambda point: point[0])
    # Divide the points into above and below the line w.r.t the extreme points
    above = [point for point in points if is_left(leftmost,rightmost, point)]
    below = [point for point in points if is_left(rightmost, leftmost, point)]
    # Finding the hull on both sides and combine them
    upper_hull = divide(above, leftmost, rightmost)
    lower_hull = divide(below, rightmost, leftmost)
    # Combining the upper and lower hulls to get the final convex hull
    convex_hull = upper_hull + lower_hull;
    
    return convex_hull;

# Driver Input program:
nlenght = int(input("Enter elements:"));
points = [];
for i in range(1,nlenght+1):
    w = random.randint(-9,9);
    v = random.randint(-9,9);
    points.append((w,v));
start = time.time();
print("Input",points)
convex_hull = merge(points)
convex_hull = list(set(convex_hull));
print(convex_hull)
end =time.time();
print(start);
print(end);
print(end-start);
