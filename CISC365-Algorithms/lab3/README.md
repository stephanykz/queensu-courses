### Part 1
   Experiment with empirically counting, for a randomly generated set of points, the size of its convex hull.

   So create a number of sets in the plane, with each point positioned uniformly randomly around the origin. Calculate the convex hull of each set of points using one of the algorithms we've talked about in class. What is the ratio of convex hull size to number of points, averaged over the different sets?

### Part 2
   Repeat the previous question with the points normally (i.e. Gaussian) distributed around the origin. Is the ratio different?

### Part 3
   Suppose you have two sets of points in the plane (of type A and type B, maybe of different colours). Determining whether the convex hulls of the two sets of points intersect is an important problem in, for example, game design because solid objects in the game shouldn't pass through one another.

   Compute the convex hull of each set of points. One simple initial check of intersection is to compute bounding circles for each convex hull -- if the circles don't intersect, then the convex hulls won't either.

   Convex hulls don't have a centre, but we can define an approximate centre as, say, the mean position of the points on the hull. A bounding circle has this as centre, and radius equal to the point on the hull farthest from the centre. Implement this idea to check if 2 convex hulls do not intersect.

### Part 4
   Of course, the bounding circles might intersect, but the convex hulls still might not overlap. A better algorithm is based on the insight that if the convex hulls don't overlap then one of the edges of one of the convex hulls must be a separating line. If you have time, implement this idea. (You have to be careful about whether you consider two convex hulls that meet at a corner, or share a common edge line are overlapping. State the definition you choose to use.)
