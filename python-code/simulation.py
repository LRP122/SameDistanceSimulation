from gentools import *
import matplotlib.pyplot as plt
import itertools
import copy

plt.ion()


# create an instance of the Points class
Number_Points = 10
P = Points()
points = P.create(Number_Points)
partners = P.find_partners(Number_Points)
Starter_Score = (P.final_score(points,partners))

count = 0

while count < 5:
    for a in range(Number_Points):
        offset = -20
        while offset < 20:

            m_perpendicular, b_perpendicular, x_mid = (P.find_line_between_partners(
                points[partners[a][0]],
                points[partners[a][1]]))
            points_test = copy.deepcopy(points)
            test_point = P.new_position(m_perpendicular,b_perpendicular,x_mid, points_test[a], offset)

            if (P.final_score(points_test,partners)) < (P.final_score(points,partners)):
                points[a] = test_point
            offset += 0.1

        plt.clf()
        for k in range(Number_Points):
            plt.scatter(points[k][0], points[k][1])
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.draw()
        plt.pause(0.1)
    count += 1


print(f"Beginning Score {Starter_Score} \nFinal score {P.final_score(points,partners)}")



