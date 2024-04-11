from gentools import *

# create an instance of the Points class

points_instance = Points()


# call the create_and_sketch method on the instance
K = points_instance.create()
partners = points_instance.find_partners()
print(K)

#print(partners)
first_partner = K[1]
second_partner = K[2]

m, b = points_instance.find_line_between_partners(first_partner,second_partner)
print(f"{m}x + {b}")

points_instance.sketch(m,b)


