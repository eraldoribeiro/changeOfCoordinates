# Converting from local to global coordinates



## **Example**: Spinning circles at the end of a line segment

Consider a horizontal line segment $\overline{AB}$ as the one shown in Figure 1. The line segment has a circle ``attached" to points $A$ and $B$. The blue circle rotates around $A$ while the pink circle rotates around $B$. The rotation radius of the blue circle is 5 and the rotation radius of the pink circle is 2. Point $A$ (i.e., the start of the line segment) is located away from the global origin (i.e., frame ${\mathcal F}\{0\}$). 

<img src="./object.png" alt="object" style="zoom:40%;" />

**Figure 1**: Object with two rotating parts (i.e., blue and pink circles). The blue circle rotates around point $A$ while the pink circle rotates around point $B$. Their frequencies of rotation may be different. The world coordinate system is labeled as frame ${\mathcal F}\{0\}$.

Our goal is to create the transformations that will rotate the two circles around their centers of rotation. Once the transformations are at hand, we can use them to create an animation of the entire system in motion. 

We can solve this problem by performing the following steps: 

1. **Place local coordinate systems centered at strategic locations**. In addition to choosing a location, we also choose the best orientation (i.e., pose) of the local coordinate system. 
2. **Create Local-to-Global transformation matrices**. These are the matrices that convert local coordinates to global coordinates. Local coordinates are convenient for calculations but we need global coordinates in order to render the graphical output of the animation. 
3. **Create the matrices of the local transformations** (e.g., rotations, scaling) on the points (i.e., object parts) associated to the local coordinate frames. These transformations result in transformed points in local coordinates. 
4. **Convert the coordinates of the transformed local parts to global coordinates prior to plotting the results.**  Plotting functions, i.e., library functions such as `plot(x,y)` only know how to plot global coordinates. As a result, any point in local coordinates must its coordinates converted to the global frame prior to plotting. 



### Step 1: Place local coordinate systems centered at strategic locations

Our first step is to choose the best locations and orientations of local coordinate systems that will help us solve the problem. We can create as many coordinate systems as we want. The ones we will use here will be centered at the points $A$ and $B$ because we want the spheres to rotate around those points. The configuration of local frames shown in Figure 2 is one possibility out of many. 

<img src="./object_systems.png" alt="object_systems" style="zoom:40%;" />

**Figure 2**: The object's end points are $A = (8,9)^\mathsf{T}$ and $B = (18,9)^\mathsf{T}$.  Points ${\bf p}$ and ${\bf q}$ are the centers of the blue and pink circles, respectively.

In this choice of configuration, all local frames are just translated with respect to the world-coordinate frame (i.e., there is no rotation between the frames). Depending on the application, the local frames may also be rotated with respect to the global frame and, sometimes, they also rotated with respect to one another. 

### Step 2: Create the local-to-global transformation matrices

We create the local-to-global transformation matrices for each local frame. 

1. Transformation ${\mathcal F}\{1\} \rightarrow {\mathcal F}\{0\}$. It is named $T_{01}$ and describes the pose (i.e., rotation and translation) of local frame ${\mathcal F}\{1\}$ w.r.t. frame ${\mathcal F}\{0\}$ which is the global frame. The transformation matrix is given by:

$$
\begin{align}
 {T}_{01} =  
  \begin{bmatrix}    
    	R_{01} & {\bf t}_{01}\\        
    	{\bf 0} &  1  
  \end{bmatrix}  
   = 
  \begin{bmatrix}    
    	1 & 0 & 8\\     
    	0 & 1 & 9\\        
    	0 & 0 & 1  
   \end{bmatrix}.
\end{align}
$$

In the example described in these notes, there is no rotation between frames ${\mathcal F}\{1\}$ and ${\mathcal F}\{0\}$, i.e., $R_{01}=I$. The origin of  ${\mathcal F}\{1\}$ is translated by ${\bf t}_{01} = (8,9)^\mathsf{T}$ w.r.t. frame ${\mathcal F}\{0\}$.

2. Transformation ${\mathcal F}\{2\} \rightarrow {\mathcal F}\{0\}$. It is named $T_{02}$ and describes the pose (i.e., rotation and translation) of local frame ${\mathcal F}\{2\}$ w.r.t. frame ${\mathcal F}\{0\}$. The transformation matrix is given by:

$$
\begin{align}
	{T}_{02} =  
  \begin{bmatrix}    
    	R_{02} & {\bf t}_{02}\\        
    	{\bf 0} &  1  
   \end{bmatrix}  
   = 
  \begin{bmatrix}    
    	1 & 0 & 18\\     
    	0 & 1 & 9\\        
    	0 & 0 & 1  
   \end{bmatrix}.
 \end{align}
$$

There is also no rotation between frames ${\mathcal F}\{2\}$ and ${\mathcal F}\{0\}$. The origin of  ${\mathcal F}\{2\}$ is translated by ${\bf t}_{02} = (18,9)^\mathsf{T}$ w.r.t. frame ${\mathcal F}\{0\}$.

### Step 3: Create the matrices of the local transformations

We now build the rotation matrices that will govern the motions of the points  ${\bf p}$ and  ${\bf q}$  in their local coordinate systems. 

1. The rotation of blue circle about its local origin:
   $$
   \begin{align}
   	R_{\theta} = 
   	  \begin{bmatrix}    
       	\sin{\theta} & -\cos\theta\\        
       	\cos\theta &  \sin\theta  
      \end{bmatrix}  
    \end{align}
   $$

2. The rotation of pink circle about its local origin:
   $$
   \begin{align}
   	R_{\phi} = 
   	  \begin{bmatrix}    
       	\sin{\phi} & -\cos\phi\\        
       	\cos\phi &  \sin\phi  
      \end{bmatrix}  
    \end{align}
   $$

### Numerical examples

Now, let's try to rotate the points to see how the whole works. First, we can rotate the blue circle by an angle $\theta = \pi/4$. To do that, we will apply the rotation to the initial location of ${\bf p}_{\{1\}} = (5,0)^\mathsf{T}$ in local coordinates (See measurements in the diagram). We will write $\tilde{\bf p}_{\{1\}}$ to indicate the homogeneous representation of point  ${\bf p}_{\{1\}}$. The rotation calculation in homogeneous coordinates as follows: 
$$
\begin{align}
	\tilde{\bf p}^\prime_{\{1\}} 
	&= 
	  \begin{bmatrix}    
    	R_{\theta} & {\bf 0}\\        
    	{\bf 0} &  1  
   \end{bmatrix} 
   \tilde{\bf p}_{\{1\}}.
 \end{align}
$$
Note that the rotated point  $\tilde{\bf p}^\prime_{\{1\}}$ is written in terms of its local coordinate system (i.e., frame ${\mathcal F}\{1\}$ ). As a result, the rotated point will not be plotted at its expected location when using library functions such as `plot(x,y)`. Library plotting functions use global (world) coordinates, not local ones. Thus, prior to plotting the rotated point, we must convert its coordinates to global coordinates, i.e.: 
$$
\begin{align}
	\tilde{\bf p}^\prime_{\{0\}} &= {T}_{01}\tilde{\bf p}^\prime_{\{1\}}, \notag \\ \notag\\
  \begin{bmatrix}    
  x_p^\prime \\     
  y_p^\prime \\    
  1  
  \end{bmatrix}_{\{0\}}
&=
	  \underbrace{\begin{bmatrix}          
	       R_{01} & {\bf t}_{01}\\  
        {\bf 0} &  1     
    \end{bmatrix}}_{\text{local-to-global}}  
	  \underbrace{\begin{bmatrix}    
    	R_{\theta} & {\bf 0}\\        
    	{\bf 0} &  1  
   \end{bmatrix}}_{\text{local motion}}  
	\begin{bmatrix}
	  x_p \\ 
	  y_p \\
	  1
  \end{bmatrix}_{\{1\}}.
 \end{align}
