"""
Click on and adjust viewing angle to activate. 

Press Enter or Space to step through the animation. 

ESC: terminates the program.

"""
from vedo import *
import os
import time          



def RotationAboutY(theta):

    # Matrix of 3-D rotation by angle=theta about the y-axis
    RotY = np.array(
        [
            [np.cos(theta), 0, np.sin(theta), 0],
            [0, 1, 0, 0],
            [-np.sin(theta), 0, np.cos(theta), 0],
            [0, 0, 0, 1],
        ]
    )

    return RotY

def getNewPosition_yellowPoint(p: np.ndarray, angle: float, T_01: np.ndarray) -> np.ndarray:   
    """Obtains the (global) coordinates of a point/object 
    after a rotation about the point's/object's local frame. 

    Args:
      p:     Current position (3x1 np.ndarray) 
      angle: Rotation angle in radians (float)
      T_01:  Transform between the local frame F{1} to the global frame F{0}  (4x4 np.ndarray)

    Returns:
      newPosition: Coordinates of the new location of p (3x1 np.ndarray) 
      
    """

    # Convert point to homogeneous coords
    p_tilde = np.block([[p], [1]])

    # Motion of the yellow point is just a rotation 
    R_y = RotationAboutY(angle)  # Using my own rotation function

    # I want to rotate the point w.r.t. local frame.
    # However, the point's original location is given in global coordinates. 
    # As a result, rotating it about a local frame using just a rotation matrix 
    # will not produce the desired outcome. I need first to convert the point to
    # the local frame, rotate it, and then convert its rotated coordinates back to 
    # the global frame prior to displaying the result. 
        
    # This matrix transforms between the local frame F{0} to the global frame F{1}
    T_10 = np.linalg.inv(T_01)
    
    # The following matrix controls the motion of the point. This matrix 
    # a composition of transformations. First: Convert the coordinates of the 
    # point from global to local coords. Second: Rotate the point. Third: Convert
    # the result from local to global coords.
    T_Motion = T_01 @ R_y @ T_10

    # This is the new location of the yellow point in global coordinates
    p_new = T_Motion @ p_tilde
    
    
    TopRotorPtsNew = (T_01 @ R_z @ T_10) @ TopRotorPtsOld
    TailRotorPtsNew = (T_02 @ R_x @ T_20) @ TailRotorPtsOld
    
    # Convert from homogeneous to Cartesian before returning     
    return p_new[:3] 


def main():
    """
    main function       
    
    """
        
    # Read mesh files of each part, and color-label them
    mainBodyMesh = Mesh("./main_body.vtk").c("white")
    topRotorMesh = Mesh("./top_rotor.vtk").c("red")
    tailRotorMesh = Mesh("./tail_rotor.vtk").c("blue")

    # Create a local coordinade frame (approx.) centered at the front of the chopper.
    # This local frame is just translated w.r.t. to the global frame. Local frame
    # will govern the motion of the yellow point. The motion is just a
    # rotation about the local y-axis.

    # Create a line to visualize the local y-axis
    startPoint, endPoint = (-40, 0, -20), (-40, -20, -20)
    line = Line(startPoint, endPoint).lw(5).c((0, 1, 0))

    # Create a point to provide an example of animation. Point
    # is off-set along the x-axis to show rotation about the local y-axis.
    p = np.array([[-30.0], [-10.0], [-20.0]])

    print("\nThe point in global coordinates = ")
    print(p)

    # Create a Vedo point at location p
    yellowPoint = Point(p, c="y")

    # Transformation matrix from local frame to global (local frame is F{1}).
    # I am centering the frame at the start point of the green line, i.e., startPoint
    T_01 = np.array(
        [
            [1.0, 0.0, 0.0, -40],
            [0.0, 1.0, 0.0,   0],
            [0.0, 0.0, 1.0, -20],
            [0.0, 0.0, 0.0, 1.0],
        ]
    )

    print("\nTransformatiin from local frame F{1} to global frame F{0}:\nT_01 = ")
    print(T_01)

    print("\n")

    # Get new position of point/object 
    theta = np.pi / 6

    # Show everything
    plt = show(
        [mainBodyMesh, topRotorMesh, tailRotorMesh, yellowPoint, line],
        __doc__,
        bg="black",
        bg2="bb",
        interactive=False,
        axes=1,
        viewup="z",
    )


    # "Animation" loop (manual animation)
    for angle in np.arange(0, 4 * np.pi, np.pi / 20):

        # Get updated position of point/object 
        p_new = getNewPosition_yellowPoint(p, angle, T_01)

        # Update object's position (leave a trail behind, just for fun!)
        yellowPoint.pos(p_new).add_trail(n=20)

        # Display scene and objects
        plt.pop().show(
            [mainBodyMesh, topRotorMesh, tailRotorMesh, yellowPoint, line],
            __doc__,
            bg= "black",
            bg2= "bb",
            viewup= "z",
            interactive = True
        )

    plt.close()

    

if __name__=="__main__":
    main()
    
    
