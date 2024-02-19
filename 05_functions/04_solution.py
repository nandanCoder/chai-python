import math
def circle_stats(radius):
    area =  math.pi*radius*radius
    circumference = 2 * math.pi*radius
    return area,circumference

a,c = circle_stats(5)

print("Area: ",round(a,2) ,"Circumference: ",round(c,2))

# round to hep gate 2 number . porar