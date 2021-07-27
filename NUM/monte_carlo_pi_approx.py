# %% A monte-carlo simulation to approximate pi
import matplotlib.pyplot as plt
import random as r
import math as m
import np
from np import linalg as la
# %% Approximate pi with monte-carlo simulation
def mc_estimate_pi(n):
    inside_count = 0
    outside_count = 0
    vector_list = []
    for i in range(n):
        # Circle in the 2*2 square has an area of pi
        """Random vectors in 1/4 of the square"""
        x = r.uniform(0,1)
        y = r.uniform(0,1)
        vector = [x,y]
        vector_list.append(vector)
        if la.norm(vector) <= 1:    # if the norm of the vector is <= 1 ==> it is in the quarter circle
            inside_count += 1
    approx_pi = 4*(inside_count/n)
    print(f"Appproximated pi is {approx_pi}")
    return([approx_pi, vector_list])    # calculate for the whole circle

#%% Visualize the results
def vis_mc_estimate_pi(vector_list, in_color="blue", out_color="red"):
    x = [a[0] for a in vector_list[1]]
    y = [a[1] for a in vector_list[1]]
    incolor = [in_color if la.norm([x[i], y[i]]) <= 1 else out_color for i in range(len(x)) ]
    figure, axes = plt.subplots()
    plt.scatter(x, y, c=incolor, s=0.01)
    axes.set_aspect(1)
    axes.add_artist(plt.Circle((0,0),1, color = 'k', fill = False))
    plt.xlim(left=0)
    plt.xlim(right=1)
    plt.ylim(bottom=0)
    plt.ylim(top=1)
    plt.title('Pi Estimate= '+str(vector_list[0]) )    #+', NoOfIterations='+str(N)+', Count Of Points Inside Circle='+str(inside_quadrant)+', Outside Circle='+str(outside_quadrant))
    return plt
#%%
out = mc_estimate_pi(100000)
out_plot = vis_mc_estimate_pi(out)
out_plot.show()


