import random
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Number_Points = 10
class Points():

    def __init__(self):
        self.x = round(random.uniform(0,100),1)
        self.y = round(random.uniform(0,100),1)

    def distance(self,x1,y1,x2,y2):
        dist = (math.sqrt(pow((x1-x2),2) + pow((y1-y2)),2))
        return dist

    def create(self):
        self.Points_Created = [Points() for _ in range(Number_Points)]
        self.Points_Created_x = [P.x for P in self.Points_Created]
        self.Points_Created_y = [P.y for P in self.Points_Created]
        self.Points_Dicts = {}
        for count,x,y in zip([i for i in range(len(self.Points_Created_x))],self.Points_Created_x,self.Points_Created_y):
            self.Points_Dicts[count] = {1 : x,
                                        2 : y}
        return self.Points_Dicts

    def sketch(self,m,b):
        plt.scatter(self.Points_Created_x,self.Points_Created_y)
        x = np.linspace(0, 100, 400)
        y = m * x + b

        plt.plot(x, y, '-r', label='y=mx+b')
        plt.title('Graph of the line y = mx + b')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='best')
        plt.grid()
        plt.show()

    def find_partners(self):
        self.big_partner_dict = {}
        self.small_partner_dict = {}
        self.small_partner_dict_array = []
        for i in range(Number_Points):
            for b in range(1, 3):
                self.small_partner_dict[b] = random.randint(1, 9)
            self.small_partner_dict_array.append(self.small_partner_dict)
            self.small_partner_dict = {}

        Keys = range(1, (Number_Points))

        for i in Keys:
            self.big_partner_dict[i] = self.small_partner_dict_array[i]
        return self.big_partner_dict

    def find_line_between_partners(self, point1, point2):
        """
        returns the linear function between the two partner points
        for any point on this line the condition of same distance will be met
        y = mx + b
        """
        x1 = point1[1]
        x2 = point1[2]
        y1 = point2[1]
        y2 = point2[2]
        mid_x = ((x1 + x2)/2)
        mid_y = ((y1 + y2) /2)

        if x2 - x1 == 0:  # Avoid division by zero
            return None, None
        else:
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            m_perpendicular = m / (-1)


            return round(m,2), round(b,2)

















