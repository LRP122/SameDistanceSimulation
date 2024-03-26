## Same distance simulation

# General Concept
A number of points is created, every point has a position x and y.
Each point chooses freely (randomly) two other points. Each point then has to achieve to be at a eqal distance from both other points.

We will create all the points, have them choose two partners.
Then the first point will move so he is at a same distance (plus minus a bit) of both points before we move the second point. 
After all points have moved, we will restart with point one, if he does not allready fullfill the condtion. We will iterate this until every conditon is met.