import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[charter]{mathdesign}')
plt.rc('font', family='serif')

plt.axes()
plt.gcf().set_size_inches(3,3)
ax = plt.gca()
s = 1.2

def rotation_matrix(a):
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    
ax.set_aspect(1)
ax.axis('off')
sq = np.sqrt(3)/2
points = [[1, 0], [0.5, sq], [-0.5, sq], [-1,0], [-0.5, -sq], [0.5, -sq]]
points = [rotation_matrix(np.pi/6)@x for x in points]
points = [list(x) for x in points]

# print(points); exit()

lines = patches.Polygon(points, closed=True, fill=True, facecolor='0.9', edgecolor='k', lw=0.5)
ax.add_patch(lines)
for x in points:
    ax.add_patch(patches.Circle(x, radius=0.04, fill=True, facecolor='k'))
ax.add_patch(patches.Circle([0,0], radius=0.04, fill=True, facecolor='k'))

ax.text(s*points[0][0], s*points[0][1], "$K$", ha='center', va='center')
ax.text(s*points[2][0], s*points[2][1], "$K$", ha='center', va='center')
ax.text(s*points[4][0], s*points[4][1], "$K$", ha='center', va='center')
ax.text(s*points[1][0]-0.05, points[1][1]+0.05, "$K'$", ha='right', va='center')
ax.text(s*points[3][0], s*points[3][1], "$K'$", ha='center', va='center')
ax.text(s*points[5][0], s*points[5][1], "$K'$", ha='center', va='center')
ax.text(-0.2, 0, "$\Gamma$", ha='right', va='center')

ax.add_patch(patches.FancyArrow(0, 0, 1.5, 0, width=0.0, head_width=0.08, length_includes_head=True, fc = 'k', lw=0.5))
ax.add_patch(patches.FancyArrow(0, 0, 0, 1.5, width=0.0, head_width=0.08, length_includes_head=True, fc = 'k', lw=0.5))

ax.text(1.04*1.5,0, "$k_x$", ha='left', va='center')
ax.text(0,1.04*1.5, "$k_y$", ha='center', va='bottom')

L = 1.6
plt.xlim(-L,L)
plt.ylim(-L,L)
plt.savefig('hexaPy.pdf')