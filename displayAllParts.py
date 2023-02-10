"""Showing all mesh parts segmented by color"""
from vedo import *
import os  
from os import path
import wget


# Path to github raw content of files. 
# We need to use raw.githubusercontent.com otherwise we download 
# an html file 
urlPath = "https://raw.githubusercontent.com/eraldoribeiro/changeOfCoordinates/main/"

# Filenames (individual mesh parts)
fn_mainBody = "main_body.vtk"
fn_topRotor = "top_rotor.vtk"
fn_tailRotor = "tail_rotor.vtk"
  
# Download the meshes from repository if we don't have them already 
if not path.exists(fn_mainBody):
    response = wget.download(urlPath + fn_mainBody)
        
if not path.exists(fn_topRotor): 
    response = wget.download(urlPath + fn_topRotor)
        
if not path.exists(fn_tailRotor): 
    response = wget.download(urlPath + fn_tailRotor)
          

# Read mesh files of each part, and color-label them
mainBodyMesh = Mesh(fn_mainBody).c("white")
topRotorMesh = Mesh(fn_topRotor).c("red")
tailRotorMesh = Mesh(fn_tailRotor).c("blue")

# Show everything 
plt = show([mainBodyMesh, topRotorMesh, tailRotorMesh], __doc__, bg='black', bg2='bb', interactive=True, axes=1, viewup='z')

plt.close()

