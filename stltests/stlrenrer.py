from stl import mesh
from matplotlib import pyplot
from mpl_toolkits import mplot3d

figure = pyplot.figure()

axes = mplot3d.Axes3D(figure)

my_mesh = mesh.Mesh.from_file("untitled.stl")
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(my_mesh.vectors))

scale = my_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)
pyplot.show()
