#!/usr/bin/env python
# coding: utf-8

# # Change of coordinates between two frames
# 
# This demo shows the solution and some visualization of the assignment on change of coordinate systems between multiple frames. 

# In[1]:


import open3d as o3d
import copy
import numpy as np


# In[ ]:





# In[2]:


# The coordinates of point p w.r.t F{p} are:
p_c = np.array([[0.0], 
               [0.0], 
               [0.5],
               [1.0]])
print('p_c=')
print(p_c)


# In[3]:


# The coordinates of point c w.r.t F{c} are:
p_p = np.array([[0.0], 
               [0.0], 
               [0.5],
               [1.0]])
print('p_p=')
print(p_p)


# In[4]:


# Frame F{p}  (x_p, y_p, z_p)
# 
# We will consider frame p as the global frame, i.e., the canonical frame. 
# We don't need to build a matrix to represent this frame as its matrix 
# representation is the 4x4 identity matrix. 


# In[5]:


# Matrix of F{c}, i.e., Transformation from F{c} to F{p}
T_pc = np.array([[1.0, 0.0, 0.0, 1.5], 
               [0.0, 1.0, 0.0, 1.0],
               [0.0, 0.0, 1.0, 0.5],
               [0.0, 0.0, 0.0, 1.0],
              ])
print('T_pc=')
print(T_pc)


# In[6]:


# The following are the coordinates of point c written w.r.t. frame F{p}
pc_inFrame_p = T_pc @ p_c
print('pc_inFrame_p=')
print(pc_inFrame_p)


# In[7]:


# And these are coordinates of point p written w.r.t. frame F{c}
T_cp = np.linalg.inv(T_pc)   # inverse, i.e., converts from frame F{p} to frame F{c}

pp_inFrame_c = T_cp @ p_p
print('pp_inFrame_c=')
print(pp_inFrame_c)


# The following code shows a visualization of the two frames. 

# In[8]:


# Create the graphical global coordinate frame
frame0_mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()

# Mesh for frame F{c}
frame1_mesh = copy.deepcopy(frame0_mesh).transform(T_pc)

# Create a small sphere to visualize 3-D points 
mesh_sphere_c = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
mesh_sphere_c.compute_vertex_normals()
mesh_sphere_c.paint_uniform_color([0.7, 0.0, 0.7])

# Create a small sphere to visualize 3-D points 
mesh_sphere_p = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
mesh_sphere_p.compute_vertex_normals()
mesh_sphere_p.paint_uniform_color([0.5, 0.5, 0.0])

# Translate sphere to point location 
mesh_sphere_p.translate(p_p[:3])

p_c_global = T_pc @ p_c
print(p_c_global)

mesh_sphere_c.translate(p_c_global[:3])


o3d.visualization.draw_geometries([frame0_mesh, frame1_mesh, mesh_sphere_p, mesh_sphere_c])


# In[ ]:





# In[ ]:





# In[ ]:




