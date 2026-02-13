import math
import matplotlib.pyplot as plt

g = (1 + math.sqrt(5)) / 2
# golden ratio

def wythoff_pairs(N):
    A = [int(math.floor(n*g)) for n in range(1, N+1)]
    B = [int(math.floor(n*g**2)) for n in range(1, N+1)]
    return list(zip(A, B))
# first N Wythoff pairs

def plot_taxicab_ball(ax, center, r):
    cx, cy = center
    poly = [(cx, cy+r), (cx+r, cy), (cx, cy-r), (cx-r, cy), (cx, cy+r)]
    xs, ys = zip(*poly)
    ax.plot(xs, ys, linewidth=1)
# plot L1 ball (diamond shape)

def show_wythoff_with_L1_balls(K=120, R_list=(10, 30, 60)):
    # We want to generate first 120 Wythoff pairs and plot L1 balls of radius 10, 30, 60
    pts = wythoff_pairs(K)
    fig, ax = plt.subplots(figsize=(6,6))
    ax.scatter([x for x,_ in pts], [y for _,y in pts], s=8)
    for r in R_list:
        plot_taxicab_ball(ax, (0,0), r)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Wythoff pairs with Taxicab (L1) balls")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.tight_layout()
    plt.show()

show_wythoff_with_L1_balls()

# Conclusion:
# The blue scattered points in the figure is close to a straight line with slope g.
# The L1 balls (diamonds) centered at the origin show that the Wythoff pairs are approximately
# evenly distributed in the L1 metric, as they intersect the balls in a roughly uniform manner