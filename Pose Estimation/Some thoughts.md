# [Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation)

## Limbs
1. Plot the **same limbs** with the **same color**, or the output video would be **bad** :dizzy_face: <br>
  you can use this:
    ```python
      # For cv2
      colors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0],
            [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255],
            [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85]]

      # For matplotlib.pyplot
      colors = [[item / 255 for item in subl] for subl in colors]
    ```
 
## Drawing
1. Plot **body parts** using *plt.plot* instead of *plt.scatter*

2. 
