## The helicopter animation

#### Overview

In this assignment, you will create an animation of an object represented by a triangulated mesh. You will animate the mesh of a helicopter shown in Figure 1 from its `.ply` file `chopper.ply`. This file and other mesh files are available from [John Burkardt's webpage](https://people.sc.fsu.edu/~jburkardt/data/ply/ply.html). 

![img](https://people.sc.fsu.edu/~jburkardt/data/ply/chopper.png)

**Figure 1**: A triangulated mesh of a helicopter. 

You will animate the helicopter's two rotor blades (i.e., the top rotor and the tail rotor). Your animation will also show the chopper take off and land vertically. Here, you will use your knowledge of *3-D transformations* and the concept of *changing coordinate frames*. 

You will need to label the vertices that belong to each part to be animated so you can control the motion of those individual parts. The motion will be created by transforming (i.e., rotating and translating) the vertices (i.e., point cloud) of the parts. Selecting the different mesh parts can be done either automatically from your program or manually by using mesh-labeling or mesh-cutting tools. 

Once the parts are labeled or selected, you will assign a local coordinate frame to each part and relate them by transformation matrices (i.e., you will create the transformation matrices). As an example of placement of local frames, Figure 2 shows three local coordinate frames that might be used for this assignment, i.e., the main-body coordinate frame, the top-rotor coordinate frame, and the tail-rotor coordinate frame. 

 ![chopper](./chopper.jpg)

**Figure 2**: Local coordinate frames for different parts of the helicopter. 

#### Submission instructions

#####What to submit: 

- **Submit a link to your animation** as a link to a cloud-based drive (e.g., Google Drive, or a link to a video service (e.g., Youtube). Please, do not submit the actual video file as they tend to be large in size. 
- **Submit the code**. Submit the code that you wrote to create the animation (e.g., Python script, Jupyter notebook, Matlab script). Submit the entire code (except for external libraries).  <u>The submission is done via GitHub by pushing the relevant files to the assignment's GitHub repository</u>. 

#### Additional information

##### **On creating animated gif files** 

If you are creating an animated gif file to store the animation, you can do it automatically from your program using library functions (i.e., saving the screenshots to files and combining them into a gif file) or manually using Web-based services that create gif animations from image sequences (you will still have to generate the images, of course). An example of such a service is: [http://gifmaker.me](http://gifmaker.me/) 

##### Studying the mathematical techniques

To complete the assignment, study the course materials on transformations and change of coordinate frames. Course materials include notes, book chapters, lecture slides, and some code examples. To obtain a good understanding of the problem and the underlying theory, you should try to study the whole set of materials.

##### Which library functions can you use? 

You can use any library function that do does perform the actual motion transformations or change-of-frame transformation matrices.  Because this assignment is about implementing geometric transformations using matrix multiplications, you are not allowed to use library functions that implement those transformations, e.g., rotate, scale, translate, rotation-about-an-axis, change of coordinate frames. Instead, you should write your own functions for those transformations. If you are in doubt about what functions to use then ask me. 

#####  Some sample (starter) code in Python

- [**Step-by-step approach with numerical example (simplified 2-D scenario)**.](https://htmlpreview.github.io/?https://github.com/eraldoribeiro/changeOfCoordinates/blob/main/Change_in_coordinate_frames_Example.html) This example assumes the vertices (in the point cloud) are already in local coordinates. When points are given in global coordinates, then their coordinates must be converted from to the local frame prior to applying the desired local transformation. 

- [**Demo code showing the rotation of a single 3-D point in front of the helicopter**. ](https://github.com/eraldoribeiro/changeOfCoordinates/blob/main/animation_CircleAndChopper.py)This demo shows all three parts of the helicopter already segmented and ready to be used to solve the assignment. The demo also shows how to apply the required transformations between frames, i.e., from global to local and then to global again prior to plotting the updated point. This [video](chopper.mp4) shows the program's execution. 

- **Sample code for animations in Vedo**. The Simulation's tab of the [Vedo documentation page ](https://vedo.embl.es/)has examples of animations using the timer and mouse interaction. It is fine to simply generate animations using a loop and key-press interaction. You can also save screenshots of the multiple iterations of your program as images and create a video from them.  

- [Notes on selecting parts of a mesh object using Vedo](https://htmlpreview.github.io/?https://github.com/eraldoribeiro/changeOfCoordinates/blob/main/selectingMeshParts.html). These notes have some suggestions on how to use Vedo's mesh-cutter tools to select the parts of a mesh. If you want to use pre-cut meshes of the helicopter parts, they are available from the following links:

  - [`main_body.vtk`](https://raw.githubusercontent.com/eraldoribeiro/changeOfCoordinates/main/main_body.vtk)
  - [`top_rotor.vtk`](https://raw.githubusercontent.com/eraldoribeiro/changeOfCoordinates/main/top_rotor.vtk)
  - [`tail_rotor.vtk`](https://raw.githubusercontent.com/eraldoribeiro/changeOfCoordinates/main/tail_rotor.vtk)

  which can be downloaded to your local directory. The program [`displayAll.py`](https://github.com/eraldoribeiro/changeOfCoordinates/blob/main/displayAllParts.py)  downloads the partial meshes of the helicopter, and displays them together.  

- [Picking the 3-D location of the local frames (notebook)](https://nbviewer.org/github/eraldoribeiro/rendering3DinColab/blob/main/displayMeshInColabUsingOpen3DandPlotly.ipynb). This notebook uses `Plotly` to visualize the mesh. Plotly displays the coordinates of the 3-D points when we click on the mouse pointer and move the pointer in space.  

 