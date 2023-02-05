"""Showing all mesh parts segmented by color"""
from vedo import *
import os  


# Read mesh file 
#fileName = 'https://people.sc.fsu.edu/~jburkardt/data/ply/chopper.ply'

# Read mesh files of each part, and color-label them
mainBodyMesh = Mesh("./main_body.vtk").c("white")
topRotorMesh = Mesh("./top_rotor.vtk").c("red")
tailRotorMesh = Mesh("./tail_rotor.vtk").c("blue")

# Show everything 
plt = show([mainBodyMesh, topRotorMesh, tailRotorMesh], __doc__, bg='black', bg2='bb', interactive=True, axes=1, viewup='z')

plt.close()

