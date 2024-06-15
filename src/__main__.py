from gentools import *
import matplotlib.pyplot as plt
import copy

plt.ion()
Number_Points = 5
P = Points()
points = P.create(Number_Points)
partners = P.find_partners(Number_Points)
Starter_Score = (P.final_score(points,partners))

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
colors = colors * (Number_Points // len(colors)) + colors[:Number_Points % len(colors)]

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
            plt.scatter(points[k][0], points[k][1], color=colors[k], label = f"Point {k}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend(loc="upper right")
        plt.draw()
        plt.pause(0.1)
    count += 1


print(f"Beginning Score {Starter_Score} \nFinal score {P.final_score(points,partners)}")



