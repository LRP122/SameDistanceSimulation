import random
import math
import matplotlib.pyplot as plt
import pandas as pd

Number_Points = 10
class Points():

    def __init__(self):
        self.x = random.uniform(0,100)
        self.y = random.uniform(0,100)

    def distance(self,x1,y1,x2,y2):
        dist = (math.sqrt(pow((x1-x2),2) + pow((y1-y2)),2))
        return dist

    def create_and_sketch(self):
        self.Points_Created = [Points() for _ in range(Number_Points)]
        self.Points_Created_x = [P.x for P in self.Points_Created]
        self.Points_Created_y = [P.y for P in self.Points_Created]
        plt.scatter(self.Points_Created_x, self.Points_Created_y)
        plt.show()

    def find_partners(self):
        self.big_partner_dict = {}
        self.small_partner_dict = {}
        self.small_partner_dict_array = []
        for i in range(100):
            for b in range(1, 3):
                self.small_partner_dict[b] = random.randint(1, 99)
            self.small_partner_dict_array.append(self.small_partner_dict)
            self.small_partner_dict = {}

        Keys = range(1, 100)

        for i in Keys:
            self.big_partner_dict[i] = self.small_partner_dict_array[i]
        return self.big_partner_dict