$$
Numerically, the global representation of the rotation of $\tilde{\bf p}_{\{1\}} = (5,0,1)^\mathsf{T}$ by an angle angle $\theta = \pi/4$ around point $A$ is:
$$
\begin{align}
  \begin{bmatrix}    
  x_p^\prime \\     
  y_p^\prime \\    
  1  
  \end{bmatrix}_{\{0\}}
&=
  \begin{bmatrix}          
  1 & 0 & 8\\           
  0 & 1 & 9\\              
  0 & 0 & 1     
  \end{bmatrix}	  
  \begin{bmatrix}    
    \sin(\pi/4) & -\cos(\pi/4)  & 0\\        
    \cos(\pi/4) & \sin(\pi/4)   & 0 \\
    	        0 &      0        & 1    
   \end{bmatrix}    
	\begin{bmatrix}
	  5 \\ 
	  0 \\
	  1
  \end{bmatrix}_{\{1\}}   \notag\\
&=  
	\begin{bmatrix}
	  11.5 \\ 
	  12.5 \\
	  1
  \end{bmatrix}_{\{0\}}, 
\end{align}
$$
which are the expected coordinates of the rotated point's position when plotted. 

To rotate the pink circle by an angle $\phi$ around the circles' local frame, we apply a local rotation to ${\bf q}_{\{2\}} = (2,0)^\mathsf{T}$, in local coordinates. Here, we use the transformation matrix that converts from frame ${\mathcal F}\{2\}$ to frame ${\mathcal F}\{0\}$, i.e., $T_{02}$. The equation is given by:  
$$
\begin{align}
	\tilde{\bf q}^\prime_{\{0\}} &= {T}_{02}\tilde{\bf q}^\prime_{\{2\}}, \notag \\ \notag\\
  \begin{bmatrix}    
  x_q^\prime \\     
  y_q^\prime \\    
  1  
  \end{bmatrix}_{\{0\}}
&=
	  \underbrace{\begin{bmatrix}          
	       R_{02} & {\bf t}_{02}\\  
        {\bf 0} &  1     
    \end{bmatrix}}_{\text{local-to-global}}  
	  \underbrace{\begin{bmatrix}    
    	R_{\phi} & {\bf 0}\\        
    	{\bf 0} &  1  
   \end{bmatrix}}_{\text{local motion}}  
	\begin{bmatrix}
	  x_q \\ 
	  y_q \\
	  1
  \end{bmatrix}_{\{2\}}.
 \end{align}
$$
After a local rotation by an angle $\phi = \pi/3$ around point $B$, followed by the change-of-frame transformation, the global coordinates of $\tilde{\bf q}_{\{2\}} = (2,0,1)^\mathsf{T}$ are:
$$
\begin{align}
  \begin{bmatrix}    
  x_q^\prime \\     
  y_q^\prime \\    
  1  
  \end{bmatrix}_{\{0\}}
&=
  \begin{bmatrix}          
  1 & 0 & 18\\           
  0 & 1 & 9\\              
  0 & 0 & 1     
  \end{bmatrix}	    
\begin{bmatrix}        
	\sin(\pi/3) & -\cos(\pi/3)  & 0\\            
	\cos(\pi/3) & \sin(\pi/3)   & 0 \\              
	0 &      0        & 1       
\end{bmatrix}	\begin{bmatrix}
	  2 \\ 
	  0 \\
	  1
  \end{bmatrix}_{\{2\}}   \notag\\
&=  
	\begin{bmatrix}
	  19.7 \\ 
	  10.0 \\
	  1
  \end{bmatrix}_{\{0\}}, 
\end{align}
$$
which are the expected coordinates of the rotated point's position when plotted. 
