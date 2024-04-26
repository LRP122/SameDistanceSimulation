from gentools import *
import matplotlib.pyplot as plt

# create an instance of the Points class

points_instance = Points()


# call the create_and_sketch method on the instance
K = points_instance.create()
partners = points_instance.find_partners()
#print(K)

#print(partners)
first_partner = K[1]
second_partner = K[2]
print(first_partner)
print(second_partner)

m, b, mp, bp = points_instance.find_line_between_partners(first_partner,second_partner)

points_instance.sketch(m,b)
points_instance.sketch(mp,bp)
print(f"m ist {m} \nmp ist {mp}")
print(f"m ist {b} \nmp ist {bp}")
plt.scatter([first_partner[1], second_partner[1]],[first_partner[2], second_partner[2]], color = "red" )
plt.show()
#print(K.find_partners())


