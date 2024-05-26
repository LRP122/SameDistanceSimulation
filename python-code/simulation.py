from gentools import *
import matplotlib.pyplot as plt
import itertools

plt.ion()
a= 0

# create an instance of the Points class
Number_Points = 3
P = Points()
points = P.create(Number_Points)
partners = P.find_partners(Number_Points)
#for i in range(Number_Points):
 #   plt.scatter(points[i][0],points[i][1])
#plt.show()
combinations = list(itertools.combinations(points,2))
print(partners)
for i in range(10):
    for i in range(Number_Points):
        m_perpendicular, b_perpendicular, x_mid = (P.find_line_between_partners(
                points[partners[i][0]],
                points[partners[i][1]]))
        if abs(P.distance(points[i],points[partners[i][0]]) - P.distance(points[i],points[partners[i][1]])) > 5:
            while a < 100:
                m_perpendicular, b_perpendicular, x_mid = (P.find_line_between_partners(
                    points[partners[i][0]],
                    points[partners[i][1]]))
                test_point = P.new_position(m_perpendicular,b_perpendicular,x_mid, points[i])
                DistanceZero = float("inf")
                DistanceOne = P.minimizer(test_point, points[partners[i][0]],points[partners[i][1]])
                if DistanceOne < DistanceZero:
                    points[i] = test_point
                a += 1
        else:
            print("Nah genug")
        plt.clf()
        for k in range(Number_Points):
            plt.scatter(points[k][0], points[k][1])
        plt.draw()
        plt.pause(0.1)


#for i in range(Number_Points):
 #   plt.scatter(points[i][0],points[i][1])
P.plot_linear_line(m_perpendicular,b_perpendicular)
#plt.show()

print(P.distance(points[0],points[1]),P.distance(points[2],points[1]))
print(P.distance(points[0],points[2]),P.distance(points[0],points[1]))
print(P.distance(points[1],points[2]),P.distance(points[0],points[2]))

