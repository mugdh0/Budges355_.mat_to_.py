#import the SciPy Library
#if not available install using pip install scipy
import scipy.io as sp

#load the .mat file using loadmat() function, file path is the reqired parameter
data = sp.loadmat(r"C:\Budges355\clip_15\point3D_bird.mat") #use your file path

#data will give a dict which contain the "point3d" variable. where the coorinates are stored
point3d = data["point3d"]
# print(data)
print(point3d)
# importing mplot3d toolkits, numpy and matplotlib
print(type(point3d))

#visualize the coordinate in 3d plane
import matplotlib.pyplot as plt
fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection='3d')

# defining all 3 axes+
for x, y, z in point3d:
    ax.plot3D(x, y, z)
    ax.scatter(x, y, z)

# plotting
ax.set_title('3D plot')
plt.show()
