import open3d as o3d
import copy
import numpy as np


# Create the graphical global coordinate frame
frame0_mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()



# Frame 1 matrix (Transformation from F{1} (c) to F{0} (p))
T1 = np.array([[1.0, 0.0, 0.0, 1.5], 
               [0.0, 1.0, 0.0, 1.0],
               [0.0, 0.0, 1.0, 0.5],
               [0.0, 0.0, 0.0, 1.0],
              ])

# Mesh for frame F{1}
frame1_mesh = copy.deepcopy(frame0_mesh).transform(T1)


# This is a point on frame c (i.e., Frame F{1})
pc = np.array([[0.0], 
               [0.0], 
               [0.5],
               [1.0]])

print('Point in frame c:')
print(pc)

# Create a small sphere to visualize 3-D points 
mesh_sphere_c = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
mesh_sphere_c.compute_vertex_normals()
mesh_sphere_c.paint_uniform_color([0.7, 0.0, 0.7])




# This is a point on frame p (i.e., Frame F{0})
pp = np.array([[0.0], 
               [0.0], 
               [0.5],
               [1.0]])



print('Point in frame p:')
print(pp)


# Create a small sphere to visualize 3-D points 
mesh_sphere_p = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
mesh_sphere_p.compute_vertex_normals()
mesh_sphere_p.paint_uniform_color([0.5, 0.5, 0.0])


# Translate sphere to point location 

mesh_sphere_p.translate(pp[:3])

pc_global = T1 @ pc
print(pc_global)

mesh_sphere_c.translate(pc_global[:3])


o3d.visualization.draw_geometries([frame0_mesh, frame1_mesh, mesh_sphere_p, mesh_sphere_c])

