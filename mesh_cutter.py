"""Drag the sphere to cut the mesh interactively
Use mouse buttons to zoom and pan"""
from vedo import *
import os  


# Read mesh file 
#fileName = 'https://people.sc.fsu.edu/~jburkardt/data/ply/chopper.ply'

#fileName = './clipped.vtk'

#fileName = "./tail_rotor.vtk"
fileName = "./main_body.vtk"


s = Mesh(fileName)

# Crop mesh. Result is saved as file clipped.vtk
plt = show(s, __doc__, bg='black', bg2='bb', interactive=True)

plt.add_cutter_tool(s, mode='box',invert=True) #modes= sphere, plane, box
plt.close()

# Display parts 
#s = Mesh('clipped.vtk')

#plt = show(s, __doc__, bg='black', bg2='bb', interactive=True)


